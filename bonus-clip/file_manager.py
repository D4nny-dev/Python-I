import os,glob,time

def list_files(path,extend=''):
    files=[]
    listfiles = glob.glob(path+extend)
    for file in listfiles:
        files.append(file.split('/')[1])
    return files 
   
def count_files():
    return len(list_files("*/*.","py"))

def get_file_info(file):
       print(os.getcwd())
