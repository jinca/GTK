#include<gtk/gtk.h>

static void button_clicked(GtkWidget* widget, gpointer data)
{
      gtk_label_set_text(GTK_LABEL(data),"Welcome to APISTRAT");
}

int main(int argc, char* argv[])
{

      gtk_init(&argc,&argv);

      GtkWidget *window, *label, *button, *hbox;

      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
      
      label = gtk_label_new("                            ");

      button = gtk_button_new_with_label("Click me");

      hbox = gtk_box_new(0,0);

      
      gtk_window_set_default_size(GTK_WINDOW(window),300,300);

      gtk_window_set_title(GTK_WINDOW(window),"Linux Foundation");

      g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit), NULL);


      g_signal_connect(button,"clicked",G_CALLBACK(button_clicked), (gpointer)label);
     

      gtk_box_pack_start(GTK_BOX(hbox),label,1,1,0);

      gtk_box_pack_start(GTK_BOX(hbox),button,1,1,0);

      gtk_container_add(GTK_CONTAINER(window),hbox);

      gtk_widget_show_all(window);

      gtk_main();

      return 0;

}
