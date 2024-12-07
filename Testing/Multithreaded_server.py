import socket
import threading

print_lock = threading.Lock()  # global lock

def threaded(c):  # thread func with client socket c
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            print_lock.release()  # release lock on exit
            break
        # reverse and send back the string from client
        data = data[::-1]
        c.send(data)
    
    c.close()  # close connection

def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        t = threading.Thread(target=threaded, args=(c,))
        t.start()

if __name__ == '__main__':
    Main()