#!/usr/bin/env python3
from server import Server
from gui import GUI
import _thread
import os

# Set the working directory
file_name = os.path.realpath(__file__)
directory_name = os.path.dirname(os.path.abspath(file_name))
os.chdir(directory_name)

# Setup the FTP server and gui
port = 2020
server = Server(2020)
gui = GUI(server)

# Run the server
try:
    _thread.start_new_thread(server.run, ())
except:
    print("Error: unable to start server thread")

# Run the GUI
gui.run()
