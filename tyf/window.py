#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gio, GLib, Gtk
import signal


class MainWindow(Gtk.ApplicationWindow):
    use_csd = False

    def __init__(self, application, **kwargs):
        super().__init__(application=application, **kwargs)
        self.set_size_request(800, 600)
        self.load_configs()

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.stack = Gtk.Stack()
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        self.box.pack_end(self.stack, True, False, 6)

        if self.use_csd:
            self.header_bar = Gtk.HeaderBar()
            self.header_bar.set_show_close_button(True)
            self.header_bar.set_custom_title(self.stack_switcher)
            self.set_titlebar(self.header_bar)
        else:
            self.switcher_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            self.switcher_box.set_center_widget(self.stack_switcher)
            self.box.pack_start(self.switcher_box, False, False, 6)

        self.add(self.box)

        self.show_all()

    def add_page(self, widget: Gtk.Widget, page_id: str, name: str):
        self.stack.add_titled(widget, page_id, name)

    def load_configs(self):
        self.use_csd = True


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="com.github.cr0vy.tyf",
            **kwargs
        )

        GLib.set_application_name("TYF")

        self.window = None

        self.activate()

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(application=self, title="TYF")
        
        self.window.present()
    
    def do_startup(self):
        Gtk.Application.do_startup(self)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        action = Gio.SimpleAction.new("quit")
        action.connect("activate", lambda *x: self.quit())
        self.add_action(action)
        self.add_accelerator("<Primary>q", "app.quit")
