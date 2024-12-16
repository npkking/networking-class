from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER
ip= '127.0.0.1'
port = 8443
context= SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="private.key")
# cert&key#context.load_cert_chain('cert.pem', 'keyNoPwd.key')
#context.load_cert_chain('cert.pem', 'private.key', 'pwd')
with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen(1)
    with context.wrap_socket(server, server_side=True) as tls:
        while True:  # service loop
            conn, addr = tls.accept()
            print(f'Connectedby {addr}\n')
            data = conn.recv(1024)
            print(f'Client Says: {data}')
            conn.sendall(b"You're welcome")
            conn.close()