import socket
import sys
import argparse
from datetime import datetime
from typing import Union

def try_sockets(target: str, port_begin: int, port_end: int) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.timeout(1)

    current_time = datetime.datetime.now()
    print("Port scan started at ", current_time.time())

    for port in range(port_begin, port_end+1):
        try:
            sock.connect((target, port))
            sock.close()
            print(f"Port {port} is open.")
        except (socket.error, socket.timeout):
            print(f"Port {port} is closed.")

target = input("Enter target IP address or domain: ")
port_begin = input("Enter start port: ")
port_end = input("Enter end port: ")

try_sockets(target, port_begin, port_end)
