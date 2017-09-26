from gi.repository import Gtk

window = Gtk.Window()
hb = Gtk.HeaderBar()
hb.set_show_close_button(True)
window.set_titlebar(hb)

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
