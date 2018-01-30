import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Language Selector")
        self.set_border_width(15)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(box_outer)

        label = Gtk.Label("Choose your  language")
        box_outer.add(label)
        #####


        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

	####

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label1 = Gtk.Label("C", xalign=0)
        link1 = Gtk.LinkButton("https://wiki.gnome.org/","Go tutorial")
        hbox.pack_start(label1, True, True, 0)
        hbox.pack_start(link1, False, True, 0)
        
        listbox.add(row)

        ####

        row= Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label2 = Gtk.Label("Python", xalign=0)
        link = Gtk.LinkButton("https://developer.gnome.org/gnome-devel-demos/stable/tutorial.py.html.en","Go tutorial")
        hbox.pack_start(label2, True, True, 0)
        hbox.pack_start(link, False, True, 0)


        listbox.add(row)

	#####
        row= Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label3 = Gtk.Label("Javascript", xalign=0)
        link3 = Gtk.LinkButton("https://developer.gnome.org/gnome-devel-demos/stable/beginner.js.html.en","Go tutorial")
        hbox.pack_start(label3, True, True, 0)
        hbox.pack_start(link3, False, True, 0)


        listbox.add(row)

        #####

        row= Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label4 = Gtk.Label("Java", xalign=0)
        link4 = Gtk.LinkButton("http://java-gnome.sourceforge.net/doc/api/4.1/overview-summary.html","Go tutorial")
        hbox.pack_start(label4, True, True, 0)
        hbox.pack_start(link4, False, True, 0)


        listbox.add(row)
     

win = ListBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
