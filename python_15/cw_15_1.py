class Des():
    def __get__(self, obj, type=None):
        print('Get was called')

    def __set__(self, obj, value):
        self.value = value
        print('Set was called')


class A():
    attr = Des()

a = A()

a.attr
a.attr = 10

class B():
    def __init__(self, param):
        self.param = param

    @property
    def name(self):
        print("Get from B is called")
        return self.param

    @name.setter
    def name(self, new_name):
        self.param = new_name
        print("Set from B is called")


b = B('DK')
b.name
b.name = 'RN'
b.name