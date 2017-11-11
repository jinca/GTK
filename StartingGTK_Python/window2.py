#! /usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def main():
    window = Gtk.Window()
    window.set_title("Linux Foundation")
    window.set_default_size(400, 600)
    window.connect("destroy", Gtk.main_quit)
    
    window.show_all()
    Gtk.main()
    

if __name__ == "__main__":
    main()
