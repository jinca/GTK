import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Language Selector")
        self.set_border_width(15)
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
 
        self.add(box_outer)

        main_label = Gtk.Label("Choose your favorite language")
        listbox = Gtk.ListBox()

        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(main_label, False, True, 0)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Java", xalign=0)
        link = Gtk.LinkButton.new_with_label("Go to Java tutorial") 
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("C", xalign=0)
        link = Gtk.LinkButton.new_with_label("Go to C tutorial") 
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("JavaScript", xalign=0)
        link = Gtk.LinkButton.new_with_label("Go to JavaScript tutorial") 
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Python", xalign=0)
        link = Gtk.LinkButton.new_with_label("Go to Python tutorial") 
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)
        
        listbox.add(row)

def main():
    window = ListBoxWindow()
    window.connect("destroy", Gtk.main_quit)

    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
