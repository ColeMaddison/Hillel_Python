#Задача -2
# Описать задачу но уже с использованием @contexmanager

from contextlib import contextmanager
from os import chdir, getcwd

@contextmanager
def cd(file_path, exc):
    try:
        print(getcwd())
        yield chdir(file_path)
    except Exception as e:
        if(type(e).__name__ == exc.__name__):
            print('error caught')
            yield
        else:
            raise exc()
    finally:
        print(getcwd())
        print('finished')


with cd('./d1dd', FileNotFoundError):
    print('all fine')


