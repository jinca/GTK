from gi.repository import Gtk

window = Gtk.Window()
label = Gtk.Label("Hello World!")

window.add(label)
window.connect("destroy",Gtk.main_quit)
window.show_all()

Gtk.main()

