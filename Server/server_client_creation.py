import sys
import socket
import time


class tcp_wrapper():
    
    def __init__(self):
        pass
    
    def create_tcp_server(self, host, port):
        server_socket = socket.socket()
        
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        server_socket.bind((host, port))
        
        return server_socket
    
    def tcp_send_string(self, host, port, string):
        client_socket = socket.socket()
    
        client_socket.connect((host, port))
    
        client_socket.send(string)
    
        client_socket.close()
    
    def tcp_recv_file(self, active_conn, filename):
        loop_control = True
    
        try:
            with open(filename, 'wb') as f:
    
                active_conn.send("success".encode())
    
                while loop_control:
                    print("loop starting")
                    data = active_conn.recv(1024)
    
                    print("Data: ", data.decode())
    
                    if data.decode() == "EOF":
                        print("HI")
                        loop_control = False
                    
                    else:
                        f.write(data)
    
                    print("loop ending")
    
            f.close()
    
            return "Success"
        except Exception as e:
            time.sleep(1)
            active_conn.send("error".encode())
    
            return "Error"
    
    def tcp_send_file(self, active_conn, filename):
        f = open(filename,'rb')
        l = f.read(1024)
    
        while(l):
            print("loop start")
            active_conn.send(l)
            l = f.read(1024)
            print("loop end")
        
        f.close()
        active_conn.send("EOF".encode())
    
        time.sleep(2)
