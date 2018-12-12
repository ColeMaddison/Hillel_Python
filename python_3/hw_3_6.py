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

string = "test 5 a0A pass007 ?xy1"

def validate_pass(string):
    pass

print(validate_pass(string))