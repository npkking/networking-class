# UDPEchoServer

from socket import *

s = socket(AF_INET,SOCK_DGRAM)

server_addr = ("", 10000)
print('starting up on ', server_addr)
s.bind(server_addr)
while True:
    print("waiting to receive message")
    data, addr = s.recvfrom(4096)
    data = data.decode()
    if data:
        sent = s.sendto(data.encode(), addr)


# UDPEchoClient
from socket import *

#Create a UDP socket
s = socket(AF_INET, SOCK_DGRAM)
server_addr = ('192.168.1.10', 10000)
message = "This is the message."

try:
    # Send data
    print('sending "%s" ' %message)
    sent = s.sendto(message.encode(), server_addr)

    #Receive response
    print('waiting to receive ...')
    data, server = s.recvfrom(4096)
    print('received "%s"' %data.decode())
finally:
    print('closing socket')
    s.close()
    