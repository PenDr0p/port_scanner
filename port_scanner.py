import socket
import sys
import argparse
from datetime import datetime
from typing import Union

"""
This is a simple port scanner. When you run this it will ask you for an IP
address or a domain name to target. Then it'll ask for a range of porst you want to scane.
As it runs it will list out which ports are opne and which are closed along with
minimal error messages to tell you why it might be closed.
"""


def try_ports(target: str, port_begin: int, port_end: int) -> None:
    #print current time for scan
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Port scan started at ", current_time)

    #try to get hostname
    try:
        host = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return  #exit early if resolution fails

    #if it can find the host then begin scanning the ports
    for port in range(port_begin, port_end + 1):
        try:
            #establish a socket and try to connect
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  
                result = sock.connect_ex((host, port))
                
                #if it could connect with no errors then print its open, else print it's closed
                if result == 0:
                    print(f"Port {port} is open.")
                else:
                    print(f"Port {port} is closed.")
        #print if there was an error or timeout
        except (socket.error, socket.timeout):
            print(f"Port {port} is closed (timeout or unreachable).")

#get user input
target = input("Enter target IP address or domain: ")
port_begin = int(input("Enter start port: "))
port_end = int(input("Enter end port: "))

try_ports(target, port_begin, port_end)
