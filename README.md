#Delete Wallpaper

Simple python script to show and/or delete current wallpaper.

Requires that you have feh installed and use it to manage your wallpaper.

##Installation

clone this repo

edit wall.py and change YOURUSER in
    playlist = "/home/YOURUSER/.fehbg"

Copy to /bin directory so you can call it from wherever (optional)
    chmod +x wall.py
    sudo cp wall.py /usr/local/bin/wall
    wall
