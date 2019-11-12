# list1.py
import os

def list_cwd():
    return os.listdir(os.getcwd())

def files_cwd():
    return [p for p in list_cwd() if os.path.isfile(p)]

def folders_cwd():
    return [p for p in list_cwd() if os.path.isdir(p)]

def size_in_bytes(fname):
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total
