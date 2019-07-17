import socket
import string
import random
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class Server:

    def __init__(self, port=2020):
        self.ip = self.__get_ip()
        self.port = port
        self.username = os.getlogin()
        self.password = self.__generate_password()
        self.__setup()

    def run(self):
        print("Starting server with address:")
        print(self.get_url())
        self.server.serve_forever()

    def get_url(self):
        return "ftp://{}:{}@{}:{}/".format(self.username, self.password, self.ip, self.port)

    def __generate_password(self, length=10):
        characters = string.ascii_lowercase
        password = ""
        for char in range(length):
            password += random.choice(characters)
        return password

    def __get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("steampowered.com", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def __setup(self):
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.username, self.password, os.environ['HOME'], perm="elradfmw")

        handler = FTPHandler
        handler.authorizer = authorizer

        self.server = FTPServer((self.ip, self.port), handler)
