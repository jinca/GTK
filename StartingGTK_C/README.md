To install on Fedora:

$sudo apt-get install libgtk-3-dev

To install on Ubuntu:

sudo apt-get install build-essential libgtk-3-dev

To compile:
 
`gcc $(pkg-config --cflags gtk+-3.0) -o window window.c $(pkg-config --libs gtk+-3.0)`

To run:

`./window`

