"""
3)Заменить в произвольной строке согласные буквы на гласные.
"""
import re
import random

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

text = 'Some tExt WIth different vOwels!..$'

def replace_vowels(text):
    changed_text = ''
    consonants_lower = [x.lower() for x in consonants]
    consonants_all = consonants_lower + consonants
    vowels_lower = [x.lower() for x in vowels]
    for i in text:
        if i in consonants_all:
            if i.islower():
                changed_text += random.choice(vowels_lower)
            else:
                changed_text += random.choice(vowels)
        else:
            changed_text += i
    return changed_text

print(replace_vowels(text))