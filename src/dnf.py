#!/usr/bin/env python3
#bytecode fucking sucks
import sys
sys.dont_write_bytecode = True

#eskimo/mantis
#Written by kevinshome
#
#
#    Copyright (c) 2020 kevinshome
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
#
#
#main.py

import os

esk_version = open("/etc/eskkv", "r").read()

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
        elif carg == "upgrade":
            os.system("dnf upgrade")
        elif carg == "dist-upgrade":
            os.system("dnf distro-sync")
        elif carg == "search":
            SJ.search()
        else:
            pass

#Spaghetti Junction: where the unholy maddness happens
class SJ:
    def help():
        #ASCII art from http://ascii.co.uk/art/eskimo
        print(f"""eskimo, the modern package manager (rpm/dnf)
v{esk_version}                                                   (o)
                                                               (_|_)
                                                                |||

[arguments]
"-h", "--help"                          show this message
"-s", "--speedtest"                     test internet speed (using sivel/speedtest-cli)

[commands]
install [PACKAGE]                       install a package
uninstall [PACKAGE]                     uninstall a package
upgrade                                 automatically upgrades upgradeable packages
dist-upgrade                            similar to upgrade, but performs more complex upgrades (i.e. distro upgrades)
search [PACKAGE]                        searches for package in available repositories and returns results

released by kevinshome""")
        sys.exit()
    def install(): #install a package
        sarg = sys.argv
        if len(sarg) - 1 == sarg.index("install"):
            print("No install target was specified\nPlease try again, or use -h for help")
            sys.exit()
        install_pkg = sarg[sarg.index("install") + 1] #pkg to be installed
        print("Installing {0}".format(install_pkg))

        os.system("dnf install {0}".format(install_pkg))

    def uninstall(): #uninstall a package
        sarg = sys.argv
        if len(sarg) - 1 == sarg.index("uninstall"):
            print("No uninstall target was specified\nPlease try again, or use -h for help")
            sys.exit()
        upkg = sarg[sarg.index("uninstall") + 1] #grab pkg to uninstall from sysargs
        print("Uninstalling " + upkg)

        os.system("dnf remove {0}".format(upkg))
    def stest(): #internet speed test
        #makes use of sivel's speedtest.net command line tool
        os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -")
    def search():
        sarg = sys.argv
        if len(sarg) - 1 == sarg.index("search"):
            print("No search target was specified\nPlease try again, or use -h for help")
            sys.exit()
        spkg = sarg[sarg.index("search") + 1] #grab pkg to search for
        print("Searching for " + spkg)
        print("Results:\n")

        os.system("dnf search {0}".format(spkg))

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
