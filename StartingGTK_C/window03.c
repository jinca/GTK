#include<gtk/gtk.h>

int main(int argc, char* argv[])

{

      gtk_init(&argc,&argv);

      GtkWidget *window, *label;

      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
      
      label = gtk_label_new("Welcome to APISTRAT");

      gtk_window_set_default_size(GTK_WINDOW(window),300,300);

      gtk_window_set_title(GTK_WINDOW(window),"Linux Foundation");

      g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit), NULL);

      gtk_container_add(GTK_CONTAINER(window),label);

      gtk_widget_show_all(window);

      gtk_main();

      return 0;

}
