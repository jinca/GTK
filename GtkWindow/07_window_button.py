from gi.repository import Gtk

window = Gtk.Window()
button = Gtk.Button("Click it!")

window.add(button)
window.connect("destroy",Gtk.main_quit)
window.show_all()
Gtk.main()
