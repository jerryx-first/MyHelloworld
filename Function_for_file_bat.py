#coding : utf-8

import os,sys


def get_file_name(file_dir):# change file name function   
    list_file_name=list()
    for filename in os.listdir(file_dir):
        list_file_name.append(os.path.join(file_dir,filename))
    return list_file_name

def change_file_suffix(file_dir,file_suffix): # change file suffix  function
    os.chdir(file_dir)
    filenamelist=os.listdir(file_dir)
    for filename in filenamelist:
        os.rename(filename,os.path.splitext(filename)[0]+"."+file_suffix)

#testing code behind


file_dir="K:\\test"
file_suffix="pcap"

change_file_suffix(file_dir,file_suffix)




