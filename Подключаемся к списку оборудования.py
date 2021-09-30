from netmiko import ConnectHandler
import getpass
import sys

USER = input("Username: ")
PASSWORD = getpass.getpass()

device_list = ["172.19.2.3", "172.19.2.4"]
for i in device_list:
    CONNECT = {'device_type': 'cisco_ios',
               'ip': i,
               'username': USER,
               'password': PASSWORD, }
    ssh = ConnectHandler(**CONNECT)
    show = ssh.send_command('sh ip int br | i 1/0/1')
    show_hostname = ''.join(ssh.send_command("sh running-config | i hostname"))
    show_hostname = show_hostname[9::]
    test = open(r"c:\test\test3.txt", 'a')
    print('HOST: ' + show_hostname + ' ' + 'IP-address: ' + CONNECT.pop('ip'), file=test)
    print(show, file=test)
    print("---" * 10, file=test)

