from gi.repository import Gtk

window = Gtk.Window()
check = Gtk.CheckButton("This is a check button")

window.add(check)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
