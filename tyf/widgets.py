#!/usr/bin/python3

import gettext
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

_ = gettext.gettext


class TypeWidget(Gtk.Frame):
    def __init__(self, name: str):
        Gtk.Frame.__init__(self)

        self.box = Gtk.Box(self, orientation=Gtk.Orientation.VERTICAL)
        self.name_label = Gtk.Label(label=name)
        self.add_button = Gtk.Button(label=_("Add"))
        self.scrolled_window = Gtk.ScrolledWindow()
        self.column_widgets_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.scrolled_window.add(self.column_widgets_box)

        self.box.pack_start(self.name_label, False, False, 3)
        self.box.pack_start(self.scrolled_window, True, True, 3)
        self.box.pack_end(self.add_button, False, False, 3)

        self.add_button.connect("clicked", self.add_column_widget)

        self.add(self.box)

    def add_column_widget(self, event):
        frame = Gtk.Frame()
        column_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        name_entry = Gtk.Entry()
        sum_entry = Gtk.Entry()
        sum_entry.set_sensitive(False)

        column_box.pack_start(name_entry, True, True, 0)
        column_box.pack_start(sum_entry, False, False, 0)

        frame.add(column_box)
        frame.show_all()

        self.column_widgets_box.pack_start(frame, False, False, 0)


class EventsWidget(Gtk.Frame):
    def __init__(self, name: str):
        Gtk.Frame.__init__(self)

        self.box = Gtk.Box(self, orientation=Gtk.Orientation.VERTICAL)
        self.name_label = Gtk.Label(label=name)
        self.add_button = Gtk.Button(label=_("Add"))
        self.scrolled_window = Gtk.ScrolledWindow()
        self.column_widgets_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.scrolled_window.add(self.column_widgets_box)

        self.box.pack_start(self.name_label, False, False, 3)
        self.box.pack_start(self.scrolled_window, True, True, 3)
        self.box.pack_end(self.add_button, False, False, 3)

        self.add(self.box)
