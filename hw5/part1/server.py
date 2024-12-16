from socket import *
from ssl import SSLContext, PROTOCOL_TLS_SERVER

ip = '127.0.0.1'
port = 8443
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="hw5/part1/KayKay.pem", keyfile="hw5/part1/private.key")

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen()
    with context.wrap_socket(server, server_side=True) as tls:
        while True:
            conn, addr = tls.accept()
            print(f'Connected by {addr}\n')
            data = conn.recv(1024)
            print(f"Client says: {data}")
            conn.sendall(b"You're welcome")
            conn.close()