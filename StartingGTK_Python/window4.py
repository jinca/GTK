#! /usr/bin/env python3

import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def on_button_clicked(button):
    print("Welcome to APISTRAT")


def on_destroy(window):
    Gtk.main_quit()


def main():
    window = Gtk.Window()
    window.set_title("Linux Foundation")
    window.set_default_size(400, 600)
    window.connect("destroy", on_destroy)

    button = Gtk.Button("Click me")
    button.connect("clicked", on_button_clicked)
    window.add(button)

    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
