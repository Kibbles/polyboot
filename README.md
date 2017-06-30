# polyboot
Reboot or reset Polycom phones remotely using curl commands (OS X / Linux).

Based on jgulczyn's post on the Polycom forums:

http://community.polycom.com/t5/VoIP/Remote-reboot-of-VVX-600s/m-p/89610#M19979

Tested on VVX300 and SoundPoint 331 phones.

## Usage:
```
./polyboot.py (-s / -f) (ip address / file) (reboot / factory) (admin PW)

Reboot (single phone /IP):        polyboot.py -s 127.0.0.1 reboot 1234
Factory Reset (single IP):        polyboot.py -s 127.0.0.1 factory 1234

Reboot (IP list, one per line):   polyboot.py -f iplist.txt reboot 1234
Factory Reset (IP list):          polyboot.py -f iplist.txt factory 1234
```

## Hint:

Don't reconfigure 350 phones pointing to a single server simultaneously.

![danger](http://i.imgur.com/myH8Brf.png)
