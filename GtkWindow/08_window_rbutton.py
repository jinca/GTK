from gi.repository import Gtk

window = Gtk.Window()
rbutton = Gtk.RadioButton("My first radio button")

window.add(rbutton)
window.connect("destroy",Gtk.main_quit)
window.show_all()

Gtk.main()
