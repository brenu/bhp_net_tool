import sys
import socket
import getopt
import threading
import subprocess

# Defining global variables
listen = false
command = false
upload = false
execute = ""
target = ""
upload_destination = ""
port = 0