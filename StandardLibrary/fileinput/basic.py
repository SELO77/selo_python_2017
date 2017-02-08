import fileinput
import os

print(os.getcwd())


print("Text to search for:")
textToSearch = input( "> " )

print ("Text to replace it with:")
textToReplace = input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
print(fileToSearch)


with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    print(file.filename())
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')