#!/usr/bin/python

import os
import sys
import subprocess

def main():
    playlist = "/home/anjan/.fehbg"
    playlist = os.path.expanduser(playlist)
    
    with open(playlist) as fin:
        feh = fin.readlines()    
    
    feh = [elem.strip().split('\'') for elem in feh]
    
    wallpapers = []

    for lists in feh:
        for walls in lists:
            wallpapers.append(walls)

    wallpapers.pop(0) 
            
    screen = int(input("On what screen is the wallpaper you wish to remove?"))
    
    if screen == 1 :
        p = subprocess.Popen(["/bin/feh", wallpapers[0]])
        returncode = p.wait()
        ask_and_delete(wallpapers[0])

    else:
        p = subprocess.Popen(["/bin/feh", wallpapers[screen]])
        returncode = p.wait()
        ask_and_delete(wallpapers[screen])

def ask_and_delete(wall):
    delete = input("was that the wallpaper you wanted to delete? [yes/no]")
    
    if delete == "yes":
        os.remove(wall)
    elif delete == "no":
        wrongscreen = input("Wrong screen? Yes to select again. No to quit. [yes/no]")
        if wrongscreen == "yes":
            main()
        elif wrongscreen == "no":
            sys.exit(0) 
        else:
         print("Please choose yes or no")   
    else:
        print("Please choose yes or no")

if __name__=="__main__":
    main()
