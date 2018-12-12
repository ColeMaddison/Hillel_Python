# **Задача-6 (Не обязательно, для тех кто скучает)
# You would like to set a password for a bank account. However, there are three restrictions on the 
# format of the password:
#  1) it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#  2) there should be an even number of letters;
#  3) there should be an odd number of digits.
# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, 
# and removing, the spaces.
# The goal is to choose the longest word that is a valid password.
# You can assume that if there are K spaces in string S then there are exactly K + 1 words.
# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: 
# "5", "a0A" and "pass007".
# Thus the longest password is "pass007" and its length is 7.
# Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character 
# and "test" contains an even number of digits (zero).

from re import match, findall
from string import ascii_letters, digits

string = "test 5 a0A pass007 ?xy1"

# solution 1
def validate_pass_1(string):
    matched = []
    for s in string.split(' '):
        letters = 0
        nums = 0
        for symbol in s:
            if symbol in ascii_letters:
                letters += 1
            elif symbol in digits:
                nums += 1
        if letters%2 == 0 and nums%2 == 1 and match('[0-9a-zA-Z]', s):
            matched.append(s)
    return matched


# solution 2
def validate_pass_2(string):
    return [s for s in string.split(' ') if len(findall('[0-9]', s))%2 == 1 and len(findall('[a-zA-Z]', s))%2 == 0 and match('[0-9a-zA-Z]', s)]

print(validate_pass_1(string))
print(validate_pass_2(string))