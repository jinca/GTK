from gi.repository import Gtk

window = Gtk.Window()
window.set_title("My first GTK Window")
window.connect("destroy", Gtk.main_quit)
window.show()
Gtk.main()
