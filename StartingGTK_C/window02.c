#include<gtk/gtk.h>

int main(int argc, char* argv[])
{

      gtk_init(&argc,&argv);
      GtkWidget *window;

      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

      gtk_window_set_default_size(GTK_WINDOW(window),300,300);
      gtk_window_set_title(GTK_WINDOW(window),"Linux Foundation");
      g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit), NULL);

      gtk_widget_show(window);
      gtk_main();
      return 0;
}
