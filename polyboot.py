#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------
# Polyboot
# ========
# A simple program to reboot or factory-reset Polycom phones using CURL commands to interact with the phone's web UI.
# Adjust the authentication password below accordingly.
#
# Usage
# ~~~~~
# ./polyboot.py (-s / -f) (ip address / file) (reboot / factory) (admin PW)
#
# Reboot (single phone /IP):        polyboot.py -s 127.0.0.1 reboot 1234
# Factory Reset (single IP):        polyboot.py -s 127.0.0.1 factory 1234
#
# Reboot (IP list, one per line):   polyboot.py -f iplist.txt reboot 1234
# Factory Reset (IP list):          polyboot.py -f iplist.txt factory 1234
# ----------------------------------------------------------------------------------------------------------------------

from subprocess import Popen
from sys import argv
from base64 import b64encode
from time import sleep

# Auth string glued in front of password
auth_string = "Polycom:"


# Help text
help = '''Usage:
------
polyboot.py (-f [ip address file] or -s [single IP address]) [reboot / factory] (admin pw)
ex.: polyboot.py -s 127.0.0.1 reboot 456
'''


# Rebooting the phone
def reboot(ip):
    reboot_curl = ['curl',
                   '-k',
                   'https://' + str(ip) + '/form-submit/Reboot',
                   '-X',
                   'POST',
                   '-H',
                   'Authorization: Basic ' + b64encode(admin_password),
                   '-H',
                   'Content-Length: 0',
                   '-H',
                   'Content-Type: application/x-www-form-urlencoded',
                   '-H',
                   'Cookie: Authorization=Basic ' + b64encode(admin_password)]
    Popen(reboot_curl, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
    return


# Factory-resetting the phone
def factory_reset(ip):
    factory_curl = ['curl',
                    '-k',
                    'https://' + str(ip) + '/form-submit/Utilities/restorePhoneToFactory',
                    '-X',
                    'POST',
                    '-H',
                    'Authorization: Basic ' + b64encode(admin_password),
                    '-H',
                    'Content-Length: 0',
                    '-H',
                    'Content-Type: application/x-www-form-urlencoded',
                    '-H',
                    'Cookie: Authorization=Basic ' + b64encode(admin_password)]
    Popen(factory_curl, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
    return


if len(argv) < 5 or len(argv) > 5:
    print('ERROR: Incorrect arguments supplied (got ' + str(len(argv)- 1) + ', expected 4)')
    print(help)


# Multi-address (file) mode
elif argv[1] == '-f':
    filename = argv[2]
    admin_password = auth_string + argv[4]
    try:
        with open(filename) as f:
            for line in f:
                ip = line.strip()
                if argv[3] == 'reboot':
                    reboot(ip)
                    print('Reboot instruction sent to address: ' + ip)
                    sleep(0.4)

                elif argv[3] == 'factory':
                    factory_reset(ip)
                    print('Factory reset instruction sent to address: ' + ip)
                    sleep(0.4)

                else:
                    print('ERROR: ' + argv[3] + ' is an invalid operation flag.')
                    print(help)
                    break

    except Exception as error:
        print('ERROR: File couldn\'t be opened.')
        print error


# Single-IP mode
elif argv[1] == '-s':
    admin_password = auth_string + argv[4]
    if argv[3] == 'reboot':
        ip = argv[2]
        reboot(ip)
        print('Reboot instruction sent to address: ' + ip)

    elif argv[3] == 'factory':
        ip = argv[2]
        factory_reset(ip)
        print('Factory reset instruction sent to address: ' + ip)

    else:
        print('ERROR: ' + argv[3] + ' is an invalid operation flag.')
        print(help)

else:
    print('Unknown mode. Use either -s or -f.')
    print(help)
