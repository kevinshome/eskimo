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
#main.py

#import sys for exit and args
import sys
import os

#checker for root privs
userenv = os.getenv("USER")
if userenv != 'root':
    if len(sys.argv) > 1:
        if "--noroot" not in sys.argv:
            print("eskimo requires root privileges\nnext time, try 'sudo eskimo ...'")
            sys.exit()


#very basic and actually bad practice, i know
#it's just that my knowledge is limited
#so here's the argument handler
#yes, i realise I could've just used argparse or something similar, but I preferred this
def arghandle():
    if slen > 1:
        #help message
        if carg == "--help" or carg == "-h":
            SJ.help()
        elif carg == "install":
            SJ.install()
        elif carg == "uninstall":
            SJ.uninstall()
        elif carg == "-s" or carg == "--speedtest":
            SJ.stest()
        else:
            pass

#Spaghetti Junction: where the unholy maddness happens
class SJ:
    def help():
        #ASCII art from http://ascii.co.uk/art/eskimo
        print("""eskimo, the modern package manager (for portage)
v0.1a (Gucci)                                                   (o)
                                                               (_|_)
                                                                |||

[arguments]
"-h", "--help"                          show this message
"-s", "--speedtest"                     test internet speed (using sivel/speedtest-cli)

[commands]
install [PACKAGE]                       install a package
uninstall [PACKAGE]                     uninstall a package

released by kevinshome""")
        sys.exit()
    def install(): #install a package
        sarg = sys.argv
        if len(sarg) - 1 == sarg.index("install"):
            print("No install target was specified\nPlease try again, or use -h for help")
            sys.exit()
        install_pkg = sarg[sarg.index("install") + 1] #pkg to be installed
        print("Installing {0}".format(install_pkg))

        os.system("emerge [-a] {0}".format(install_pkg))

    def uninstall(): #uninstall a package
        sarg = sys.argv
        if len(sarg) - 1 == sarg.index("uninstall"):
            print("No uninstall target was specified\nPlease try again, or use -h for help")
            sys.exit()
        upkg = sarg[sarg.index("uninstall") + 1] #grab pkg to uninstall from sysargs
        print("Uninstalling " + upkg)

        os.system("emerge -C {0}".format(upkg))
    def stest(): #internet speed test
        #makes use of sivel's speedtest.net command line tool
        os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -")

# below is the mantis makeshift argument parser
# this may seem simple, but it came to me after about 3 mtn dew code reds
slen = len(sys.argv)
num = 0

if "--noroot" in sys.argv:
    print("Running eskimo in no-root mode, may not work.")

if slen > 1:
    while num < slen - 1:
        num = num + 1
        carg = sys.argv[num]
        arghandle()
else:
    SJ.help()

sys.exit()