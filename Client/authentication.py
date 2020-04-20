from Crypto.Cipher import AES
from random import randint
import getpass
import socket
import hashlib
import ldap 
import sys


class authenticator:
    
    def __init__(self):
        pass
    
    def _prompt_pass(self, username):
        password = str(getpass.getpass(prompt='Password: '))
        return (username, password)
        
    def _encrypt_data(self, user_pass_tuple):
        encryption_key = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
        user_pass_combo = user_pass_tuple[0] + user_pass_tuple[1]
        string_encryption = encryption_key.encrypt(str(user_pass_combo))
        return string_encryption
        
    def authentication_controller(self, username): 
        ldap_server = "ldap://192.168.86.44"
        user_pass_tuple = self._prompt_pass(username)
        password = user_pass_tuple[1]
        
        user_dn = "cn="+username+",dc=osproject,dc=com"
       # base_dn = "dc=osproject,dc=com"
        
        connect = ldap.initialize('ldap://192.168.86.44')
        connect.protocol_version = 3
        connect.set_option(ldap.OPT_REFERRALS, 0)
       # search_filter = "uid="+username
        try:
            connect.simple_bind_s(user_dn, password)
            print("worky")
        except:
            sys.exit("Invalid Credentials")
            
        #result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
        #connect.unbind_s()

        #Authentication:
        #Authenticate users - done
        #Admin control panel
            #Create users in ldap and locally
            #Delete users in ldap and locally
        #Change passwords

        
#        user_pass_tuple = self._prompt_pass(username)
#        encrypted_string = self._encrypt_data(user_pass_tuple)
#        
#        print(user_pass_tuple)
#        print(encrypted_string)
#        
#        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        server_addr = ("192.168.86.44", 10000)
#        sock.sendto(str(encrypted_string).encode(), server_addr)        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def _generate_random_key(self):
    #     range_start = 10**(16-1)
    #     range_end = (10**16)-1
    #     return str(randint(range_start, range_end))
    
    # def _encrypt(self, random_key):
    #     password_encryption_key = AES.new(random_key, AES.MODE_CFB, "This is an IV456")
    #     input_password = password_encryption_key.encrypt(getpass.getpass(prompt="Password: "))
        
    #     return input_password
    
    # def _decrypt(self, random_key, input_pass):
    #     password_decryption_key = AES.new(random_key, AES.MODE_CFB, "This is an IV456")
    #     password_pre_hash = password_decryption_key.decrypt(input_pass)
    
    #     return password_pre_hash
    
    # def _hash_pass(password):
    #     return password
    
    # def authentication_controller(self):
    #     random_key = self._generate_random_key()
    #     username = input("Username: ")
        
    #     password = self._encrypt(random_key)
    #     pre_hash_pass = self._decrypt(random_key, password)
    #     hashed_pass = self._hash_pass(pre_hash_pass)
        
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     server_addr = ("192.168.86.44", 10000)
    #     sock.sendto(str(hashed_pass).encode(), server_addr)
    
# authentication_controller()

# encrypt(generate_random_key())

# print(encrypt_decrypt("random_key"))

# password_encryption_key("This is a key123", AES.MODE_CFB, "This is an IV456")
# input_password = password_encryption_key.encrypt(input("Password: "))

# password_decryption_key("This is a key123", AES.MODE_CFB, "This is an IV456")
# password_pre_hash = password_decryption_key.decrypt(input_password)