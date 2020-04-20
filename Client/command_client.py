from server_client_creation import * #import the server_client_creation python file
from command_parser import comm_parser #import the command_parser python file
import socket #import the socket library
import time #import the time library


class primary_controller():
    
    def __init__(self):
        pass
    
    def start_client(self, remote_host, remote_port):
        #Instantiation of all class objects required
        command_parse = comm_parser()
        
        command = input("$> ") #prompt the user for a command
        
        #commands:
        #upload [filename] will upload a filename
        #download [filename] will download a filename
        #delete [filename] will delete the file name
        
        s = socket.socket() #Instantiate the socket object

        
        s.connect((remote_host,remote_port)) #connect to the defined host/port combo
        s.send(command.encode()) #send the command to the server
        
        while(command != "QUIT"): #while the user doesn't enter QUIT, keep prompting for another command
            command_parse.command_parsing(command, s) #pass the command entered, along with the socket object to the command_parser
        
            message = s.recv(4096) #wait for the server's response on whether the command was successful or not
            
            print(message.decode()) #output the server's response to the console
        
            command = input("$> ") #prompt the user for another command
        
            s.send(command.encode()) #send the command to the server
            
        s.close() #after quitting, close the socket


