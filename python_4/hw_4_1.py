# TASK-1
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not 
# occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

a_1 = [1, 3, 6, 4, 1, 2]
a_2 = [1, 2, 3]
a_3 = [-1, -3]
a_4 = [-1000000]


def solution(a): 
    integer = 1
    for x in range(len(a) + 1): #needed +1 if the biigest in is the last
        if integer in a:
            integer += 1
        else:
            return integer


print(solution(a_1))
print(solution(a_2))
print(solution(a_3))
print(solution(a_4))