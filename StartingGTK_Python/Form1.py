import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FormSchool(Gtk.Window):
 
    def __init__(self):
        Gtk.Window.__init__(self, title="School Placement")
        self.set_border_width(15)
        
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=5 )
        label = Gtk.Label("Nombre Completo")
        label2 = Gtk.Label(" ")
        label3 = Gtk.Label(" ")
        entry = Gtk.Entry()
        button = Gtk.Button("Send")
        school_store = Gtk.ListStore(int, str)
        school_store.append([1,"Maths School"])
        school_store.append([2,"Physics School"])
        school_store.append([3,"Computer Science School"])
        school_store.append([4,"Economics School"])

        school_combo = Gtk.ComboBox.new_with_model_and_entry(school_store)
        school_combo.set_entry_text_column(1)
        self.add(box)
     
        box.pack_start(label, False, True, 0)
        box.pack_start(entry, False, True, 0)
        box.pack_start(school_combo, False, True, 0)
        box.pack_start(button, False, True, 0)
        box.pack_start(label2, False, True, 0)

        button.connect("clicked", self.on_clicked, entry, label2, school_combo) 
        
    def on_clicked(self, button ,entry, label, combo):
        text = entry.get_text()
        tree_iter = combo.get_active_iter()
        model = combo.get_model()
        text2 = model[tree_iter][1:]
        label.set_text(text + " belongs to the "+ " %s" %(text2))
        entry.set_text(" ")
        combo.set_entry_text_column(1)

def main():
    window = FormSchool()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
