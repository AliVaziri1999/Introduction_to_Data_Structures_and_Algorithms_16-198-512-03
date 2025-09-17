# Author: Ali Vaziri
# HW02

##############################
# Question 1:
def toInt(s):

    if s == "": # Base case: if the string is empty, return 0
        return 0
    else:
        last_digit = ord(s[-1]) - ord('0')  # Get the last character and convert it to int value
        return toInt(s[:-1]) * 10 + last_digit # Recursive call for the remaining string


# Q1 - Test case:
test_string = "2375"
result = toInt(test_string)
print("Q1 - Test case:")
print(result)
##############################

# Question 2:
def sumString(n):

    if n == 1: # Base case
        return "1"
    else:
        return sumString(n - 1) + "+" + str(n)


# Q2 - Test case:
test_value = 5
result = sumString(test_value)
print("Q2 - Test case:")
print(result)
##############################

# Question 3:


# Q3 - Test case:
print("Q3 - Test case:")
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

    # Recursive case: try 1, 2, or 3 steps
    return climbCount(n - 1) + climbCount(n - 2) + climbCount(n - 3)


# Q5 - Test case:

##############################