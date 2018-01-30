#include<gtk/gtk.h>

static void button_clicked(GtkWidget *widget, gpointer data)
{
    g_print("%s\n",gtk_entry_get_text(GTK_ENTRY(data)));
}

int main(int argc, char* argv[])
{
        gtk_init(&argc,&argv);

        GtkWidget *window,*entry,*button,*box;

        window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
       
        gtk_window_set_title(GTK_WINDOW(window),"Linux Foundation");

        g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit),NULL);

        entry = gtk_entry_new();
       
        button =gtk_button_new_with_label("Click me");
   
        g_signal_connect(button,"clicked",G_CALLBACK(button_clicked), entry);

        box = gtk_box_new(0,0);

        gtk_box_pack_start(GTK_BOX(box),entry,0,0,0);

        gtk_box_pack_start(GTK_BOX(box),button,1,1,0);

        gtk_container_add(GTK_CONTAINER(window),box);

        gtk_widget_show_all(window);

        gtk_main();

        return 0;
}
