# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:40:23 2020

@author: Rameez
"""


from command_client import primary_controller
from authentication import authenticator
# from flask import Flask, render_template, redirect, url_for, request

# app = Flask(__name__)

# @app.route('/')
# def main():
#     return render_template("welcomepage.html")

# @app.route('/home')
# def home():
#     return "HELLO"

# @app.route('/loginpage', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('loginpage.html', error=error)
    
if __name__ == '__main__':
    auth = authenticator()
    cont = primary_controller()
    
    username = input("Username: ")
    auth.authentication_controller(username)
    
    
    host = "192.168.86.44" #define the remote host that you are connecting to
    port = 5133 #define the port on the remote host
    
    cont.start_client(host, port)