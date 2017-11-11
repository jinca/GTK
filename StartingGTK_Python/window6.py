#! /usr/bin/env python3

import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def on_button_clicked(button):
    label.set_text("Welcome to APISTRAT")


def on_destroy(window):
    Gtk.main_quit()


def main():
    window = Gtk.Window()
    window.set_title("Linux Foundation")
    window.set_default_size(400, 600)
    window.connect("destroy", on_destroy)

    label = Gtk.Label("")

    button = Gtk.Button("Click me")
    button.connect("clicked",on_button_clicked)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    box.pack_start(button, True, True, 0)
    box.pack_start(label, True, True, 0)

    window.add(box)
    window.show_all()
    Gtk.main()


if__name__ == "__main__":
    main()
