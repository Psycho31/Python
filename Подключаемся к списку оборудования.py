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
    show_hostname = ssh.send_command('sh run | i hostname')
    print(show_hostname)
    test = open(r"c:\test\test3.txt", 'a')
    print(show_hostname + ' ' + CONNECT.pop('ip'), file=test)
    print(show, file=test)
    print("---" * 10, file=test)
    
