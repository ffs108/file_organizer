'''
Francisco Figueroa
7/2/2022
'''

import os
import shutil


def drive_loc(parent, drive):
    dest = ""
    if drive == 'n':
        dest = parent
    else:
        dest = "D:"
    return dest


def file_move(path, files, dest):
    for file in files:
        filename, extension = os.path.splitext(file)
        #print(extension)
        extension = extension[1:]
        #makes new folder if folder not existing
        if not os.path.exists(dest + '/' + extension):
            os.makedirs(dest + '/' + extension)
        shutil.move(src=path + '/' + file, dst=dest + '/' + extension + '/' + file)

def main():
    path = r"C:\Users\User\Downloads" #can be changed
    files = os.listdir(path)
    parent = os.path.abspath(os.path.join(path, '..'))
    drive = input("Move to D:\\? {y/n} ")
    dest = drive_loc(parent, drive)
    file_move(path, files, dest)
    print("Done.")

main()
