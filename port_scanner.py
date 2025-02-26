import socket
import sys
import argparse
from datetime import datetime
from typing import Union

def try_sockets(target: str, port_begin: int, port_end: int) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Port scan started at ", current_time)
    
    #try to get hostname
    try:
        host = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return  #exit early if resolution fails

    for port in range(port_begin, port_end + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  
                result = sock.connect_ex((host, port))
                
                if result == 0:
                    print(f"Port {port} is open.")
                else:
                    print(f"Port {port} is closed.")
        except (socket.error, socket.timeout):
            print(f"Port {port} is closed (timeout or unreachable).")


target = input("Enter target IP address or domain: ")
port_begin = int(input("Enter start port: "))
port_end = int(input("Enter end port: "))

try_sockets(target, port_begin, port_end)
