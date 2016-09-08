# Ubuntu keyboard toggling applet (Unity / Gnome)
Adds an icon to the system tray for easily turning a keyboard off and back on,
for example on convertible netbooks or a docked laptop.

## Installation

To install, click the "Clone or Download" button in the top right and select
**Download ZIP**.  Extract the ZIP file to a folder on your computer.  From a
terminal, run:

```bash
xinput --list
```

This will list the id's for the input devices on your computer.  Find the one
that corresponds to your keyboard and note it down.  It will probably say
something like `AT Translated Set 2 keyboard`.  On some keyboards, for example
that of the Lenovo Yoga 11e on which this code was tested, there will also be an
additional line for "Extra Buttons" which you should note down as well.

In the extracted folder, open the file "KeyboardOnOffApplet.py" in a text editor
and change the number 12 after `KEYBOARD_XINPUT_ID` to match the id of your own
keyboard.  If your keyboard has an "Extra Buttons" portion, you can change the
number 14 after `EXTRA_BUTTONS_XINPUT_ID` to match that as well.  If not, just
remove the number to leave the blank quotes: `""`.

Finally, this applet is written in python and requires python3-gi to work.  To
install it, run this command in a terminal (you may be prompted for a password):

```bash
sudo apt install python3-gi
```

The applet is now ready to use.  You can test it by changing to the extracted
folder in a terminal session and typing `./KeyboardOnOffApplet.py` then hitting
enter.  You should see a new icon appear in your system tray showing a picture
of a keyboard.  **Be careful not to disable a keyboard that you have no way of
re-enabling**, for example by selecting "Disable Hardware Keyboard" and then
exiting the application before enabling it again.

The default icons configured in the applet are intended to match the default
Ubuntu theme as of version 16.04 LTS (Xenial Xerus). They have been modified
from the icons in [this post](http://askubuntu.com/a/713597) which I have included as well in case they match an
alternate theme better.  To change the icons used by the applet, simply update
the paths/filenames specified in `PATH_TO_ON_ICON` and `PATH_TO_OFF_ICON` to
match your own file.

Once you confirm that the applet works as desired, you may wish to set it so
that it runs by default every time you start your computer.  To do this, use the
"Startup Applications" program from the Ubuntu menu.  Add an entry, name it
something that makes sense to you, and for the "command" input browse to the
file "KeyboardOnOffApplet.py" in the folder where you extracted the applet.

## License information
This applet is [Free Software](https://en.wikipedia.org/wiki/Free_software).  Code is MIT licensed, and documentation is
licensed under CC BY-SA 4.0
