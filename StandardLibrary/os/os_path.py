import os
import sys

pwd = sys.modules['__main__'].__file__
print(pwd)

filename = os.path.dirname(pwd)
print(filename)
print(pwd.replace(filename+'/', ''))

# os.path.abspath(sys.modules)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR', BASE_DIR)
print(os.path.abspath(__file__))
print(__file__)


name = 'oops.txt'
with open(name, 'wt') as f:
    print('What?', file=f)

print(os.path.exists(name), os.path.isfile(name), os.path.isdir(name))