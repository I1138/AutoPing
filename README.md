# AutoPing V 0.1 for Linux
Python / Linux script to ping a range of ip adresses, collate responses, and return active adresses.
In the future this program may be ported to linux, since the commands are simmilar, and many users prefer linux.

## Requires: 
- Python 3.5 (tested) or previous versions (theoretical)
- BASH shell (Ping)

## Use:
- When run, the program will ask for an ip adress range. This should be supplied in the format: 192.168.1.1-10 (but substitute your own ip adress range)
- This progam currently only scans ranges on the last digit set (192.168.1.1-10 works, but 192.168.1-10.1 does not work)
- This program is network intensive. Do not try this at peak network times, as the ping command hogs network resources, and for that reason is not typically automated.

_Note: Some Python installations may not recognize .py files as python by default, if this ocurrs, simply set python as the default program for .py files_

**This project is licensed under the MIT open source license, refer to the LICENSE.md file for details.**
