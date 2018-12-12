# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке 
# как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все 
# заглавные буквы, то получим сообщение "HELLO".


text = "How are you? Eh, ok. Low or Lower? Ohhh."

def upper_case_word(text):
    return  ''.join([i for i in text if i.isupper()])

print(upper_case_word(text))