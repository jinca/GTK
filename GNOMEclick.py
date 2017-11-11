import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


def on_destroy(window):
    Gtk.main_quit()


def on_Toto_button_clicked(Toto_button):
    box.add(Toto_label)


def on_Bruni_button_clicked(Bruni_button):
    box.add(Bruni_label)


def on_Sol_button_clicked(Sol_button):
    box.add(Sol_label)


def on_Martin_button_clicked(Martin_button):
    box.add(Martin_label)


def on_Julitas_button_clicked(Julitas_button):
    box.add(Julitas_label)


def main():
    window = Gtk.Window()


    frame = Gtk.Frame()
    frame.set_label("Escoge a tu persona favorita del team")

    box = Gtk.Box()


    Toto_button = Gtk.Button("Toto")
    Bruni_button = Gtk.Button("Brunis")
    Sol_button = Gtk.Button("Sol")
    Martin_button = Gtk.Button("Martincio")
    Julitas_button = Gtk.Button("Julitas")

    Toto_label = Gtk.Label("Elegiste al gran Toto")
    Bruni_label = Gtk.Label("Elegiste a Bruni Bruni")
    Sol_label = Gtk.Label("Elegiste a chica Selfie")
    Martin_label = Gtk.Label("Elegiste al master Martin")
    Julitas_label = Gtk.Label("Elegiste a Julitas :)")

    fixed = Gtk.Fixed()
    box.add(fixed)
    Toto_label.show()
    Bruni_label.show()
    Sol_label.show()
    Martin_label.show()
    Julitas_label.show()
    frame.add(box)
    window.set_default_size(400, 600)
    window.modify_bg(Gtk.StateType.NORMAL, 
                     Gdk.Color.from_floats(0.8,0.1,1.0))
    window.set_title("GNOME Peru Challenge")
    fixed.put(Toto_button, 40, 60)
    fixed.put(Bruni_button, 40, 100)
    fixed.put(Sol_button, 40, 140)
    fixed.put(Martin_button, 40, 180)
    fixed.put(Julitas_button, 40, 220)

    Toto_button.connect("clicked", on_Toto_button_clicked)
    Bruni_button.connect("clicked", on_Bruni_button_clicked)
    Sol_button.connect("clicked", on_Sol_button_clicked)
    Martin_button.connect("clicked", on_Martin_button_clicked)
    Julitas_button.connect("clicked", on_Julitas_button_clicked)

    window.add(frame)
    window.connect("destroy", on_destroy)
    window.show_all()
    Gtk.main()
    

if __name__ == '__main__':
    main()
