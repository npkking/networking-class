from socket import create_connection
from ssl import SSLContext, PROTOCOL_TLS_CLIENT
host='Kay'
ip= '127.0.0.1'
port = 8443
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')
with create_connection((ip, port)) as client:
    with context.wrap_socket(client, server_hostname=host) as tls:
        print(f'Using {tls.version()}\n')
        tls.sendall(b'Hello, world')
        data = tls.recv(1024)
        print(f'Server says: {data}')
