# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class SwitchParams(object):
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.unit_name = unit_name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.login = login
        self.password = password

    # unit name
    @property
    def get_unit_name(self):
        print(self.unit_name)

    @get_unit_name.setter
    def get_unit_name(self, val):
        self.unit_name = val
        print('Unit name set to: {}'.format(val))

    # mac address
    @property
    def get_mac_address(self):
        print(self.mac_address)

    @get_mac_address.setter
    def get_mac_address(self, val):
        self.mac_address = val
        print('Unit name set to: {}'.format(val))

    # ip address
    @property
    def get_ip_address(self):
        print(self.ip_address)

    @get_ip_address.setter
    def get_ip_address(self, val):
        self.ip_address = val
        print('Unit name set to: {}'.format(val))

    # login
    @property
    def get_login(self):
        print(self.login)

    @get_login.setter
    def get_login(self, val):
        self.login = val
        print('Unit name set to: {}'.format(val))

    # password
    @property
    def get_password(self):
        print(self.password)

    @get_password.setter
    def get_password(self, val):
        self.password = val
        print('Unit name set to: {}'.format(val))

switcher = SwitchParams(1,1,1,1,1)

switcher.get_ip_address
switcher.get_login
switcher.get_mac_address
switcher.get_password
switcher.get_unit_name

switcher.get_ip_address = 2
switcher.get_login = 2
switcher.get_mac_address = 2
switcher.get_password = 2
switcher.get_unit_name = 2

switcher.get_ip_address
switcher.get_login
switcher.get_mac_address
switcher.get_password
switcher.get_unit_name

