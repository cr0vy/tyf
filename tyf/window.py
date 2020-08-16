#!/usr/bin/python3

import gettext
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gio, GLib, Gtk
import signal

from .widgets import EventsWidget, TypeWidget

_ = gettext.gettext

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

        self.main_widget = MainWidget()
        self.budget_widget = BudgetWidget()

        self.add_page(self.main_widget, "main_widget", _("Main"))
        self.add_page(self.budget_widget, "budget_widget", _("Budget"))

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


"""
-----------
| Widgets |
-----------
"""
class BudgetWidget(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_column_spacing(6)
        self.set_column_homogeneous(True)
        self.set_row_homogeneous(True)

        self.events_widget = EventsWidget(name=_("Events"))
        self.incomes_widget = TypeWidget(name=_("Incomes"))
        self.expenses_widget = TypeWidget(name=_("Expenses"))

        self.attach(Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL), 0, 0, 4, 1)
        self.attach(self.events_widget, 0, 1, 4, 5)
        self.attach(self.incomes_widget, 4, 1, 3, 5)
        self.attach(self.expenses_widget, 7, 1, 3, 5)

class MainWidget(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
