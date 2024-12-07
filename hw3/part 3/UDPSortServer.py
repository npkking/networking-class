import numpy as np
from socket import *


def sorting(command, sequence):
    if command == "asc":
        sequence.sort()
        return sequence
    elif command ==  "desc":
        sequence.sort(reverse = True)
        return sequence


bufmax = 10 #max size taken

s = socket(AF_INET, SOCK_DGRAM)

s.bind(("localhost", 3000))

while True:
    sequence = []
    
    while True: #getting the trunk
        data, addr = s.recvfrom(bufmax)
        data = data.decode()
        if data == "":
            break
        else:
            sequence.append(data)
    
    #concatenate string
    sequence = "".join(sequence)
    int_sequence = sequence.split(" ")
    int_sequence = [int(element) for element in int_sequence]

    command, addr = s.recvfrom(bufmax)
    command = command.decode()
    int_sequence = sorting(command, int_sequence)

    result_sequence = [str(element) for element in int_sequence]
    message = " ".join(result_sequence)

    chunk_size = 10 #bytes
    chunks = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)] #initialize list of chunks
    for seq, chunk in enumerate(chunks): #using the enumerate to get the index and the data at the same time
        print(f"Sending chunk #{seq} with message {chunk}")
        s.sendto(chunk.encode(), addr)
    s.sendto("".encode(), addr)

    print(f"Server is serving client {addr[0]}:{addr[1]}")

    data, addr = s.recvfrom(bufmax)
    data = data.decode()

    if data == "close":
        break
    elif data == "continue":
        continue

print("Closing the socket")
s.close()