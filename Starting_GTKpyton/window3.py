import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
button = Gtk.Button("Click me")

window.set_title("Welcome to APISTRAT")
window.set_default_size(400,600)

window.connect("destroy",Gtk.main_quit)
window.add(button)
window.show_all()

Gtk.main()
