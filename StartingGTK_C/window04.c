#include <gtk/gtk.h>

static void on_button_clicked (GtkWidget* widget, gpointer data)
{
    g_print ("Welcome to APISTRAT\n");
}

int main (int argc, char *argv[])
{
    GtkWidget *window, *button;

    gtk_init (&argc, &argv);

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 400, 600);
    gtk_window_set_title (GTK_WINDOW (window), "Linux Foundation");

    button = gtk_button_new_with_label ("Click me");
    gtk_container_add (GTK_CONTAINER (window), button);

    g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);
    g_signal_connect (button, "clicked", G_CALLBACK(on_button_clicked), NULL);

    gtk_widget_show_all (window);
    gtk_main ();
    return 0;
}
