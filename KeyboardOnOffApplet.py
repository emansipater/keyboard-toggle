#!/usr/bin/env python3

#Imports
import os
import signal
from subprocess import call
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

#Unique indicator name
APPINDICATOR_ID = "keyboardonoff"

#Set this value to the keyboard id obtained from running xinput --list
KEYBOARD_XINPUT_ID = "12"

#Specify the id for additional buttons or leave empty to disable
EXTRA_BUTTONS_XINPUT_ID = "14"

#Specify filenames (or relative paths) for on and off icons here
PATH_TO_ON_ICON = './keyboardwhite.png'
PATH_TO_OFF_ICON = './keyboardwhiteoff.png'

class KeyboardOnOffIndicator(object):
    def __init__(self):
        self.indicator = AppIndicator.Indicator.new(
            APPINDICATOR_ID, os.path.abspath(PATH_TO_ON_ICON),
            AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)

        #Enable keyboard at start to ensure consistent state
        self.enable_keyboard(self)


    def run(self):
        Gtk.main()

    def update_menu(self, current_status):
        menu = Gtk.Menu()

        #Choose between enable and disable options based on current_status
        if current_status == 'enabled':
            item_keyboard_off = Gtk.MenuItem("Disable Hardware Keyboard")
            item_keyboard_off.connect('activate', self.disable_keyboard)
            menu.append(item_keyboard_off)
        elif current_status == 'disabled':
            item_keyboard_on = Gtk.MenuItem('Enable Hardware Keyboard')
            item_keyboard_on.connect('activate', self.enable_keyboard)
            menu.append(item_keyboard_on)

        #Option to quit the applet
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', quit)
        menu.append(item_quit)

        menu.show_all()
        self.indicator.set_menu(menu)

    def enable_keyboard(self, source):
        #use xinput to enable the keyboard
        call(["xinput", "enable", KEYBOARD_XINPUT_ID])

        #also enable extra buttons if needed
        if EXTRA_BUTTONS_XINPUT_ID:
            call(["xinput", "enable", EXTRA_BUTTONS_XINPUT_ID])

        #update icon and menu to reflect current status
        self.indicator.set_icon(os.path.abspath(PATH_TO_ON_ICON))
        self.update_menu('enabled')

    def disable_keyboard(self, source):
        #use xinput to disable the keyboard
        call(["xinput", "disable", KEYBOARD_XINPUT_ID])

        #also disable extra buttons if needed
        if EXTRA_BUTTONS_XINPUT_ID:
            call(["xinput", "disable", EXTRA_BUTTONS_XINPUT_ID])

        #update icon and menu to reflect current status
        self.indicator.set_icon(os.path.abspath(PATH_TO_OFF_ICON))
        self.update_menu('disabled')


def main():
    #Allow for keyboard interrupts
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    KeyboardOnOffIndicator().run()

if __name__ == "__main__":
    main()
