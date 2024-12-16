from socket import *
import time
from ssl import SSLContext, PROTOCOL_TLS_CLIENT



host = "Kay"
address = ("127.0.0.1", 3000)



def main():
    context = SSLContext(PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("hw5/part4/sth.pem")

    with create_connection(address) as client:
        with context.wrap_socket(client, server_hostname=host) as tls:
            while True:
                command = input("Please type down the command (if write please use write key:value syntax): ")
                tls.sendall(command.encode())
                if command.lower() == "close":
                    break
                data = tls.recv(2048).decode()
                print(data)

            tls.close()

if __name__ == "__main__":
    main()
