#include <gtk/gtk.h>

static void button_clicked (GtkWidget* widget, gpointer data)
{
    gtk_label_set_text (GTK_LABEL (data), "Welcome to APISTRAT");
}

int main (int argc, char *argv[])
{
    GtkWidget *window, *label, *button, *box;

    gtk_init (&argc, &argv);

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 400, 600);
    gtk_window_set_title (GTK_WINDOW (window), "Linux Foundation");

    label = gtk_label_new ("");
    button = gtk_button_new_with_label ("Click me");

    box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 6);
    gtk_box_pack_start (GTK_BOX (box), button, TRUE, TRUE, 0);
    gtk_box_pack_start (GTK_BOX (box), label, TRUE, TRUE, 0);
    gtk_container_add (GTK_CONTAINER (window), box);

    g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);
    g_signal_connect (button, "clicked", G_CALLBACK (button_clicked), (gpointer)label);

    gtk_widget_show_all (window);
    gtk_main ();
    return 0;
}
