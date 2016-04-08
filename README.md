# AutoPing V 1.0
Python / Windows script to ping a range of ip adresses, collate responses, and return active adresses.
## Requires: 
- Python 3.5 (tested) or prevoius versions (theoretical)
- Windows / Dos shell (Ping, Findstr)
- (optional) Windows Shell scripts (.cmd)
In the future, I may port this program to linux, since the commands are simmilar, and many users prefer linux.
## Use:
- when run, the program will ask for an ip adress range. This should be supplied in the format: 192.168.1.1-10 (but substitute your own ip adress range)
- this progam currently only scans ranges on the last digit set (192.168.1.1-10 works, but 192.168.1-10.1 does not work)
- this program is network intensive. Do not try this at peak network times, as the ping command hogs network resources, and for that reason is not typically automated.
