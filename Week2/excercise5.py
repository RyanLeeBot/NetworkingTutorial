'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.

https://github.com/ktbyers/pynet/tree/master/learning_python/lesson2
'''

with open('show_ip_bgp_summ.txt') as f:
    bgp_sum = f.readlines()

bgp_first = bgp_sum[1].strip()
bgp_last = bgp_sum[-1].strip()

bgp_first = bgp_first.split()
bgp_first = bgp_first[-1]

bgp_last = bgp_last.split()
bgp_last = bgp_last[0]


print(bgp_first, bgp_last)