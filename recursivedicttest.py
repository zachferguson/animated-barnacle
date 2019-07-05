import os
import pathlib
from os import path
import json
from ftplib import FTP
from ftplib import FTP_TLS
import datetime
import re

comp_dict = {'server_files': {}, 'local_files': {}}
ignore = [".git"]


def local_parser(directory, spacing):
    if os.path.split(directory)[1] in ignore:
        return
    os.chdir(directory)  # change to directory passed in as arguement
    contents = os.listdir(directory)  # list contents of this directory

    if directory not in comp_dict['local_files'].keys():
        #comp_dict['local_files'].update({directory:{}})
        comp_dict['local_files'][directory] = {}
    
    for item in contents:  # for file or folder in current directory
        os.chdir(directory)  # change to argument directory (in case that has returned back a level from a recursive run
        itempath = str(pathlib.Path.cwd().joinpath(item))  # 
        print(spacing * " " + str(itempath))
        print(" ")
        if not path.isdir(itempath):
            print(spacing * " " + item + " is a file")
            #temp = Local_File(item, datetime.datetime.fromtimestamp(os.path.getmtime(itempath)).strftime('%Y-%m-%d %H:%M:%S'), itempath)
            temp = {'filename':str(item), 'mod':datetime.datetime.fromtimestamp(os.path.getmtime(itempath)).strftime('%Y-%m-%d %H:%M:%S'), 'filepath':itempath}
            #comp_dict['local_files'][directory].update({item:temp})
            #comp_dict['local_files'][directory].update(json.dumps(temp))
            comp_dict['local_files'][directory][item] = temp
        else:
            print(spacing * " " + item + " is a directory")
            print(spacing * " " + f"_______new_directory: {item}_______")
            local_parser(itempath, spacing + 2)
            #print(itempath)
            #print(os.listdir(itempath))
            print(spacing * " " + f"_______end_directory: {item}_______")
    

local_parser(os.getcwd(), 0)
print("******* RESULTS *******")
for entry in comp_dict['local_files']:
    print(entry)
    print(comp_dict['local_files'][entry])
    '''
    for item in entry:
        #print(json.dumps(item))
        print(item)
        #print(comp_dict['local_files'][entry][item])
        print("*******")
    '''
    print("_____________________________")
