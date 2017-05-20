#
# fileTraverser.py
#
# Charles Kenney
# © 2017
#

import os

def main() :
    print('please enter a valid directory and file extension to iterate over.\n')
    ext = input('file extension: ')
    directory = input('directory: ')
    iterateOverFiles(ext, directory)

# takes a file extension and a directory
def iterateOverFiles(ext, directory) :
    for filename in os.listdir(directory) :
        if filename.endswith(ext) :
            openFile(directory, filename)
            # wait for user to respond
            while True :
                response = input('enter anything to continue... ')
                if not response :
                    continue
                else :
                    break
            continue

# open file in default program
def openFile(directory, filename) :
    fullpath = directory
    if directory.endswith('/') == False :
        fullpath += '/'
    fullpath += filename
    print("[+] opening file at path: {}".format(fullpath))
    os.system("open " + fullpath)


# Runtime
main()
