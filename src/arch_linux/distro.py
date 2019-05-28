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
#distro.py

def find_distro():

    """
    find linux distro via /etc/os-release
    """

    global dist_name
    global dist_ver

    try:
        fh = open('/etc/os-release', 'r')
    except:
        exit("Sorry, your distribution could not be found :(\nAre you sure that you're using Linux?")

    with open("/etc/os-release") as f:
        dist_name = f.read().lower().split()[0]
        dist_name = dist_name.replace("name=", "")
        dist_name = dist_name.replace('"', '')

    with open("/etc/os-release") as f:
        dist_ver = f.read().lower().split()[10]
        dist_ver = dist_ver.replace('"', '')
        dist_ver = dist_ver.replace("version_id=", "")

find_distro()

if __name__ == "__main__":
    #used to check if program works correctly
    print("Your distro is: " + dist_name)
    print("Your version is: " + dist_ver)
