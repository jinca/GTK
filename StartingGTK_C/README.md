To install on Fedora:

`sudo dnf install libgtk-3-dev`

In case more dependences are needed

sudo dnf install gtk3-devel gstreamer-devel clutter-devel libgda-devel gobject-introspection-devel

In case you have not installed any development tool

sudo dnf install @c-development @development-tools gnome-common pygobject2 dbus-python redhat-rpm-config perl-Text-CSV

To install on Ubuntu:

`sudo apt-get install build-essential libgtk-3-dev`

To compile:
 
`gcc $(pkg-config --cflags gtk+-3.0) -o window window.c $(pkg-config --libs gtk+-3.0)`

To compile with WebKit

`gcc $(pkg-config --cflags gtk+-3.0) $(pkg-config --cflags webkitgtk-3.0) -o grid01 grid01.c $(pkg-config --libs gtk+-3.0) $(pkg-config --libs webkitgtk-3.0)`

To run:

`./window`

