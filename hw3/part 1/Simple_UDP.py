# Simple UDP Server
from socket import *

maxsize = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 10000)) #bind to all IP already

while True:
    data, addr = s.recvfrom(maxsize)
    print(data.decode())
    resp = "Get off my lawn!".encode()
    s.sendto(resp, addr)

#Simple UDP Client

from socket import *

maxsize = 1024

s = socket(AF_INET, SOCK_DGRAM)
msg = "Hello World".encode()
s.sendto(msg, ("192.168.1.10", 10000))
data, addr = s.recvfrom(maxsize)
print(data)