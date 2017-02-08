import os

try:
    os.mkdir('f')
except FileExistsError:
    os.removedirs('f/mock')
    os.mkdir('f')


print(os.listdir('f'))

os.mkdir('f/mock')
print(os.listdir('f'))