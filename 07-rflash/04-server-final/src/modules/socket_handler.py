import socket
import sys
import json
import os, errno
import logging
import tarfile
import tomllib
import shutil

from .pysecag import AGVerifier
from .config import Config
from .jlink_script_handler import JLinkScriptHandler


logger = logging.getLogger("rflash.socket_handler")


BUFFER_SIZE = 4096
FORMAT = 'utf-8'
HOST = "0.0.0.0"
PORT = 5002
TEMP_PATH = "/var/tmp/rflash"
KEYDIR = os.path.join("/home", "agramkow", ".config", "AGRAMKOW", "keys")


class SocketHandler:
    def __init__(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((HOST, PORT))
        self.__socket.listen(1)

    def handle(self):
        """
        Starts listening on port 5002. If a socket connection is established, the handler gets the configuration and parses it.
        If the configuration is valid, the handler gets the name of the binary file and it's data, creating the binary file to be flashed.
        Finally the handler flashes the device.
        """
        while True:
            try:
                conn = self.__get_conn()

            except Exception as err:
                logger.error(err)

            # If a connection is established
            else:
                try:
                    logger.info("Making tmp dir...")

                    try:
                        os.makedirs(TEMP_PATH)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise

                    # Get signature & file
                    logger.info("Getting signature and file...")
                    (filepath, signature) = self.__get_file(conn)

                    # Verify data
                    logger.info("Verifying data...")
                    agverifier = AGVerifier(os.path.join(KEYDIR, "agpubkey"), os.path.join(KEYDIR, "agsymkey"))
                    if not agverifier.verify(filepath, signature):
                        self.__send_err(conn, "Received file could not be verified!")
                        raise Exception("Received file could not be verified!")
                    
                    # Unpack
                    logger.info("Extracting tarball...")
                    with tarfile.open(filepath) as tar:
                        tar.extractall(TEMP_PATH)
                    os.remove(filepath)

                    # Get conf & binary
                    conf = self.__get_conf()
                    bin_path = self.__get_bin()

                    # TryFlash, return output
                    flasher = JLinkScriptHandler(conf)
                    output = flasher.handle(bin_path)
                    self.__send_ack(conn, data=output)
                
                # On error, close socket and log error
                except Exception as err:
                    logger.error(err)
                
                # Finally, close socket and continue loop
                finally:
                    self._cleanup(conn)
                    continue

    def __get_conn(self):
        """
        Loops until connection is gotten.\n
        Returns accepted connection.
        """
        conn = None
        while True:
            try:
                logger.info("Listening for socket connections on port: {}".format(PORT))
                (conn, (ip, port)) = self.__socket.accept()
            
            # Continue listening, even if nothing happens
            except socket.timeout:
                pass

            # For debugging, to be able to close application
            except KeyboardInterrupt:
                sys.exit(0)

            except Exception as err:
                raise err

            # If connection established:
            else:
                logger.info("Accepted connection. [{}:{}]".format(ip, port))
                return conn
                

    def __get_file(self, conn: socket.socket) -> (str, bytes):
        """
        Receives the file.
        Treat socket as a file, as protocol is newline based. Received artefacts are:
            - filename
            - filesize
            - signature
            - file data

        Returns the path to the file and the signature.
        """
        logger.info("Receiving file...")
        filename = None
        filesize = None
        signature = None

        # Treat socket as file
        with conn.makefile("rb") as clientf:
            # Get protocol artefacts
            filename = clientf.readline().strip().decode()
            filesize = int(clientf.readline())
            signature = clientf.readline().strip()

            filepath = os.path.join(TEMP_PATH, filename)

            # File recv in chunks, for bigger files
            with open(filepath, "wb") as f:
                while filesize:
                    chunk = min(filesize, BUFFER_SIZE)
                    data = clientf.read(chunk)
                    if not data: break
                    f.write(data)
                    filesize -= len(data)

            # If filesize isn't zero, something wen't wrong in the transfer, either loss of bytes or too many bytes
            if filesize != 0:
                raise Exception("Invalid file download.")
            else:
                return (filepath, signature)


    def __get_conf(self) -> str:
        """
        Gets conf object from TEMP_PATH
        """
        logger.info("Getting configuration...")

        # Get conf_path
        files = os.listdir(TEMP_PATH)
        conf_path = None

        for file in files:
            if ".toml" in file:
                conf_path = os.path.join(TEMP_PATH, file)
                break

        if conf_path is None:
            raise Exception("No configuration found in received tarball...")
        
        # Get conf
        conf = None
        try:
            with open(conf_path, "rb") as f:
                conf = Config(json.dumps(tomllib.load(f)))
        except Exception as e:
            logger.error("Invalid toml file received: {}".format(e))
            raise Exception("Invalid toml file received: {}".format(e))

        # Return conf
        return conf
    

    def __get_bin(self) -> str:
        """
        Gets binary path from TEMP_PATH
        """
        logger.info("Getting binary path...")

        files = os.listdir(TEMP_PATH)
        bin_path = None

        for file in files:
            if ".elf" in file or ".hex" in file:
                bin_path = os.path.join(TEMP_PATH, file)
                break

        if bin_path is None:
            raise Exception("No binary file found in received tarball...")
        
        return bin_path
    
    
    def __send_ack(self, conn: socket.socket, data: str):
        """
        Sends ACK with output to client.
        """
        ack = json.dumps({"status": 0,"data": data})
        try:
            conn.sendall(ack.encode(FORMAT))
        except Exception as e:
            raise Exception("Error sending ACK to client: {}", e)
        
    def __send_err(self, conn: socket.socket, err: str):
        """
        Sends ERR to client.
        """
        err = json.dumps({"status": 1, "err": err})
        try:
            conn.sendall(err.encode(FORMAT))
        except Exception as e:
            raise Exception("Error sending ACK to client: {}", e)


    def _cleanup(self, conn: socket.socket):
        """
        Cleans up connection data. This includes removing the flashed binary and closing the connection.
        """
        logger.info("Removing temp files...")
        shutil.rmtree(TEMP_PATH)

        logger.info("Closing connection...")
        conn.close()