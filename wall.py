#!/usr/bin/python

# Delete Wallpaper. By Anjan Momi. 
# {simple python script to show and/or delete current wallpaper}
# Copyright (C) {2014}  {Anjandev Momi}
# Contact me at anjan@momi.ca

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys
import subprocess

def main():
    playlist = "~/.fehbg"
    playlist = os.path.expanduser(playlist)
    
    with open(playlist) as fin:
        feh = fin.readlines()    
    
    feh = [elem.strip().split('\'') for elem in feh]
    
    wallpapers = []

    for lists in feh:
        for walls in lists:
            wallpapers.append(walls)

    wallpapers.pop(0)
    wallpapers.pop(0) 

    #pop out spaces in list
    while(' ' in wallpapers):
        wallpapers.remove(' ') 

    screen = int(input("On what screen is the wallpaper you wish to remove? "))
    
    if screen == 0:
        print("I think you mean screen 1")

    elif screen == 1 :
        p = subprocess.Popen(["/bin/feh", wallpapers[0]])
        returncode = p.wait()
        ask_and_delete(wallpapers[0])

    else:
        # move user entered number one over since zero indexed
        screen = screen - 1
        p = subprocess.Popen(["/bin/feh", wallpapers[screen]])
        returncode = p.wait()
        ask_and_delete(wallpapers[screen])

def ask_and_delete(wall):
    delete = input("was that the wallpaper you wanted to delete? [yes/no] ")
    
    if delete == "yes":
        os.remove(wall)
    elif delete == "no":
        wrongscreen = input("Wrong screen? Yes to select again. No to quit. [yes/no] ")
        if wrongscreen == "yes":
            main()
        elif wrongscreen == "no":
            sys.exit(0) 
        else:
         print("Please choose yes or no ")   

    else:
        print("Please choose yes or no ")

if __name__=="__main__":
    main()
