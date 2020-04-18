'''

 https://github.com/ktbyers/pynet/tree/master/learning_python/lesson4
 
Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen.
'''


import re 

with open('show_ipv6_intf.txt') as f:
    show_ipv6 = f.read()

# Use re.DOTALL to have .* span newlines
match = re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", show_ipv6, flags=re.DOTALL)



#MY VERSION
ip_list = match.group(1).split()
ip_list.pop(1)

print(ip_list)


'''
#Kirks fancy version

for i, address in enumerate(ip_list[:]):
    address = re.sub(r"\[VALID\]", "", address)
    ip_list[i] = address.strip()

print()
print('-' * 80)
print(ip_list)
print('-' * 80)
print()

'''