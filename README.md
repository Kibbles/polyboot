# polyboot
Reboot or reset Polycom phones remotely.

## Usage:
```
./polyboot.py (-s / -f) (ip address / file) (reboot / factory) (admin PW)

Reboot (single phone /IP):        polyboot.py -s 127.0.0.1 reboot 1234
Factory Reset (single IP):        polyboot.py -s 127.0.0.1 factory 1234

Reboot (IP list, one per line):   polyboot.py -f iplist.txt reboot 1234
Factory Reset (IP list):          polyboot.py -f iplist.txt factory 1234
```
