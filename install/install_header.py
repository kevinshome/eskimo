#eskimo/mantis
#Written by kevinshome
#
#
#   Copyright (C) 2019 kevinshome
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#install_header.py

import sys
import shutil
import os

def sysarg_check():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("""eskimo installer

usage: sudo python install.py [args]

[args]

"--help", "-h"                                  show this message
"--uninstall"                                   uninstall an existing mantis install

"--no-dep-install"                              supress installing dependencies from PyPi
"--no-build"                                    suppress building the binary executable
"--no-req-files"                                supress creation of /usr/lib/eskimo and files inside
"--no-move-exec"                                supress installation of executable to /usr/bin/

released by kevinshome""")
        sys.exit()
    if "--uninstall" in sys.argv:
        uch = input("Are you sure you want to remove eskimo? (Y/n): ")
        if uch.lower() == "y" or uch == "":
            print("Removing executable from /usr/bin/")
            os.remove("/usr/bin/eskimo")
            print("Remove directory tree from /usr/lib/")
            shutil.rmtree("/usr/lib/eskimo")
            print("eskimo successfully uninstalled.")
            sys.exit()
        else:
            print("Uninstall Terminated.\nNo files have been changed.")
            sys.exit()
