import threading
from socket import *
import numpy as np
import json
import time #slow down the system to test for concurency
from ssl import PROTOCOL_TLS_SERVER, SSLContext



address = ("127.0.0.1", 3000)
shared_dictionary = {"age" : 21, "name" : "Khanh"}

reader_count = 0
writer_active = False #mechanism for lock condition

lock = threading.Lock()
condition = threading.Condition(lock)



def handle_write(client_socket, client_address, key, value):
    global shared_dictionary

    shared_dictionary[key] = value
    client_socket.sendall(f"Wrote the {key}:{value} into the dictionary".encode())
    print(f"Writing done by {client_address[0]}:{client_address[1]}")
    time.sleep(5)


def handle_read(client_socket, client_address):
    global shared_dictionary

    data = json.dumps(shared_dictionary)    #use this json module to serialize them into json form to transfer through network
    client_socket.sendall(data.encode())

    print(f"Sent the dictionary data to client {client_address[0]}:{client_address[1]}")
    time.sleep(5)

def on_connection(client_socket, client_address):
    global reader_count, writer_active
    
    while True:
        request = client_socket.recv(1024).decode()
        request = request.split(" ")

        if request[0].lower() == "close":
            print(f"Disconecting to client {client_address[0]}:{client_address[1]}")
            break

        elif request[0].lower() == "read":
            with condition: #acquiring lock
                while writer_active:
                    condition.wait()    #wait for writer to finish, release the lock temporarily
                reader_count += 1   #release the lock after this, needing the lock in here because we try to access a global variable     
            
            handle_read(client_socket, client_address) #this makes all clients can read concurently as soon as they acquire the lock 
            
            with condition:
                reader_count -= 1   #decrease after finish reading
                if reader_count == 0:
                    condition.notify_all()  #wakes up other threads

        elif request[0].lower() == "write":
            data = request[1].split(":")
            key = data[0]
            value = data[1]

            with condition:
                while writer_active or reader_count > 0:   #in case writer mode is activated (some one is writing) or there is someone still reading
                    condition.wait()
                writer_active = True #signalize that there is writer currently writing

            handle_write(client_socket, client_address, key, value)

            with condition:
                writer_active = False #done writing
                condition.notify_all()

    client_socket.close()


def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    server.listen(5)
    print(f"Server is operating on {address[0]}:{address[1]}")
    context = SSLContext(PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="hw5/part4/sth.pem", keyfile="hw5/part4/private.key")
    tls = context.wrap_socket(server, server_side=True)
    while True:
        client_socket, client_address = tls.accept()
        print(f"Server is connecting to {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=on_connection, args=(client_socket, client_address))
        client_thread.start()



if __name__ == "__main__":
    main()
