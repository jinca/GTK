from gi.repository import Gtk,Gdk

window = Gtk.Window()
window.connect("destroy",Gtk.main_quit)
window.modify_bg(Gtk.StateType.NORMAL,Gdk.Color.from_floats(1.0,0.0,0.5))
window.show()
Gtk.main()
