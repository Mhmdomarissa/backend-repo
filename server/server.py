
import os
from dotenv import load_dotenv

load_dotenv('../config.env') 

class Server:
    def __init__(self):
        self.server_ip = os.getenv('ServerIPAddress', '127.0.0.1')

    def start(self):
        print(f"Server starting at {self.server_ip}")

if __name__ == "__main__":
    server = Server()
    server.start()
