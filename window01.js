#!/usr/bin/gjs

const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

Gtk.init(null);

const LanguageWindow = Lang.Class({
    Name: "LanguageWindow",
    Extends: Gtk.Window,

    _init: function() {
        this.parent({title: "Language Selector"});
        this.border_width = 10;

        let vbox = new Gtk.Box({orientation: Gtk.Orientation.VERTICAL, spacing: 6});
        this.add(vbox);

        let label = new Gtk.Label();
        label.set_label("Languages");
	label.set_halign(Gtk.Align.START);
	vbox.add(label);

	let checkbutton1 = new Gtk.CheckButton({label: "Java"});
	checkbutton1.set_halign(Gtk.Align.START);
	vbox.add(checkbutton1);


	let checkbutton2 = new Gtk.CheckButton({label: "C"});
	checkbutton2.set_halign(Gtk.Align.END);
	vbox.add(checkbutton2);

	let checkbutton3 = new Gtk.CheckButton({label: "Python"});
	checkbutton3.set_halign(Gtk.Align.START);
	vbox.add(checkbutton3);

	let checkbutton4 = new Gtk.CheckButton({label: "Java Script"});
	checkbutton4.set_halign(Gtk.Align.END);
	vbox.add(checkbutton4);
	    
	let button1 = new Gtk.Button({label:"Quit"});
	button1.set_halign(Gtk.Align.START);
	vbox.add(button1);

	let button2 = new Gtk.Button({label:"Learn"});
	button2.set_halign(Gtk.Align.END);
	vbox.add(button2);
    }
});

let win = new LanguageWindow();
win.connect("delete-event", Gtk.main_quit);
win.show_all();
Gtk.main();
