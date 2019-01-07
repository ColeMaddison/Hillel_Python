# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

import re

string_1 = 'hello 1 one two three 15 world'
string_2 = '1 23'
string_3 = 'hello 1 one two three four five 15 world'

def find_consecutive_words(string):
    return True if len(re.findall(r'\b\w[a-zA-Z]+\b \b\w[a-zA-Z]+\b \b\w[a-zA-Z]+\b', string)) else False

print(find_consecutive_words(string_1))
print(find_consecutive_words(string_2))
print(find_consecutive_words(string_3))