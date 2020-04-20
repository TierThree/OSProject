import sys
import socket
from server_client_creation import tcp_wrapper

#parses commands
#parameter parsed_command_line: command that was ran
#parameter active_s: socket object

class comm_parser():
    def __init__(self):
        pass
    
    def command_parsing(self, parsed_command_line, active_s):
        wrapper = tcp_wrapper()
        
        if("download" in str(parsed_command_line.lower())):
            filename = str(parsed_command_line).split(" ")[1]
            print("Passing it along")
            wrapper.tcp_recv_file(active_s, filename) 
         
        elif("upload" in str(parsed_command_line.lower())):
            filename = str(parsed_command_line).split(" ")[2]
            
            errorOrContinue = active_s.recv(1024)
            if "error" in errorOrContinue.decode():
                print("Error")
            
            else:
                wrapper.tcp_send_file(active_s, filename)

