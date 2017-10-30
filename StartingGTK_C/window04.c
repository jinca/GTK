#include<gtk/gtk.h>

static void button_clicked(GtkWidget* widget, gpointer data)
{
       g_print("Welcome to APISTRAT\n");
}

int main(int argc, char* argv[])
{
      gtk_init(&argc,&argv);

      GtkWidget *window, *button;

      button = gtk_button_new_with_label("Click me");
      g_signal_connect(button,"clicked",G_CALLBACK(button_clicked), NULL);

      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
      gtk_window_set_default_size(GTK_WINDOW(window),300,300);
      gtk_window_set_title(GTK_WINDOW(window),"Linux Foundation");
      g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit), NULL);

      gtk_container_add(GTK_CONTAINER(window),button);

      gtk_widget_show_all(window);
      gtk_main();
      return 0;
}
