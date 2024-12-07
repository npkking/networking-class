#For this assignment, I assume the prefix input from client having space " " between terms

from socket import *
from threading import *


def prefixEvaluation(data):
    stack = [] # stack for storing the operands, use the one on the leftmost known first
    tokens = data.split() #split the term using the space

    for token in reversed(tokens):
        if(token.isdigit()): #positive number
            stack.append(int(token))
        elif(token.lstrip("-").isdigit()):
            stack.append(int(token))
        else:
            operand1 = stack.pop() #pop the last item
            operand2 = stack.pop()
            if token == "+":
                res = operand1+operand2
                stack.append(res)
            elif token == "-":
                res = operand1-operand2
                stack.append(res)
            elif token == "*":
                res = operand1 * operand2
                stack.append(res)
            elif token == "/":
                res = operand1/operand2
                stack.append(res)
    return stack.pop()

def on_connection(client_socket, client_address):
    while True:
        request = client_socket.recv(1024).decode("utf-8")

        if request.lower() == "close":
             client_socket.send("closed".encode("utf-8"))
             print(f"Closing connection with {client_address[0]}:{client_address[1]}")
             break
        
        print(f"Received: {request} from {client_address[0]}:{client_address[1]}")
        response = str(prefixEvaluation(request)).encode("utf-8")
        client_socket.sendall(response)

    client_socket.close()

server = socket(AF_INET, SOCK_STREAM)
server_ip = "127.0.0.1"
port = 8000
server.bind((server_ip, port)) #tuple
server.listen(5)
print(f"Listening on {server_ip}:{port}")

while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]}")
    t = Thread(target=on_connection, args=(client_socket,client_address))
    t.start()
    


