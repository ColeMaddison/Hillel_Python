# Определить свой класс Exception который будет записывать месседж ошибки в файл. Тоесть при возникновении 
# ошибки вам нужно писать ее в файл а не выводить. Как пример вызова вашего функционала используйте пример 
# ниже:

# can be done with logging module

class Exc(Exception):
    def __init__(self, arg):
        self.args = arg

    def log_to_file(self, file_name):
        with open('./python_13/{}'.format(file_name), 'a+') as f:
            f.write('Error occured: {}\n'.format(str(self.args)))

try:
    raise Exc("Bad error")
except Exc as e:
    e.log_to_file('errors.txt')



