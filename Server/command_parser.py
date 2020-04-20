import sys
import socket
import time
import os
import subprocess
from server_client_creation import tcp_wrapper

class comm_parser():
    
    def __init__(self):
        pass

    def command_parse(self, parsed_command_line, active_conn, active_s):
        wrapper = tcp_wrapper()

        if(parsed_command_line == "QUIT"):
            print("Exiting...")
     
            active_conn.close()
     
            active_s.close()
     
            sys.exit() 
     
        elif("upload" in str(parsed_command_line.lower())):
            filename = str(parsed_command_line).split(" ")[1]
     
            try:
                if(wrapper.tcp_recv_file(active_conn, filename) != "Success"):
                    active_conn.send("Error".encode())
                else:
                    active_conn.send("Success".encode())
            except Exception as e:
                active_conn.send(str(e).encode())
     
        elif("download" in str(parsed_command_line.lower())):
            filename = str(parsed_command_line).split(" ")[1]
     
            try:
                wrapper.tcp_send_file(active_conn, filename)
                active_conn.send("Success".encode())
            except Exception as e:
                active_conn.send(str(e).encode())
     
        elif("delete" in str(parsed_command_line.lower())):
            filename = str(parsed_command_line).split(" ")[1]
     
            try:
                command = "rm " + filename
                subprocess.check_output([command])
                time.sleep(2)
                active_conn.send("Success".encode())
            except Exception as e:
                time.sleep(2)
                active_conn.send(str(e).encode())
                print(e)
     
        elif("ls" in str(parsed_command_line.lower())):
            filepath = str(parsed_command_line).split(" ")[1]
     
            try:
               output = subprocess.check_output(["ls", "-l", filepath])
               time.sleep(2)
               output_real = str(output) + "\nSuccess"
               active_conn.send(output_real.encode())
            except Exception as e:
               time.sleep(2)
               active_conn.send(str(e).encode())
     
        else:
            print("Error, command not recognized")
     
            active_conn.close()


