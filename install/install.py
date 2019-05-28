#bytecode fucking sucks
import sys
sys.dont_write_bytecode = True

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
#install.py
#
#This is the installer for eskimo
#Use Wisely

#imports
import os
from install_header import *
import shutil
import time
import distro

#test to see if install already exists
if "--uninstall" not in sys.argv:
    exists = os.path.isfile("/usr/bin/eskimo")
    if exists:
        print("It looks as if an installation of eskimo exists already on this system (/usr/bin/eskimo)")
        exit("You will need to uninstall any previous installations of eskimo before installing a new one")

#distro var set
distro.find_distro()
user_dist = distro.dist_name

#root checker
if os.geteuid() != 0:
    exit("eskimo requires root priveleges to install\nRun 'sudo python install.py [...]'")

#argument checker from install_header
sysarg_check()

#basic funcs
def clr():
    os.system("clear")

#steps
def step1():
    print("    - Checking for and installing pyinstaller if missing.")
    #Install PyInstaller
    os.system("python3 -m pip install pyinstaller -q")
    #END

def step2():

    global src_dist

    print("    - Building base executable with pyinstaller")
    #PyInstaller
    os.system("pyinstaller ../src/{0}/main.py --onefile".format(src_dist))
    shutil.rmtree("build")
    os.remove("main.spec")
    #END

def step3():
    if "--no-dir-make" not in sys.argv:
        print("    - Making required dirs for eskimo in /usr/lib")
        os.mkdir("/usr/lib/eskimo")
    #END

def step4():
    print("    - Installing binary package")
    os.rename("dist/main", "/usr/bin/eskimo")
    shutil.rmtree("dist")
    #END

def distro_check():

    global src_dist

    if user_dist.lower() == "ubuntu" or user_dist.lower() == "debian":
        src_dist = "debian"
    #END

#code
clr()
print("Welcome to the installer for eskimo v0.0.1 (Off-White)")
input("Press ENTER to begin installation...\n")

distro_check()

if "--no-dep-install" not in sys.argv:
    print("Gathering and installing dependencies")
    step1()
if "--no-build" not in sys.argv:
    print("Building executable")
    step2()
if "--no-req-files" not in sys.argv:
    print("Creating /usr/lib required files")
    step3()
if "--no-move-exec" not in sys.argv:
    print("Installing binary package")
    step4()
print("Installation Finished!")
sys.exit()
