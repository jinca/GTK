import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()

window.set_title("Welcome to APISTRAT")
window.set_default_size(400,600)

window.connect("destroy",Gtk.main_quit)
window.show()

Gtk.main()
