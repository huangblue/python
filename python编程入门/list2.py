import os
def cwd_size_in_bytes2(): 
    return sum(size_in_bytes(f) for f in files_cwd())
def size_in_bytes(fname):
    return os.stat(fname).st_size
def files_cwd():
    return [p for p in list_cwd() if os.path.isfile(p)]
def list_cwd():
    return os.listdir(os.getcwd())
