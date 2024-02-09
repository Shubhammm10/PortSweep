#!/bin/python3

import socket
from datetime import datetime

# Define our target
target = "192.168.100.1"  # Replace "192.168.100.1" with the desired target IP address

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator - if port is open it throws a 0, otherwise 1
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Could not connect to server.")
