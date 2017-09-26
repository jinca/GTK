from gi.repository import Gtk

window = Gtk.Window()
scrolled = Gtk.ScrolledWindow()
window.add(scrolled)
window.connect("destroy",Gtk.main_quit)
scrolled.show()

Gtk.main()
