from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy",Gtk.main_quit)
window.set_default_size(400,600)
window.show()

Gtk.main()
