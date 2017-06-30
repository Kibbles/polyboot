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

## IP List:

By default, you can pull all Polycom phones out of all local DHCP scopes using the following Powershell snippet:

```
Get-DhcpServerv4Scope -cn (DHCP Server) | select ScopeID | ForEach-Object {
Get-DhcpServerv4Lease -cn (DHCP Server) -ScopeID $_.ScopeID | where {$_.HostName -like "Polycom*"} | select IPAddress
} > dhcp_polycomlist.txt
```

This will put all IPs into a text file called `dhcp_polycomlist.txt`. 

Remove the first two lines and you've got a list of IPs to give to polyboot.

## Hint:

Don't reconfigure 350 phones pointing to a single server simultaneously.

![danger](http://i.imgur.com/myH8Brf.png)
