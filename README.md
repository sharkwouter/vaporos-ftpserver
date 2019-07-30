# VaporOS-FTPServer

A simple to use ftp server for VaporOS. It starts and ftp server with a random password and displays how to connect to on screen.

![](https://github.com/sharkwouter/steamos-ftpserver/raw/master/screenshot.png)

## Installation

Install the following packages:

- python
- python-pygame
- python-pyftpdlib
- fonts-dejavu-core

The application can be started by running: 

``./vaporos-ftpserver``

## Installation with venv

Before installation the following tools will need to be installed:

- python3
- git

This program can be installed by performing the following steps on the commandline:

- ``git clone https://github.com/sharkwouter/steamos-ftpserver.git``
- ``cd steamos-ftpserver``
- ``python3 -m venv venv``
- ``source venv/bin/activate``
- ``pip install -r requirements.txt``

Now the application can be started with:
 
 ``./vaporos-ftpserver``

Starting the application again in the future will require the following commands:

- ``cd steamos-ftpserver``
- ``source venv/bin/activate``
- ``./vaporos-ftpserver``

## Future plans

Future plans for this application include the following:

- Improve this readme for SteamOS (It was created on Debian Buster and requires further testing on SteamOS)
- Package SteamOS-FTPServer for SteamOS
