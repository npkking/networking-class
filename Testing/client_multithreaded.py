import socket

def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))    
    while True:
        # message sent to server
        message = input('Message to send: ')
        if message == 'bye':
            break
        print('Send message: %s\n' % message)
        s.send(message.encode('ascii'))

        # message received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of the sent message
        print('Received from the server:', str(data.decode('ascii')))

    # close the connection
    s.close()

if __name__ == '__main__':
    Main()