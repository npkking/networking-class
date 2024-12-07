from socket import *
from collections import defaultdict


class UDPmessageServer:
    def __init__(self, host = '127.0.0.1', port = 8000):
        self.mailboxes = defaultdict(lambda: {'ownerIP': None, 'message': [], 'rev_message': []}) #list of messages and owner IP
        self.host = host
        self.port = port
        self.readMode = False
        self.current_read = None


    def start_server(self):
        with socket(AF_INET,SOCK_DGRAM) as server:
            server.bind((self.host, self.port))
            print(f"Server is listening on {self.host}:{self.port}")
            while True: #never shutdown
                data, addr = server.recvfrom(1024)
                data = data.decode()
                print(f"Server is listening to {addr[0]}:{addr[1]}")
                response = self.handle_request(data.strip(), addr)
                if response:
                    server.sendto(response.encode(), addr)


    def handle_request(self, request, client_address):
        args = request.split(' ')
        if not args:
            print("Client disconnected")
        else:
            command = args[0]
            if command == 'create':
                self.check_mode()
                return self.create_mail(args[1], client_address[0])
            elif command == 'send':
                self.check_mode()
                return self.send_mail(args[1], ' '.join(args[2:])) #concatenate the message
            elif command == 'delete':
                self.check_mode()
                return self.delete_mail(args[1], client_address[0])
            elif command == "destroy":
                self.check_mode()
                return self.destroy_mail(args[1], client_address[0])
            elif command == "read":
                self.readMode = True
                self.check_change_read_mail(args[1])
                return self.read_mail(args[1])
            else:
                return "Command unidentified"


    def check_change_read_mail(self, mbox_id):
        if mbox_id != self.current_read:
            self.recover_mail() #recover
            self.current_read = mbox_id #update


    def check_mode(self):
        if self.readMode == True:
            self.readMode = False
            self.recover_mail()


    def recover_mail(self):
        for mail in reversed(self.mailboxes[self.current_read]['rev_message']):
            self.mailboxes[self.current_read]['message'].append(mail)
        self.mailboxes[self.current_read]['rev_message'].clear()

  
    def create_mail(self, mbox_id, owner_ip):
        if self.mailboxes[mbox_id]['ownerIP'] is not None:
            return "Error: Mailbox already exists"
        else:
            self.mailboxes[mbox_id]['ownerIP'] = owner_ip
            print(f"mailbox {mbox_id} created")
            return f"Mailbox {mbox_id} created"


    def send_mail(self, mbox_id, message):
        if not self.mailboxes[mbox_id]['ownerIP']:
            return "Mail box does not exist"
        else:
            self.mailboxes[mbox_id]['message'].append(message)
            return f"Message sent to mail box {mbox_id}"


    def read_mail(self, mbox_id):
        if not self.mailboxes[mbox_id]['ownerIP']:
            return "Mail box does not exist"
        elif not self.mailboxes[mbox_id]['message']:
            return "No more mail to read"
        else:
            mes = self.mailboxes[mbox_id]['message'].pop()
            self.mailboxes[mbox_id]['rev_message'].append(mes)
            return mes


    def delete_mail(self, mbox_id, ip):
        if not self.mailboxes[mbox_id]['ownerIP']:
            return "Error: Mail box does not exist"
        elif self.mailboxes[mbox_id]['ownerIP'] != ip:
            return "Error: Unauthorized to delete message in the mail"
        elif self.mailboxes[mbox_id]['message']:
            self.mailboxes[mbox_id]['message'].pop()
            return f"Successfully deleted 1 mail from mailbox {mbox_id}"
        else:
            return "No more mail to delete"


    def destroy_mail(self, mbox_id, ip):
        if not self.mailboxes[mbox_id]['ownerIP']:
            return "Error: Mail box does not exist"
        elif self.mailboxes[mbox_id]['ownerIP'] != ip:
            return "Error: Unauthorized to delete the mailbox"
        else:
            del self.mailboxes[mbox_id]
            return f"Destroy mailbox {mbox_id}"


server = UDPmessageServer()
server.start_server()
