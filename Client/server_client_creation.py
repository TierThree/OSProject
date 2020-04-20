import sys #import sys library
import socket #import socket library
import time #import time library

class tcp_wrapper():
    
    def __init__(self):
        pass

    #provide a wrapper to create tcp server
    #host parameter: enter IP address
    #port parameter: enter port number
    def create_tcp_server(self, host, port):
        server_socket = socket.socket()
    
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        server_socket.bind((host, port))
    
        return server_socket
    
    #provide a wrapper to send a string over tcp
    #host parameter: enter IP address
    #port parameter: enter port number
    #string parameter: enter string to transfer
    def tcp_send_string(self, host, port, string):
        client_socket = socket.socket()
    
        client_socket.connect((host, port))
    
        client_socket.send(string)
    
        client_socket.close()
    
    #provide a wrapper to recieve a file over tcp
    #socket parameter: socket object
    #filename parameter: filename to transfer
    def tcp_recv_file(self, active_conn, filename):
        
        with open(filename, 'wb') as f:
            
            loop_control = True
    
            while loop_control:
                print("loop start")
                data = active_conn.recv(1024)
    
                print(data)
    
                if data.decode() == "EOF":
                    loop_control = False
    
                else:
                    f.write(data)
    
                print("loop end")
        
        f.close()
    
    #provide a wrapper to send a file over tcp
    #socket parameter: socket object
    #filename parameter: filename to transfer
    def tcp_send_file(self, active_conn, filename):
        f = open(filename,'rb')
        l = f.read(1024)
    
        time.sleep(1)
    
        while(l):
            active_conn.send(l)
            l = f.read(1024)
    
        f.close()
        print("sending EOF")
        time.sleep(2)
        active_conn.send("EOF".encode())

