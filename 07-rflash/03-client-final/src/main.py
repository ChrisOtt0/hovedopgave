import os
import sys
import socket
import tomllib
import json
import tarfile
from modules.args import get_args
from modules.pysecag import AGSigner

IP = "192.168.1.44"
PORT = 5002
FORMAT = "utf-8"
BUFFER_SIZE = 4096

VALIG_CONF_OPTS = ["device", "interface", "jtagconf", "speed"]


if __name__ == "__main__":
    # Get args: configuration path and binary path
    args = get_args()
    retries = args.retries

    # Conf validation
    print("Validating conf.toml...")
    conf = None
    try:
        with open(args.configpath, "rb") as f:
            conf = tomllib.load(f)
    except Exception as e:
        print("Invalid conf.toml file: {}".format(e))
        sys.exit(1)

    for key in conf.keys():
        if not key in VALIG_CONF_OPTS:
            print("Invalid conf.toml file content. Key {} is not valid.".format(key))

    bin_name = args.binarypath.rsplit(os.sep, 1)[1]

    # Generate tarball
    while retries:
        print("Generating tarball...")
        filename = "rflash.tar.gz"
        with tarfile.open(filename, "w:gz") as tar:
            tar.add(args.configpath, arcname=os.path.basename(args.configpath))
            tar.add(args.binarypath, arcname=os.path.basename(args.binarypath))

        # Sign tarball
        print("Signing tarball...")
        agsigner = AGSigner(os.path.join(args.keydir, "agprivkey"), os.path.join(args.keydir, "agsymkey"))
        signature = None
        
        try:
            signature = agsigner.sign(filename)
        except Exception as e:
            print(e)
            sys.exit(1)
        
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((IP, PORT))

            # Send as according to the protocol
            with open(filename, "rb") as f:
                print(f"Sending {filename}: {os.path.getsize(filename)}")
                client.sendall(filename.encode() + b"\n")
                client.sendall(f"{os.path.getsize(filename)}".encode() + b"\n")
                client.sendall(signature + b"\n")

                # Send file in chunks, so large files can be handled
                while True:
                    data = f.read(BUFFER_SIZE)
                    if not data: break
                    client.sendall(data)

            client.shutdown(socket.SHUT_WR)

            # Wait for output
            try:
                print("Sent file successfully. Waiting for output...")
                response = client.recv(BUFFER_SIZE).decode(FORMAT).rstrip("\r").rstrip("\n")
                response_json = json.loads(response)
                if response_json["status"] == 1:
                    print("An error ocurred receiving JLink Flash output data: {}".format(response_json["err"]))
                    retries -= 1
                    print(f"Retries left: {retries}")
                    continue
                else:
                    print(response_json["data"])
                    response_lines = response_json["data"].split("\n")
                    if len(response_lines) < 10:
                        sys.exit(1)

                    ok_line = response_lines[-9]
                    if ok_line != "O.K.":
                        print("Flashing failed.")
                        sys.exit(1)

            except Exception as e:
                print("An unexpected error ocurred: {}".format(e))
                sys.exit(1)

        except Exception as e:
            print("An error occured while processing: {}".format(e))
            sys.exit(1)
        
        finally:
            # Cleanup
            os.remove(filename)
            if os.path.isfile(signature):
                os.remove(signature)

