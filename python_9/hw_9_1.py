# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

ip_list = ['192.168.1.1', '192.168.0.1', '192.168.1.254', '10.0.0.138', '192.168.1.1', '192.168.1.10.1']

class IPMagager(object):
    def __init__(self, ip_list):
        self.ip_list = ip_list

    def get_ip_list(self):
        print(self.ip_list)

    def get_ip_list_reversed(self):
        print([i[::-1] for i in self.ip_list])

    def get_ip_list_cut_two(self):
        print(['.'.join(i.split('.')[1:]) for i in self.ip_list])
    
    def get_ip_list_last_octet(self):
        print([i.split('.')[-1] for i in self.ip_list])

manage = IPMagager(ip_list)

manage.get_ip_list()
manage.get_ip_list_reversed()
manage.get_ip_list_cut_two()
manage.get_ip_list_last_octet()