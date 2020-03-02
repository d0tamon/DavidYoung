# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:45:44 2019

@author: SahilPatil
"""
#Import Libraries
from getpass import getpass as GP
from cryptography.fernet import Fernet
import os

#Create Credential Variables
credential = {'username': None,
              'password':None}
#Input Username
credential['username'] = input("Enter your username: ")

#Input Password
password = GP("Enter your password: ")

#Encode Password
password_byte = password.encode('utf-8')

#Generate Key and Token
key = Fernet.generate_key()
cipher = Fernet(key)
token = cipher.encrypt(password_byte)


#Change Directory of where to save the password files
os.chdir(r"C:\Users\Username\Desktop\Python Files\Passwords")
with open("key.txt", "wb") as file:
    file.write(key)

with open("password.txt", "wb") as file:
    file.write(token)

with open("password.txt","rb") as file:
    token1 = file.read()
    
credential['password'] = cipher.decrypt(token1).decode('utf-8')

MyPassword = credential['password']
