from gi.repository import Gtk

def on_entry_activated(entry, label):
    text = entry.get_text()  
    label.set_text(text)  
    entry.set_text('')  

window = Gtk.Window()
window.set_title('Welcome to APISTRAT')
window.set_border_width(10)
window.connect('delete-event', Gtk.main_quit)

layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

parrot = Gtk.Label('Enter a message and press <ENTER>...')

entry = Gtk.Entry()
entry.connect('activate', on_entry_activated, parrot)  

layout.pack_start(entry, True, True, 0)
layout.pack_start(parrot, True, True, 0)

window.add(layout)
window.show_all()
Gtk.main()
