# HW02
# Class: Introduction to Data Structures and Algorithms - 16:198:512:03
# Professor: Dr. Kreutzer
# Fall 2025
# Author: Ali Vaziri


##############################
# Question 1:
def toInt(s):

    if s == "": # Base case: if the string is empty, return 0
        return 0
    else:
        last_digit = ord(s[-1]) - ord('0')  # Get the last character and convert it to int value
        return toInt(s[:-1]) * 10 + last_digit # Recursive call for the remaining string


# Q1 - Test case:
print("Q1 - Test case:")
test_string = "2375"
print(toInt(test_string))
##############################

# Question 2:
def sumString(n):

    if n == 1: # Base case
        return "1"
    else:
        return sumString(n - 1) + "+" + str(n)


# Q2 - Test case:
print("Q2 - Test case:")
test_value = 5
print(sumString(test_value))
##############################

# Question 3:
def rearrange(L, k):

    if len(L) <= 1: # rearrange L so that all values < k appear before values >= k , in place.
        return L
    p_recursive(L, k, first=0, last=len(L) - 1)
    return L


def p_recursive(A, k, first, last):

    if first >= last: # Base case is pointers, [first for (front) and last for (back)], meet or cross.
        return

    if A[first] < k: # If the front item already belongs to the left side, advance first
        p_recursive(A, k, first + 1, last)
    else:
        A[first], A[last] = A[last], A[first] # A[first] >= k --> swap it to the back and shrink from the right
        p_recursive(A, k, first, last - 1)


# Q3 - Test case:
print("Q3 - Test case:")
print(rearrange([3, 4, 8, 9, 5, 2], 8))
print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))
print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))
##############################

# Question 4:
def figure(n, current=1):
    if current > n: # Base case: stop when current is bigger than n
        return
    print('X' * current)
    figure(n, current + 1) # recursive call for the next row


# Q4 - Test case:
print("Q4 - Test case:")
n = 5
figure(n)
##############################

# Question 5:
def climbCount(n):

    if n == 0: # Base cases
        return 1
    if n < 0:
        return 0

    return climbCount(n - 1) + climbCount(n - 2) + climbCount(n - 3) # Recursive; try step 1, 2, or 3.


# Q5 - Test case:
print("Q5 - Test case:")
n = 4
print(climbCount(n))
##############################

# Question 6:
"""
To generate all arrangements of “abcd” from the arrangements of the shorter string “abc”, I follow the same recursive design we used in class, grow the problem from a smaller solved instance to the next size up, and combine the results systematically. 
For instance, I already have every unique permutation of “abc”. Each of those length-3 strings provides a frame where I can insert the new letter “d”. For a string of length 3, there are 4 insertion slots:
before index 0,
between 0–1,
between 1–2,
after index 2.

By inserting “d” into each of those four positions for every permutation of “abc,” I obtain all permutations of “abcd”, without missing any and without duplicates.
For example, starting from “abc,” the four insertions give dabc, adbc, abdc, and abcd. Doing the same operation for acb, bac, bca, cab, and cba produces four new strings from each:

From abc we get: dabc, adbc, abdc, abcd
From acb we get: dacb, adcb, acdb, acbd
From bac we get: dbac, bdac, badc, bacd
From bca we get: dbca, bdca, bcda, bcad
From cab we get: dcab, cdab, cadb, cabd
From cba we get: dcba, cdba, cbda, cbad

collecting them all 6 x 4 = 24 permutations, which is 4! results.
Generally, if I already have all (n−1)! permutations of a length (n−1) string, inserting the Nth letter into each of the n possible positions across all those strings n x (n−1)! = n! permutations. That’s exactly why this “insert in every position” construction is both complete and non-redundant.
"""