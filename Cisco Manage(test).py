from netmiko import ConnectHandler
import getpass
import sys

USER = input("Username: ")
PASSWORD = getpass.getpass()

DEVICE = ''

while DEVICE != '4':
    print("""
    1. Первый этаж
    2. Второй этаж
    3. Адушкин плаза
    4. Выход
    """)
    DEVICE = (int(input('Выберите усройство: ')))
    if DEVICE ==1:
        DEVICES_IP = "172.16.2.6"
        DEVICE_PARAMS = {'device_type': 'cisco_ios',
                        'ip': DEVICES_IP,
                        'username': USER,
                        'password': PASSWORD, }
        ssh = ConnectHandler(**DEVICE_PARAMS)
    elif DEVICE == 2:
        DEVICES_IP = "172.16.2.4"
        DEVICE_PARAMS = {'device_type': 'cisco_ios',
                         'ip': DEVICES_IP,
                         'username': USER,
                         'password': PASSWORD, }
        ssh = ConnectHandler(**DEVICE_PARAMS)
    elif DEVICE == 3:
        DEVICES_IP = "172.16.2.5"
        DEVICE_PARAMS = {'device_type': 'cisco_ios',
                         'ip': DEVICES_IP,
                         'username': USER,
                         'password': PASSWORD, }
        ssh = ConnectHandler(**DEVICE_PARAMS)
    elif DEVICE == 4:
        break
    else:
        print("""
        Нет такого :)
        """)
        continue


    def port_discovery():
        PORT_LOOKING = ssh.send_command("sh int status | i " + INVENTORY)
        PORT_LOOKING = PORT_LOOKING.split()
        PORT_LOOKING = PORT_LOOKING[0]
        PORT_LOOKING = 'interface ' + PORT_LOOKING
        SHOW = ssh.send_command("sh run " + PORT_LOOKING)
        print(SHOW)
        return PORT_LOOKING
        # ищет порт по инвентарнику и выводит его на экран


    number = ''

    while number != '6':
        print("""
        1. Изменить количество разрешенных mac-адресов на порту
        2. Выключить порт
        3. Вывести информацию о настройках порта
        4. Включить порт        
        5. Поменять ПК/Телефон на порту
        6. Вернуться в меню выбора устройств
        """)

        number = int(input("Что вы хотите сделать?: "))

        if number == 1:
            INVENTORY = input("Введите инвентарный номер устройства(только цифры): ")
            PORT = port_discovery()
            MAX_MAC = input("Введите количество разрешенных mac-адресов на порту : ")
            COMMANDS = [PORT,
                        "switchport port-security maximum " + MAX_MAC]
            RESULT = ssh.send_config_set(COMMANDS)
            SHOW = ssh.send_command("sh run " + PORT)
            print(SHOW)
            print(input("Нажмите Enter"))

        elif number == 2:
            print("""
            
            ----------------------
            Очищает port-security.
            Убирает описание.
            Выключает PoE.
            Выключает сам порт.
            ----------------------
            
            """)
            INVENTORY = input("Введите инвентарный номер устройства(только цифры): ")
            PORT = port_discovery()
            CLEAR_PORT = ssh.send_command("clear port-sec sti " + PORT)
            COMMANDS = [PORT,
                        "switchport port-security maximum 1",
                        "no description",
                        "power inline never",
                        "shutdown"]
            RESULT = ssh.send_config_set(COMMANDS)
            SHOW = ssh.send_command("sh run " + PORT)
            print(SHOW)
            print(input("Нажмите Enter"))

        elif number == 3:
            INVENTORY = input("Введите инвентарный номер устройства(только цифры): ")
            port_discovery()
            print(input('Нажмите Enter'))

        elif number == 4:
            INVENTORY = input("Введите номер порта(Например: 1/0/1): ")
            PORT = "interface g" + INVENTORY
            SHOW = ssh.send_command("sh run " + PORT)
            print(SHOW)
            print(input('Нажите Enter'))
            MAX_MAC = input('Введите количество разрешенных mac-адресов на порту: ')
            DESC = input('Введите описание(инвентарный номер устройства): ')
            PoE = ()
            while PoE != 'yes' and 'no':
                PoE = (str(input('Нужно ли PoE на порту?(yes/no): ')))
                if PoE == 'no':
                    POWER = "power inline never"
                elif PoE == 'yes':
                    POWER = "power inline static max 4000"
                else:
                    print('Пожалуйста, введете yes или no')
                    continue


            COMMANDS = [PORT,
                        "switchport mode access",
                        "switchport access vlan 100",
                        "switchport voice vlan 112",
                        "switchport nonegotiate",
                        "description " + DESC,
                        "switchport port-security mac-address sticky",
                        "switchport port-security maximum " + MAX_MAC,
                        "switchport port-security",
                        "ip arp inspection limit rate 100",
                        "spanning-tree bpduguard enable",
                        "no shutdown",
                        POWER]
            RESULT = ssh.send_config_set(COMMANDS)
            SHOW = ssh.send_command("sh run " + PORT)
            print(SHOW)
            print(input("Нажмите Enter"))

        elif number == 5:
            print("""
            
            ------------------------------------
            Очищает port-security.
            Запрашивает ввод описания для порта.
            ------------------------------------
                                         
            """)
            INVENTORY = input("Введите инвентарный номер устройства(только цифры): ")
            PORT = port_discovery()
            clear_port = ssh.send_command("clear port-sec sti " + PORT)
            DESC = input('Введите описание для порта: ')
            COMMANDS = [PORT,
                        "description " + DESC,
                        ]
            RESULT = ssh.send_config_set(COMMANDS)
            SHOW = ssh.send_command("sh run " + PORT)
            print(SHOW)
            print(input("Нажмите Enter"))
        elif number == 6:
            break

        else:
            print("""
            Нет такого :)
            """)






