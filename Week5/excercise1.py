'''
https://github.com/ktbyers/pynet/tree/master/learning_python/lesson5


1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.


1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
'''

def ssh_conn(ip_addr, username='admin', password='woot', device_type='cisco_ios'):

    print()
    print(30 * '-')
    print('IP Address: {}'.format(ip_addr))
    print('Username: {}'.format(username))
    print('Password: {}'.format(password))
    print('Device Type: {}'.format(device_type))
    print(30 * '-')
    print()

ssh_conn('10.1.1.10', device_type='mydevce')



def ssh_conn2(ip_addr, username, password, device_type="cisco_ios"):
    print("-" * 80)
    print("IP Addr: {}".format(ip_addr))
    print("Username: {}".format(username))
    print("Password: {}".format(password))
    print("Platform: {}".format(device_type))
    print("-" * 80)


# Adding a default value
ssh_conn2('192.168.1.1', password='cisco123', username='admin1')
ssh_conn2('192.168.1.1', password='cisco123', username='admin1', device_type="cisco_nxos")

my_device = {
    "ip_addr": "172.16.1.1",
    "device_type": "cisco_xr",
    "username": "admin",
    "password": "cisco123"
}
ssh_conn2(**my_device)