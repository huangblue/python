# list.py
import os
def list_py(path = None):
    if path == None:
        path = os.getcwd()
    return [fname for fname in os.listdir(path) if os.path.isfile(fname) if fname.endswith('.py') if os.stat(fname).st_size>500]
