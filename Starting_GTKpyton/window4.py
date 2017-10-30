import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

def on_button_clicked(button):
    print("Welcome to APISTRAT\n")

def on_destroy(window):
    Gtk.main_quit()

window = Gtk.Window()
button = Gtk.Button("Click me")

window.set_title("Linux Foundation")
window.set_default_size(400,600)
button.connect("clicked",on_button_clicked)
window.add(button)
window.connect("destroy",on_destroy)
window.show_all()

Gtk.main()

