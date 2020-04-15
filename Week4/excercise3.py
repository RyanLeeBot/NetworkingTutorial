'''
Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version, serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
'''
import re

with open('show_version.txt') as f:
    show_version = f.read()


match = re.search(r"^Cisco IOS Software,.* Version (.*),", show_version, flags=re.M)

if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (.*)\s*$", show_version, flags=re.M)

if match:
    serial_number = match.group(1)

match = re.search(r"^Configuration register is (.*)\s*$", show_version, flags=re.M)

if match:
    register = match.group(1)


print()
print("{:>20}: {:15}".format("OS Version", os_version))
print("{:>20}: {:15}".format("Serial Numbern", serial_number))
print("{:>20}: {:15}".format("Register", register))
print()
