#!/usr/bin/env python3
from server import Server
from gui import GUI
import _thread

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
