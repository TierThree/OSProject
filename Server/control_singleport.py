import socket
import time
import sys
import os
from command_parser import comm_parser
from server_client_creation import tcp_wrapper


class primary_controller():
    
    def __init__(self, gid, uid):
        os.setgid(1001)
        os.setuid(1001)
    
    def start_control(self, host, port):
        wrapper = tcp_wrapper()
        command_parsing = comm_parser()
        
        s = wrapper.create_tcp_server(host, port)
        s.listen(10)
        
        conn, addr = s.accept()
        print("conn established")
        
        
        while True:
           #conn, addr = s.accept() 
           #print("Connection accepted, awaiting command...")
        
           print("COMMAND WAIT")
           command_line = conn.recv(4096)
           parsed_command_line = str(repr(command_line))[2:-1]
           print("Formatted command: ", parsed_command_line)
        
           command_parsing.command_parse(parsed_command_line, conn, s)
           print("FINISHED PARSED")
