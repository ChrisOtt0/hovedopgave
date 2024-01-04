import os
import sys
import socket
import subprocess

BUFFER_SIZE = 4096
FORMAT = 'utf-8'
HOST = "0.0.0.0"
PORT = 5002
TEMP_PATH = "/home/agramkow/.config/AGRAMKOW/rflash/temp"

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind((HOST, PORT))
S.listen(1)


def recv_data(conn: socket.socket):
    """
    Recv function.\n
    Retrieves the update package from TCP/IP socket connection
    """

    # Receive filename
    try:
        bin_name = conn.recv(BUFFER_SIZE).decode(FORMAT).rstrip("\r").rstrip("\n")
    except:
        raise

    bin_path = os.path.join(TEMP_PATH, bin_name)

    # Open file and write in bytes
    with open(bin_path, "wb") as f:
        # While data, receive and write
        while True:
            try:
                data = conn.recv(BUFFER_SIZE)
            except:
                raise

            if not data:
                break

            f.write(data)


# Main function
if __name__ == '__main__':
    while True:
        try:
            (conn, (ip, port)) = S.accept()

        # Passed to continue listening
        except socket.timeout:
            pass

        # For testing purposes
        except KeyboardInterrupt:
            sys.exit(0)

        # Should be handled
        except Exception as e:
            pass

        # If connection is established
        else:
            try:
                recv_data(conn)

            # Close connection on error and raise error
            except:
                conn.close()
                raise

            else:
                # Flash device
                # os.system call
                if not os.system("/home/agramkow/code/jlink/./JLinkExe -device R7FA6M2AF3CFB -if JTAG -jtagconf -1,-1 -speed 4000 -CommanderScript /home/agramkow/.config/AGRAMKOW/rflash/commandfiles/3PHPM.jlink") == 0:
                    conn.sendall("Err".encode(FORMAT))
                    conn.close()
                    continue

                # Send response
                conn.sendall("Ok".encode(FORMAT))

                # Close conn
                conn.close()
                continue