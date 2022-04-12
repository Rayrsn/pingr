from ping3 import ping
import ping3
from pybeep.pybeep import PyBeep
import time
import os
import termcolor
import colorama
colorama.init()
# os.system('mode con: cols=80 lines=20')
lepinghost = input('host (Default is google.com): ') or "google.com"
ping3.EXCEPTIONS = True
leping = 0
global Timeout
global HostUnknown
Timeout = 0
HostUnknown = 0

def BeepBeep():
    PyBeep().beep()
    PyBeep().beep()
def Boop():
    PyBeep().beep()
def BOOOOOOP():
    PyBeep().beep()

Boop()

while 1:
    time.sleep(1)
    os.system('clear')
    # os.system('cls')
    if Timeout == 0 and HostUnknown == 0: 
        print(termcolor.colored('Currently pinging: ' + lepinghost, "green"))
    if Timeout !=0 and HostUnknown ==0:
        print(termcolor.colored('Currently pinging: ' + lepinghost, "green") + '    ' + termcolor.colored('Total Timeouts: ' + str(Timeout), 'red', 'on_white'))
    if Timeout ==0 and HostUnknown !=0:
        print(termcolor.colored('Currently pinging: ' + lepinghost, "green") + '    ' + termcolor.colored('Total Unknown Hosts: ' + str(HostUnknown),'red', 'on_white'))
    if Timeout !=0 and HostUnknown !=0:
        print(termcolor.colored('Currently pinging: ' + lepinghost, "green") + '    ' + termcolor.colored('Total Timeouts: ' + str(Timeout), 'red', 'on_white') + '    ' + termcolor.colored('Total Unknown Hosts: ' + str(HostUnknown),'red', 'on_white'))
    try:
        leping = ping(lepinghost,unit='ms',timeout=4,size=24,ttl=97)
    except ping3.errors.Timeout:
        BeepBeep()
        Timeout += 1
        leping = "Invalid"
    except ping3.errors.HostUnknown:
        BOOOOOOP()
        HostUnknown += 1
        leping = "Invalid"
    except ping3.errors.DestinationHostUnreachable:
        Boop()
        pass
        leping = "Invalid"

    if type(leping) == float:
        print('          ' + termcolor.colored('Current Ping:', 'red', 'on_blue') + " " + termcolor.colored(str(int(leping)), 'grey','on_cyan', attrs=['reverse']))
    if type(leping) != float:
        print('          ' + termcolor.colored('Current Ping:', 'red', 'on_blue') + " " + termcolor.colored(str(leping), 'grey','on_cyan', attrs=['reverse']))
