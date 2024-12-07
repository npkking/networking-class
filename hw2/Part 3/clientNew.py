import tkinter as tk
from socket import *

class TCPMailboxClient:
    def __init__(self, app):
        self.app = app
        self.app.title("Mailbox System") #naming the application
        self.create_widgets()


    def create_widgets(self):
        self.command_label = tk.Label(self.app, text="Enter command with targeted ID")
        self.command_label.pack()

        self.info = tk.Label(self.app, text="Command list: create, send, read, delete, destroy. Example: send 23 Hello, how are you")
        self.info.pack()

        self.command_entry = tk.Entry(self.app, width=50)
        self.command_entry.pack()

        self.send_button = tk.Button(self.app, text="Send command", command=self.send_command) # call the function
        self.send_button.pack()

        self.response_text = tk.Text(self.app, state="disabled", width=50, height=10)
        self.response_text.pack()


    def send_command(self): #each request send to the server is a connection
        command = self.command_entry.get()
        response = self.send_to_server(command)
        self.display(response)

    def send_to_server(self, command):
        with socket(AF_INET, SOCK_STREAM) as client:
            try:
                client.connect(('127.0.0.1', 8000))
                client.sendall(command.encode())
                response = client.recv(1024).decode()
                return response

            except:
                return str(Exception)
            

    def display(self,response):
        self.response_text.config(state="normal")
        self.response_text.insert(tk.END, response + "\n") #at the end
        self.response_text.config(state="disabled")

    
    def keep_reading():
        pass


root = tk.Tk()
maill = TCPMailboxClient(root)
root.mainloop()