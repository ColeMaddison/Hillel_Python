# descriptors  - управляемое поведение методов
# meta classes

# class Proxy:
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, owner):
#         self.value = value

# class Smth:
#     attr = Proxy()

#  @staticmethod - just func in class - not using self

# meta classes - класс type который создает другие классы

# name, bases, attrs = 'Smth', (w), {'attr': 42}
# Smth = type(name, bases, attrs)
# Some = Smth()
# print(Some)