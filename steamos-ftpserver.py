#!/usr/bin/env python3
import socket
import string
import random
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#Get the IP
def getIp():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  ip = s.getsockname()[0]
  s.close()
  return ip

#Generate a random password
def generatePassword(length=10):
    charList = string.ascii_lowercase
    password = ""
    for char in range(length):
         password+=random.choice(charList)
    return password

ip = getIp()
username = os.getlogin()
password = generatePassword()
port = 2020

connectstring = "ftp://{}:{}@{}:{}/".format(username, password, ip, port)
print(connectstring)

authorizer = DummyAuthorizer()
authorizer.add_user(username, password, "/home/{}".format(username), perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((ip, port), handler)
server.serve_forever()
