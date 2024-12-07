from socket import *
import time



address = ("127.0.0.1", 3000)



def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(address)
    while True:
        command = input("Please type down the command (if write please use write key:value syntax): ")
        client.sendall(command.encode())
        if command.lower() == "close":
            break
        data = client.recv(2048).decode()
        print(data)

    client.close()

if __name__ == "__main__":
    main()
