# VaporOS-FTPServer

A simple to use ftp server for VaporOS. It starts and ftp server with a random password and displays how to connect to on screen.

![](https://github.com/sharkwouter/vaporos-ftpserver/raw/master/screenshot.png)

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

- ``git clone https://github.com/sharkwouter/vaporos-ftpserver.git``
- ``cd vaporos-ftpserver``
- ``python3 -m venv venv``
- ``source venv/bin/activate``
- ``pip install -r requirements.txt``

Now the application can be started with:
 
 ``./vaporos-ftpserver``

Starting the application again in the future will require the following commands:

- ``cd vaporos-ftpserver``
- ``source venv/bin/activate``
- ``./vaporos-ftpserver``

## Building the package for SteamOS

To build this package, the following software will need to be installed:

- build-essential
- devscripts

This program can be build by performing the following steps on the commandline:

- ``git clone https://github.com/sharkwouter/vaporos-ftpserver.git``
- ``cd vaporos-ftpserver``
- ``dch`` (This will allow you to change the changelog)
- ``dpkg-buildpackage -us -uc``

After that install with the following commands:

- ``sudo dpkg -i ../vaporos-ftpserver*.deb``
- ``sudo apt-get install -f``

## Future plans

Future plans for this application include the following:

- Ship the package with VaporOS
- Improving the GUI
