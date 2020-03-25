'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

ip_addresses = ['10.5.10.6', '10.30.0.2', '10.20.4.89', '10.67.20.1', '10.2.54.1']

ip_addresses.append('192.168.1.10')

azure_ips = ['172.30.0.1', '172.30.10.5']

ip_addresses.extend(azure_ips)

print(ip_addresses)

print(ip_addresses[0])

print(ip_addresses[-1])

ip_addresses.pop(0)

ip_addresses.pop(-1)

ip_addresses[0] = '255.255.255.0'

print(ip_addresses[0])