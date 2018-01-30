import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class ListSchool(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Students of the School")
        self.set_border_width(15)
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing =5)

        self.add(box_outer)

        nom_label = Gtk.Label("Nombre Completo")
        nom_entry = Gtk.Entry()

        box_outer.pack_start(nom_label,True, True, 0)
        box_outer.pack_start(nom_entry, True, True, 0)

def main():
    window = ListSchool()
    window.connect("destroy", Gtk.main_quit)

    window.show_all()

if __name__ == "__main__":
    main()
