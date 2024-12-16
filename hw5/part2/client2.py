from socket import *
from ssl import SSLContext, PROTOCOL_TLS_CLIENT


host = "Kay"
server_ip = '127.0.0.1'
server_port = 3000
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations("hw5/part2/sth.pem")

with create_connection((server_ip, server_port)) as client:
    with context.wrap_socket(client, server_hostname=host) as tls:
        while True:
            prefix = input("Please type down the arithmetic expression with space in prefix form: ")
            tls.sendall(prefix.encode("utf-8"))
            receive = tls.recv(1024).decode("utf-8")

            if receive.lower() == "closed":
                print("Closing connection with the server from now!")
                break

            print(f"The evaluation result responsed from the prefix: {prefix} is {receive}")
            print()



client.close()