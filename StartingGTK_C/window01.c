#include<gtk/gtk.h>

void main(int argc, char* argv[])

{

      gtk_init(&argc,&argv);

      GtkWidget *window;

      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

      g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit), NULL);

      gtk_widget_show(window);

      gtk_main();

}
