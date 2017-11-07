#include <gtk/gtk.h>

static void on_button_clicked (GtkWidget* widget, gpointer data)
{
    gtk_label_set_text (GTK_LABEL (data), "Welcome to APISTRAT");
}

int main (int argc, char* argv[])
{
    GtkWidget *window, *label, *button, *box;

    gtk_init (&argc, &argv);

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 300, 200);
    gtk_window_set_title (GTK_WINDOW (window), "Linux Foundation");
    gtk_container_set_border_width (GTK_CONTAINER (window), 50);
      
    button = gtk_button_new_with_label ("Click me");
    gtk_widget_set_halign (button, GTK_ALIGN_START);
    gtk_widget_set_valign (button, GTK_ALIGN_START);
      
    label = gtk_label_new (NULL);
    gtk_widget_set_halign (label, GTK_ALIGN_END);
    gtk_widget_set_valign (label, GTK_ALIGN_END);

    box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 6);
    gtk_box_pack_start (GTK_BOX (box), button, TRUE, TRUE, 0);
    gtk_box_pack_start (GTK_BOX (box), label, TRUE, TRUE, 0);
    gtk_container_add (GTK_CONTAINER (window), box);
      
    g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);
    g_signal_connect (button, "clicked", G_CALLBACK (on_button_clicked), label);

    gtk_widget_show_all (window);
    gtk_main ();
    return 0;
}
