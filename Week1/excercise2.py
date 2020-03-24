ip_addr = input("Enter your IP: ")

octets = ip_addr.split('.')

print("\n")
print("{:^20}{:^20}{:^20}{:^20}".format('Octet1', 'Octet2', 'Octet3', 'Octect4'))
print("-" * 80)
print("{:^20}{:^20}{:^20}{:^20}".format(*octets))
print("{:^20}{:^20}{:^20}{:^20}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print("{:^20}{:^20}{:^20}{:^20}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print("-" * 80)
print("\n")