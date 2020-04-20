# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:54:36 2020

@author: Rameez
"""

from control_singleport import primary_controller
import socket

host = "192.168.86.44"
port = 5133

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind((host, 10000))
#data, addr = sock.recvfrom(1024)
#print(data)

controller = primary_controller(1001, 1001)

controller.start_control(host, port)
