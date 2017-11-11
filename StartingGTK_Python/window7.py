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
    window.set_default_size(300, 200)
    window.set_border_width(50)
    window.connect("destroy", on_destroy)

    button = Gtk.Button("Click me")
    button.set_halign(Gtk.Align.START)
    button.set_valign(Gtk.Align.START)
    button.connect("clicked", on_button_clicked)

    label = Gtk.Label("")
    label.set_halign(Gtk.Align.END)
    label.set_valign(Gtk.Align.END)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    box.pack_start(button, True, True, 0)
    box.pack_start(label, True, True, 0)

    window.add(box)
    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
