from socket import *

bufsize = 20 #20 bytes so at max 5 integers

s = socket(AF_INET, SOCK_DGRAM)

while True:
    sequence = input("Please type down your intergers sequence you want to sort: ")

    chunk_size = 10 #bytes
    print(len(sequence))
    chunks = [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)] #initialize list of chunks
    for seq, chunk in enumerate(chunks): #using the enumerate to get the index and the data at the same time
        print(f"Sending chunk #{seq} with message {chunk}")
        s.sendto(chunk.encode(), ("localhost", 3000))
    s.sendto("".encode(), ("localhost", 3000))

    command = input("Please enter the command either asc or desc to sort: ")
    s.sendto(command.encode(), ("localhost", 3000))

    res = []
    while True: #getting the trunk
        data, addr = s.recvfrom(bufsize)
        data = data.decode()
        if data == "":
            break
        else:
            res.append(data)
    res = "".join(res)
    print(f"The sorted string is {res}")

    choice = input("Do you still want to sort things? ")
    if choice.lower() == "no" or choice.lower() == "n":
        s.sendto("close".encode(), ("localhost", 3000))
        break
    elif choice.lower() == "yes" or choice.lower() == "y":
        s.sendto("continue".encode(), ("localhost", 3000))
        continue
    else:
        print("Error. Program is suspended")
        break

s.close()