#include <gtk/gtk.h>

static void on_entry_activate (GtkEntry *entry, GtkLabel *label)
{
    gtk_label_set_text (GTK_LABEL (label), gtk_entry_get_text (GTK_ENTRY (entry)));
}

int main (int argc, char *argv[])
{
    GtkWidget *window, *entry, *label, *box;

    gtk_init (&argc, &argv);

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 300, 200);
    gtk_window_set_title (GTK_WINDOW (window), "Linux Foundation");
    gtk_container_set_border_width (GTK_CONTAINER (window), 50);

    entry = gtk_entry_new ();
    gtk_entry_set_activates_default (GTK_ENTRY(entry), TRUE);
    label = gtk_label_new ("Enter a message and press <ENTER> ...");

    box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 6);
    gtk_box_pack_start (GTK_BOX (box), label, TRUE, TRUE, 0);
    gtk_box_pack_start (GTK_BOX (box), entry, TRUE, TRUE, 0);
    gtk_container_add (GTK_CONTAINER (window), box);

    g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);
    g_signal_connect (G_OBJECT (entry), "activate", G_CALLBACK (on_entry_activate), label);

    gtk_widget_show_all (window);
    gtk_main ();
    return 0;
}
