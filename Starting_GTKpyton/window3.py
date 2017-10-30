import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
label = Gtk.Label("Welcome to APISTRAT")

window.set_title("Linux Foundation")
window.set_default_size(400,600)

window.connect("destroy",Gtk.main_quit)
window.add(label)
window.show_all()

Gtk.main()
