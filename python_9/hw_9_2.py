# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

import json
import os

class JSONManager(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def file_write(self, data, to_file=None):
        try:
            to_file = self.file_path if not to_file else to_file
            with open(to_file, 'a+', encoding='utf-8') as out:
                out.write(', \n') # to write trailing comma as a new dict and prevent error
                json.dump(data, out)
        except Exception as e:
            print(e)

    def file_read(self):
        try:
            with open(self.file_path, 'r') as fp:
                print(json.load(fp))
        except Exception as e:
            print(e)

    def file_combine(self,*args, out_file = '{}/hw_9_2_combined.json'.format(os.path.dirname(__file__))):
        for file in args:
            try:
                with open(file, 'r') as f:
                    self.file_write(out_file, json.load(f))
            except Exception as e:
                print(e)

file1 = JSONManager('./python_9/hw_9_2_json_1.json')

# file1.file_write({"a": 1})
# file1.file_read()
file1.file_combine('./python_9/hw_9_2_json_1.json', './python_9/hw_9_2_json_3.json', out_file='./python_9/hw_9_2_combined.json')