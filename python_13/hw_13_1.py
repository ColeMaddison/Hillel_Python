# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход. 
# Так же ваш объект должен принимать исключение которое он будет подавлять. Если флаг об исключении 
# отсутствует, исключение должно быть поднято.

from os import chdir

class cd(object):
    def __init__(self, file_path, exc=None):
        self.file_path = file_path
        self.exc = exc

    def __enter__(self):
        try:
            chdir(self.file_path)
        except Exception as e:
            if(type(e).__name__ == self.exc.__name__):
                print('error caught')
            else:
                raise self.exc()
    
    def __exit__(self, etype, value, traceback):
        print('finished')
        return True

with cd('./dd1d', FileNotFoundError):
    print('all fine')