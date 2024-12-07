from socket import *


client = socket(AF_INET, SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 8000
client.connect((server_ip, server_port))

while True:
    prefix = input("Please type down the arithmetic expression with space in prefix form: ")
    client.sendall(prefix.encode("utf-8"))
    receive = client.recv(1024).decode("utf-8")

    if receive.lower() == "closed":
        print("Closing connection with the server from now!")
        break

    print(f"The evaluation result responsed from the prefix: {prefix} is {receive}")
    print()

client.close()