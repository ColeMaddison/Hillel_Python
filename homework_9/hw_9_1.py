# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить

import re

class EmailDescriptor:
    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, value):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value) is not None :
            self.email = value
        else:
            raise ValueError("Email does not match requirements.")

class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
print(my_class.email)
my_class.email = "novalidemail"
