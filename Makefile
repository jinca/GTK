PHONY: all

all:
	gcc `pkg-config --cflags gtk+-3.0` `pkg-config --cflags --libs webkitgtk-3.0` -o window grid01.c `pkg-config --libs gtk+-3.0` `pkg-config --cflags --libs webkitgtk-3.0`
