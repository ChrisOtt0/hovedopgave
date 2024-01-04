import os
import sys
import socket

IP = "192.168.1.44"
PORT = 5002
FORMAT = "utf-8"
BUFFER_SIZE = 4096


if __name__ == "__main__":
    # Get binary file path and name from argv
    bin_path = sys.argv[1]
    bin_name = bin_path.rsplit(os.sep, 1)[1]
    
    # Send name and file
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))

        # Send name
        client.sendall(bin_name.encode(FORMAT))

        # Open file and send
        with open(bin_path, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break

                client.send(bytes_read)

        client.shutdown(socket.SHUT_WR)

    except:
        print("Error sending file.")
        raise

    # Wait for answer
    while True:
        try:
            answer = client.recv(BUFFER_SIZE).decode(FORMAT)
            print(answer)
            break
        
        except socket.timeout:
            pass
        except:
            raise