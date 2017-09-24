from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy",Gtk.main_quit)
window.show()
Gtk.main()
