import stat
import shutil
import os

if os.getuid() != 0:
    exit("PrivilegeError: root access required...")

if os.path.exists("/usr/bin/apt"):

    print("Setup has detected APT on your system, would you like to install eskimo for APT?")

    if input("Y\\n").lower() != "n":
        shutil.copyfile("src/apt.py", "/usr/bin/eskimo")
        os.chmod("/usr/bin/eskimo", stat.S_IXOTH)
    else:
        pass

elif os.path.exists("/usr/bin/dnf"):

    print("Setup has detected DNF on your system, would you like to install eskimo for DNF ?")

    if input("Y\\n").lower() != "n":
        shutil.copyfile("src/dnf.py", "/usr/bin/eskimo")
        os.chmod("/usr/bin/eskimo", stat.S_IRWXO)
    else:
        pass

elif os.path.exists("/usr/bin/pacman"):

    print("Setup has detected pacman on your system, would you like to install eskimo for pacman ?")
    if input("Y\\n").lower() != "n":
        shutil.copyfile("src/pacman.py", "/usr/bin/eskimo")
        os.chmod("/usr/bin/eskimo", stat.S_IRWXO)
    else:
        pass

elif os.path.exists("/usr/bin/zypper"):

    print("Setup has detected zypper on your system, would you like to install eskimo for zypper ?")

    if input("Y\\n").lower() != "n":
        shutil.copyfile("src/dnf.py", "/usr/bin/eskimo")
        os.chmod("/usr/bin/eskimo", stat.S_IRWXO)
    else:
        pass
