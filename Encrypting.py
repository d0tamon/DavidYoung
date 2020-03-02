# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:45:44 2019

@author: SahilPatil
"""
from getpass import getpass as GP
from cryptography.fernet import Fernet
import os

credential = {'username': None,
              'password':None}

credential['username'] = input("Enter your username: ")
password = GP("Enter your password: ")

password_byte = password.encode('utf-8')
key = Fernet.generate_key()
cipher = Fernet(key)
token = cipher.encrypt(password_byte)



os.chdir(r"C:\Users\Username\Desktop\Python Files\Passwords")
with open("key.txt", "wb") as file:
    file.write(key)

with open("password.txt", "wb") as file:
    file.write(token)

with open("password.txt","rb") as file:
    token1 = file.read()
    
credential['password'] = cipher.decrypt(token1).decode('utf-8')

MyPassword = credential['password']
