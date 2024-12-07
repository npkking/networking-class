#Part 1 code will be fixed here
# TCP CLient
import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server_ip = "203.0.113.25"  # server's IP address (not localhost)
server_port = 8000       # server's port number 
client.connect((server_ip, server_port)) 

while True: 
    msg = input("Enter message: ") 
    client.send(msg.encode("utf-8")[:1024])  # send msg to server 
    response = client.recv(1024).decode("utf-8") # receive response 

    # on receiving "closed", we break and close the socket 
    if response.lower() == "closed": 
        break 
    
    print(f"Received: {response}")  # print resonse 

client.close() # close client socket





#TCP Server
import socket 

# create server socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_ip = "0.0.0.0" # Bind to all available network interfaces
port = 8000 
server.bind((server_ip, port)) # bind to address and port 
server.listen(0)  # listen for incoming connections 
print(f"Listening on {server_ip}:{port}") 

# accept incoming connections 
client_socket, client_address = server.accept() 
print(f"Conn from {client_address[0]}:{client_address[1]}")

# receive data from the client 
while True: 
    request = client_socket.recv(1024).decode("utf-8") 
    
    # if we receive "close", then break and close 
    if request.lower() == "close": 
        # send response that the connection is closed 
        client_socket.send("closed".encode("utf-8")) 
        break 
    
    print(f"Received: {request}") 
    response= "accepted".encode("utf-8") 
    client_socket.send(response) 
client_socket.close() # close connection with the client 
print("Connection to client closed") 
server.close() # close server socket





#TCP Echo Client
import socket
#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server listenting port
server_address = ('203.0.113.25', 10000)
sock.connect(server_address)
try: 
    message = 'This is the message'
    print('sending', message)
    sock.sendall(message.encode())  #send data

    amount_received = 0
    amount_expected = len(message)
    msg = []

    while amount_received < amount_expected: # Loop for response
        data = sock.recv(16)
        amount_received += len(data)
        msg.append(data)
    
    print('received', b''.join(msg).decode()) # return the concatenation of the strings in msg

finally:
    print('closing socket')
    sock.close()





#TCP Echo Server
import socket

# Create a TCP/IP socket
sock = socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('starting up on port ', server_address)
sock.bind(server_address)

#Listen for incoming connections
socket.listen(1)
while True: #server loop
    print('waiting for a connection')
    connection, client_address = sock.accept() # Wait first
    try:
        print('connection from', client_address)
        while True: # Data procesing loop
            data = connection.recv(16)  # Receive data in chunks up to 16 bytes
            print('received ', data) 
            if data: 
                print('sending data back to the client') 
                connection.sendall(data)  # Retransmit it back 
            else: 
                print('no data from', client_address) 
                break 
    finally:  # Clean up the connection 
        connection.close()