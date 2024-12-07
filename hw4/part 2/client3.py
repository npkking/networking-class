from socket import *


bufsize = 10 
address = ("localhost", 3000)


client = socket(AF_INET, SOCK_STREAM)
client.connect(address)


while True:
    sequence = input("Please type down your intergers sequence you want to sort: ")

    chunk_size = 10 #bytes
    print(len(sequence))
    chunks = [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)] #initialize list of chunks
    client.sendall(str(len(chunks)).encode())
    for seq, chunk in enumerate(chunks): #using the enumerate to get the index and the data at the same time
        print(f"Sending chunk #{seq} with message {chunk}")
        client.sendall(chunk.encode())

    command = input("Please enter the command either asc or desc to sort: ")
    client.sendall(command.encode())

    res = []
    chunk_size = int(client.recv(1024).decode())
    for i in range (chunk_size): #getting the trunk
        data = client.recv(bufsize).decode()
        res.append(data)
    res = "".join(res)
    print(f"The sorted string is {res}")

    choice = input("Do you still want to sort things? ")
    if choice.lower() == "no" or choice.lower() == "n":
        client.sendall("close".encode())
        break
    elif choice.lower() == "yes" or choice.lower() == "y":
        client.sendall("continue".encode())
        continue
    else:
        print("Error. Program is suspended")
        break

client.close()