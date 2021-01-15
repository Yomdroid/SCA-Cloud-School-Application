# importing Libraries
import platform
from shutil import which
import subprocess

INSTALLED = "is already installed."
INSTALLING = "will be installed now."

def linux_installations():
    "This installs wget, curl and nodejs for Linux systems"
    # For Ubuntu or Debian
    if platform.version().find("Ubuntu") > -1 or platform.version().find("Debian") > -1:
        if which("wget") is not None:
            print(f"Wget {INSTALLED} \n")
        else:
            print(f"Wget {INSTALLING} \n")
            sudo_command = ["sudo", "apt-get", "install", "wget"]
            subprocess.run(sudo_command, check = True)
        if which("curl") is not None:
            print(f"Curl {INSTALLED} \n")
        else:
            print(f"Curl {INSTALLING} \n")
            sudo_command = ["sudo", "apt-get", "install", "curl"]
            subprocess.run(sudo_command, check = True)
        if which("node") is not None:
            print(f"Nodejs {INSTALLED} \n")
        else:
            print(f"Nodejs {INSTALLING} \n")
            sudo_command = ["sudo", "apt-get", "install", "nodejs", "npm"]
            subprocess.run(sudo_command, check = True)
    # for Fedora
    if "fc" in platform.platform():
        if which("wget") is not None:
           print(f"Wget {INSTALLED} \n")
        else:
            print(f"Wget {INSTALLING} \n")
            sudo_command = ["sudo", "dnf", "install", "wget"]
            subprocess.run(sudo_command, check = True)
        if which("curl") is not None:
            print(f"Curl {INSTALLED} \n")
        else:
            print(f"Curl {INSTALLING} \n")
            sudo_command = ["sudo", "dnf", "install", "curl"]
            subprocess.run(sudo_command, check = True)
        if which("node") is not None:
            print(f"Nodejs {INSTALLED} \n")
        else:
            print(f"Nodejs {INSTALLING} \n")
            sudo_command = ["sudo", "dnf", "install", "nodejs", "npm"]
            subprocess.run(sudo_command, check = True)

def mac_installations():
    "This installs wget, curl and nodejs for Mac systems"
    if which("wget") is not None:
        print(f"Wget {INSTALLED} \n")
    else:
        print(f"Wget {INSTALLING} \n")
        sudo_command = ["brew", "install", "wget"]
        subprocess.run(sudo_command, check = True)
    if which("curl") is not None:
        print(f"Curl {INSTALLED} \n")
    else:
        print(f"Curl {INSTALLING} \n")
        sudo_command = ["brew", "install", "curl"]
        subprocess.run(sudo_command, check = True)
    if which("node") is not None:
        print(f"Nodejs {INSTALLED} \n")
    else:
        print(f"Nodejs {INSTALLING} \n")
        sudo_command = ["brew", "install", "node"]
        subprocess.run(sudo_command, check = True)

def window_installations():
    "This installs wget, curl and nodejs for Window systems"
    if which("wget") is not None:
        print(f"Wget {INSTALLED} \n")
    else:
        print(f"Wget {INSTALLING} \n")
        sudo_command = ["choco", "install", "wget"]
        subprocess.run(sudo_command, check = True)
    if which("curl") is not None:
        print(f"Curl {INSTALLED} \n")
    else:
        print(f"Curl {INSTALLING} \n")
        sudo_command = ["choco", "install", "curl"]
        subprocess.run(sudo_command, check = True)
    if which("node") is not None:
        print(f"Nodejs {INSTALLED} \n")
    else:
       print(f"Nodejs {INSTALLING} \n")
       sudo_command = ["choco", "install", "nodejs"]
       subprocess.run(sudo_command, check = True)
    
def run_script():
    system = platform.system()
    if  system == "Linux" or system == "Linux2":
        linux_installations()
    elif system == "Darwin":
        mac_installations()
    elif system == "Win32" or system == "Win64" or system =="Cygwin":
        window_installations()

run_script()
