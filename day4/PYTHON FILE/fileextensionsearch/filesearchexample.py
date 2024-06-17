# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:07:09 2024

@author: UD SYSTEMS
"""


from FileExtensionNotFoundException import FileExtensionNotFoundException
from DirectoryNotFoundException import DirectoryNotFoundException
import os
'''
    Write a Python Program to display the complete file name with 
    extension.
    input -- file name extension and name of the directory
    output --  all filenames with user given extension

'''
directoryName = input("Enter the name of the directory : ")
fileExtensionName= input("Enter the name of the file extension which you are looking ")

#Search the directory in your system
#If given directory doesn't exists throw a custom exception DirectoryNotFoundException
#If file extension doesn't exists throw a custom exception FileExtensionNotFoundException
#If directory and file extension exists then display the list of filename with extension

#fo=open("D:/",'r')
#fo.read

try:
    isFilePresent=False
    files=list()
    dirContent=os.listdir(directoryName)

    print("****************************************************")
    for file in dirContent:
            if(file.endswith(fileExtensionName)):
                isFilePresent=True
                files.append(file)
   
    if(isFilePresent):
        print(files)
        print('Files found')
    else:
      raise FileExtensionNotFoundException('Directory '+directoryName+' doesn\'t contains  file with extension ' + fileExtensionName)
except FileNotFoundError as fnfe:
    print(fnfe)
except FileExtensionNotFoundException as fenfe:
    print(fenfe)