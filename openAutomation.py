#
# fileTraverser.py
#
# Charles Kenney
# © 2017
#

import os
import platform

def main() :
    validateSystem()
    print('Please enter a valid directory and file extension to iterate over.\n')
    while True :
        ext = input('file extension: ')
        directory = input('directory: ')
        if os.path.isdir(directory) :
            break
        else :
            print('[-] Error: Invalid directory!')
            continue
    traverseFiles(ext, directory)

# takes a file extension and a directory
def traverseFiles(ext, directory) :
    for filename in os.listdir(directory) :
        if filename.endswith(ext) :
            openFile(directory, filename)
            # wait for user to respond
            while True :
                response = input('Enter anything to continue... ')
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
    print("[+] Opening file at path: {}".format(fullpath))
    os.system("open " + fullpath)

# verifies system is on mac os
def validateSystem() :
    system = platform.platform()
    if 'darwin' not in system.lower() :
        print('system: {}'.format(system))
        print("Sorry, this script is only supported on mac!")
        exit(1)



# Runtime
main()
