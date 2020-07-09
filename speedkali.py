import os
import apt
import sys
import subprocess

def banner():
    print("*"*60)
    print("\tKALI UPDATE SPPED FIX | BY EXPLOIT EVERYTHING ")
    print("*"*60)

def sudocheck():
    if not os.geteuid() == 0:
        sys.exit("\n [+] Only Root Can Run This Script \n [+] Try \"sudo speedkali.py\" ")

def showcurrentsource():
    try:
        source = open("/etc/apt/sources.list", "r")
        print("*"*60)
        print("\t THIS IS YOUR CURRENT KALI SOURCE REPO LIST\n")
        print(source.read()) 
    except Exception:
        print(" [+] FILE NOT FOUND")
        print(" [+] CHECK /etc/apt/sources.list EXISTS OR NOT")
        print("*"*60)

def packageinstall():
    pkg_name = "apt-transport-https"
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    pkg = cache[pkg_name]
    print("*"*60)
    print("\n")
    if pkg.is_installed:
        print(" [+] {pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        pkg.mark_install()
        print("\n[+] {pkg_name}  installed".format(pkg_name=pkg_name))
        try:
            cache.commit()
        except Exception as arg:
            print(sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg)))
    print("\n")
def modifysource():
    source = open("/etc/apt/sources.list", "r+")
    source.truncate(0)
    with open("/etc/apt/sources.list", 'a') as line:
        line.write("deb https://mirror.cedia.org.ec/kali kali-rolling main non-free contrib")
    print("*"*60)
    print("\t THIS IS YOUR NEW KALI SOURCE REPO LIST\n")
    print(source.read()) 

def renamedns():
    dns = open("/etc/resolv.conf", "r+")
    print("*"*60)
    print(" [+] OLD DNS CONFIG \n")
    print(dns.read())
    dns.truncate(0)  
    with open("/etc/resolv.conf", 'a') as line:
        line.write("nameserver 8.8.8.8\n")
        line.write("nameserver 8.8.4.4\n")
    print("*"*60)
    print(" [+] NEW DNS CONFIG \n")
    dns = open("/etc/resolv.conf", "r+")
    print(dns.read())

def updateskali():
    print("*"*60)
    print(" [+] UPDATING KALI LINUX\n")
    subprocess.call("sudo apt update",shell=True)
    print("*"*60)
    print(" [+] SETTING DONE!")
    print(" [+] SUBSCRIBE OUR YOUTUBE CHANNEL FOR MORE")
    print(" [+] https://www.youtube.com/c/ExploitEverything")
    print("*"*60)

if __name__ == "__main__":
    banner()
    sudocheck()
    showcurrentsource()
    packageinstall()
    modifysource()
    renamedns()
    updateskali()