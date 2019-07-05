# https://towardsdatascience.com/10-python-file-system-methods-you-should-know-799f90ef13c2
# https://pythonprogramming.net/ftp-transfers-python-ftplib/
import os
import pathlib
from os import path
import json
from ftplib import FTP
from ftplib import FTP_TLS
import datetime
import re

    
#server_file_modded("-rw-r--r--    1 equipins   equipins         4801 May 21 20:50 about.html")

# WORKS _______ NEEDS UPDATED TO COMPARE _______ #
def updater(directory, spacing):
    os.chdir(directory)  # change to directory passed in as arguement
    contents = os.listdir(directory)  # list contents of this directory
    
    for item in contents:  # for file or folder in current directory
        os.chdir(directory)  # change to arguement directory (in case that has returned back a level from a recursive run
        itempath = pathlib.Path.cwd().joinpath(item)  # 
        #print(spacing * " " + f"{item} is a directory: {os.path.isdir(itempath)}")
        print(spacing * " " + str(itempath))
        print(" ")
        if not path.isdir(itempath):
            print(spacing * " " + item + " is a file")
        else:
            print(spacing * " " + item + " is a directory")
            print(spacing * " " + f"_______new_directory: {item}_______")
            updater(itempath, spacing + 2)
            #print(itempath)
            #print(os.listdir(itempath))
            print(spacing * " " + f"_______end_directory: {item}_______") 
            

def server_file_modded(ftp, file_name):
    temp = ftp.mlsd(file_name)
    for item in temp:
        print(file_name)
        mod = item[1]['modify']
        filetype = item[1]['type']
        dated = datetime.datetime(int(mod[:4]),int(mod[4:6]),int(mod[6:8]), int(mod[8:10]), int(mod[10:12]), int(mod[12:]))
        return_object = {}
        return_object['modified'] = datetime.datetime(int(mod[:4]),int(mod[4:6]),int(mod[6:8]), int(mod[8:10]), int(mod[10:12]), int(mod[12:]))
        return_object['filetype'] = filetype
        return dated

# WORKS #
def ftp_connection():
    credentials = get_credentials()
    ftp = FTP_TLS()

    ftp.connect(credentials['ftp_client'],)
    ftp.login(credentials['user'], credentials['password'],)
    server_data = []
    ftp.retrlines('LIST', server_data.append)
    for item in server_data:
        file_name = item[item.find(":")+4:]
        if path.isdir(file_name) or file_name[:1] == '.':
            continue
        else:
            modtime = server_file_modded(ftp, file_name)
            if modtime:
                print(modtime)
                print("____________________________________________")
    
    ftp.quit()
    


    
# WORKS #
def create_credentials(client_address, client_port, username, password):
    login_data = {
        'ftp_client': client_address,
        'ftp_port': client_port,
        'user': username,
        'password': password,
        }
    with open('login.txt', 'w') as login_info:
        json.dump(login_data, login_info)

# WORKS #
def get_credentials():
    with open('login.txt') as credentials:
        login_data = json.load(credentials)
        return login_data

ftp_connection()
        
