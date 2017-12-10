#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
    GtkWidget *win, *grid, *b1, *b2, *cb1, *cb2, *cb3, *cb4;
    
    gtk_init (&argc, &argv);
    win = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title (GTK_WINDOW (win), "Language Selector");
    gtk_window_set_default_size (GTK_WINDOW (win), 60, 80);
    gtk_container_set_border_width (GTK_CONTAINER (win), 10);

    grid = gtk_grid_new ();
    
    b1 = gtk_button_new_with_label ("Quit");
    g_signal_connect (b1, "clicked", G_CALLBACK (gtk_main_quit), NULL);

    b2 = gtk_button_new_with_label ("Learn");

    cb1 = gtk_check_button_new_with_label ("Java");
    cb2 = gtk_check_button_new_with_label ("Python");
    cb3 = gtk_check_button_new_with_label ("C");
    cb4 = gtk_check_button_new_with_label ("Java Script");

    gtk_grid_attach (GTK_GRID (grid), b1, 1, 3, 1, 1);
    gtk_grid_attach (GTK_GRID (grid), b2, 3, 3, 1, 1);
    gtk_grid_attach (GTK_GRID (grid), cb1, 1, 1, 1, 1);
    gtk_grid_attach (GTK_GRID (grid), cb2, 1, 2, 1, 1);
    gtk_grid_attach (GTK_GRID (grid), cb3, 3, 1, 1, 1);
    gtk_grid_attach (GTK_GRID (grid), cb4, 3, 2, 1, 1);

    gtk_container_add (GTK_CONTAINER (win), grid);

    g_signal_connect (win, "destroy", G_CALLBACK (gtk_main_quit), NULL);
    gtk_widget_show_all(win);
    
    gtk_main();
    return 0;
}
