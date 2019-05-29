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

        #finds distro name in /etc/os-release
    with open("/etc/os-release") as f:
        dist_name = f.read().lower().split()[0] #split /etc/os-release into string bits and select the first one with name=*DISTRO*
        dist_name = dist_name.replace("name=", "") #remove "name=" identifier
        dist_name = dist_name.replace("pretty_", "") #because debian just HAS to be different
        dist_name = dist_name.replace('"', '')#remove quotes around distro name


if __name__ == "__main__":
    #used to check if program works correctly

    find_distro()
    print("Your distro is: " + dist_name)
