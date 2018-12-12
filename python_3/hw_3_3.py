# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все

from re import search

string_1 = "..,   word"
string_2 = "word."
string_3 = " let's go"
string_4 = "go"

def get_first_word(string):
    return search(r"[\w]+'?[\w]+", string)[0]


print(get_first_word(string_1))
print(get_first_word(string_2))
print(get_first_word(string_3))
print(get_first_word(string_4))