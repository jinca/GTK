import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_entry_activated(entry, label):
    text = entry.get_text()  
    label.set_text(text)  
    entry.set_text('')  

window = Gtk.Window()
window.set_title('Welcome to APISTRAT')
window.set_border_width(10)
window.connect('delete-event', Gtk.main_quit)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

label = Gtk.Label('Enter a message and press <ENTER>...')

entry = Gtk.Entry()
entry.connect('activate', on_entry_activated, label)  

box.pack_start(entry, True, True, 0)
box.pack_start(label, True, True, 0)

window.add(box)
window.show_all()
Gtk.main()
