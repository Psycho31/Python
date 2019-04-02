from netmiko import ConnectHandler
import getpass
import sys

USER = input("Username: ")
PASSWORD = getpass.getpass()
print("""
1 floor - 172.16.2.6
2 floor - 172.16.2.4
Adushkin plaza - 172.16.2.5
""")

DEVICES_IP = input("Enter the ip address: ")
DEVICE_PARAMS = {'device_type': 'cisco_ios',
                 'ip': DEVICES_IP,
                 'username': USER,
                 'password': PASSWORD, }

ssh = ConnectHandler(**DEVICE_PARAMS)

number = ''

while number != '6':
    print("""
    1. Change the number of the maximum mac-adresses
    2. Disable port
    3. Port info
    4. Transplant 2 users
    5. Change PC(1 user)
    6. Quit
    """)

    number = int(input("what do you want to do?: "))

    if number == 1:
        INVENTORY = input("enter the inventory of the pc: ")
        PORT = ssh.send_command("sh int status | i " + INVENTORY)
        PORT = PORT.split()
        PORT = PORT[0]
        PORT = 'interface ' + PORT
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("press any key"))
        MAX_MAC = input("enter maximum count of devices : ")
        COMMANDS = [PORT,
                "switchport port-security maximum " + MAX_MAC]
        RESULT = ssh.send_config_set(COMMANDS)
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("press any key"))


    elif number == 2:
        INVENTORY = input("enter the inventory of the pc: ")
        PORT = ssh.send_command("sh int status | i " + INVENTORY)
        PORT = PORT.split()
        PORT = PORT[0]
        PORT = "interface " + PORT
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("press any key"))
        NEW_INVENTORY = input("enter the new description of " + PORT + ":")
        clear_port = ssh.send_command("clear port-sec sti " + PORT)
        commands = [PORT,
                "shutdown",
                "description " + NEW_INVENTORY]
        RESULT = ssh.send_config_set(commands)
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("end. press any key"))


    elif number == 3:
        INVENTORY_1 = input("enter the inventory of the PC: ")
        PORT = ssh.send_command("sh int status | i " + INVENTORY_1)
        PORT = PORT.split()
        PORT = PORT[0]
        PORT = 'interface ' + PORT
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)

        print(input("press any key"))


    elif number == 4:
        INVENTORY_1 = input("enter inventory of 1st PC: ")
        PORT_1 = ssh.send_command("sh int status | i " + INVENTORY_1)
        PORT_1 = PORT_1.split()
        PORT_1 = PORT_1[0]
        PORT_1 = 'interface ' + PORT_1
        SHOW_1 = ssh.send_command("sh run " + PORT_1)
        print(SHOW_1)
        print(input("press any key"))
        NEW_INVENTORY_1 = input("enter new description of " + PORT_1 + ":")
        COMMANDS_PORT_1 = [PORT_1,
                       "description " + NEW_INVENTORY_1,
                       "no switchport port-security",
                       "no shutdown"]
        RESULT_1 = ssh.send_config_set(COMMANDS_PORT_1)
        SHOW_1 = ssh.send_command("sh run " + PORT_1)
        print(SHOW_1)
        print(input("press any key"))

        INVENTORY_2 = input("enter inventory of 2nd PC: ")
        PORT_2 = ssh.send_command("sh int status | i " + INVENTORY_2)
        PORT_2 = PORT_2.split()
        PORT_2 = PORT_2[0]
        PORT_2 = 'interface ' + PORT_2
        SHOW_2 = ssh.send_command("sh run " + PORT_2)
        print(SHOW_2)
        print(input("press any key"))
        NEW_INVENTORY_2 = input("enter new description of 2nd port: ")
        COMMANDS_PORT_2 = [PORT_2,
                       "description " + NEW_INVENTORY_2,
                       "no switchport port-security",
                       "no shutdown"]
        RESULT_2 = ssh.send_config_set(COMMANDS_PORT_2)
        SHOW_2 = ssh.send_command("sh run " + PORT_2)
        print(SHOW_2)
        print(input("press any key"))

        PORT_TEMP = ssh.send_command("sh int status | i temp")
        PORT_TEMP = PORT_TEMP.split()
        PORT_TEMP = PORT_TEMP[0]
        PORT_TEMP = 'interface ' + PORT_TEMP
        NEW_INVENTORY_TEMP = input("enter new description of temp port: " + PORT_TEMP + ":")
        COMMANDS_PORT_TEMP = [PORT_TEMP,
                          "description " + NEW_INVENTORY_TEMP,
                          "no switchport port-security",
                          "no shutdown"]
        REULST_TEMP = ssh.send_config_set(COMMANDS_PORT_TEMP)
        SHOW_TEMP = ssh.send_command("sh run " + PORT_TEMP)
        print(SHOW_TEMP)
        print(input("end. press any key"))

    elif number == 5:
        INVENTORY = input("enter the inventory of the pc: ")
        PORT = ssh.send_command("sh int status | i " + INVENTORY)
        PORT = PORT.split()
        PORT = PORT[0]
        PORT = 'interface ' + PORT
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("press any key"))
        clear_port = ssh.send_command("clear port-sec sti " + PORT)
        NEW_INVENTORY = input("enter the new description: ")
        COMMANDS = [PORT,
                "no shutdown",
                "description " + NEW_INVENTORY]
        RESULT = ssh.send_config_set(COMMANDS)
        SHOW = ssh.send_command("sh run " + PORT)
        print(SHOW)
        print(input("press any key"))

    else:
        print("""
    wrong number
      """)
print(input("press any key"))





