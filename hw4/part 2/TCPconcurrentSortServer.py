from socket import *
import threading


bufmax = 10 #max size taken
address = ("localhost", 3000)


def sorting(command, sequence):
    if command == "asc":
        sequence.sort()
        return sequence
    elif command ==  "desc":
        sequence.sort(reverse = True)
        return sequence

def on_connection(client_socket, client_address):
    while True:
        sequence = []
        chunk_size = int(client_socket.recv(1024).decode())

        for i in range(chunk_size): #getting the trunk
            data = client_socket.recv(bufmax).decode()
            sequence.append(data)

        #concatenate string
        sequence = "".join(sequence)
        int_sequence = sequence.split(" ")
        int_sequence = [int(element) for element in int_sequence]

        command = client_socket.recv(bufmax)
        command = command.decode()
        print(command)
        int_sequence = sorting(command, int_sequence)

        result_sequence = [str(element) for element in int_sequence]
        message = " ".join(result_sequence)

        chunk_size = 10 #bytes
        chunks = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)] #initialize list of chunks
        client_socket.sendall(str(len(chunks)).encode())
        for seq, chunk in enumerate(chunks): #using the enumerate to get the index and the data at the same time
            print(f"Sending chunk #{seq} with message {chunk}")
            client_socket.sendall(chunk.encode())

        data = client_socket.recv(bufmax)
        data = data.decode()

        if data == "close":
            break
        elif data == "continue":
            continue

    print(f"Closing the socket of {client_address[0]}:{client_address[1]}")
    client_socket.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen(5)
print(f"Server is operating on {address[0]}:{address[1]}")

while True:
    client_socket, client_address = server.accept()
    print(f"Server is connecting to {client_address[0]}:{client_address[1]}")
    t = threading.Thread(target=on_connection, args=(client_socket,client_address))
    t.start()
    

