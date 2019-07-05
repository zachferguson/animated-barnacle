# https://towardsdatascience.com/10-python-file-system-methods-you-should-know-799f90ef13c2
# https://pythonprogramming.net/ftp-transfers-python-ftplib/
import os
import pathlib
from os import path

def updater(directory, spacing):
    os.chdir(directory)
    contents = os.listdir(directory)
    print("updater called for: ")
    print(contents)
    for item in contents:
        item = item.rstrip()
        #itempath = pathlib.Path.cwd().joinpath(item)
        itempath = os.path.join(pathlib.Path.cwd(), item)
        print(f"{item} is a directory: {os.path.isdir(itempath)}")
        print(itempath)
        print(" ")
        if not path.isdir(itempath):
            print(spacing * " " + item + " is a file")
        else:
            print(spacing * " " + f"_______new_directory: {item}_______")
            updater(itempath, spacing + 2)
            #print(itempath)
            #print(os.listdir(itempath))
            print(spacing * " " + f"_______end_directory: {item}_______") 
            

outer_contents = pathlib.Path.cwd()
#outer_contents = pathlib.Path.cwd().joinpath("atest")
updater(outer_contents, 0)
