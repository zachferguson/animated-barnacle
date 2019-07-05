import os
import pathlib
from os import path
import json
from ftplib import FTP
from ftplib import FTP_TLS
import datetime
import re

    

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


updater(os.getcwd(), 0)
