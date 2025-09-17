# Author: Ali Vaziri
# HW02

##############################
# Questions
##############################
# Question 1:
def toInt(s):

    if s == "": # Base case: if the string is empty, return 0
        return 0
    else:
        last_digit = ord(s[-1]) - ord('0')  # Get the last character and convert it to int value
        return toInt(s[:-1]) * 10 + last_digit # Recursive call for the remaining string

##############################

# Question 2:
def sumString(n):

    if n == 1: # base case
        return "1"
    else:
        return sumString(n - 1) + "+" + str(n)

##############################

# Question 3:

##############################

# Question 4:
def print_figure(n, current=1):
    if current > n: # Base case: stop when current is bigger than n
        return
    print('X' * current)
    print_figure(n, current + 1) # recursive call for the next row

##############################



##############################
# Test cases for the functions
##############################
if __name__ == "__main__":

    # Q1 - Test case:
    test_string = "2375"
    result = toInt(test_string)
    print("Q1 - Test case:")
    print(result)


    # Q2 - Test case:
    test_value = 5
    result = sumString(test_value)
    print("Q2 - Test case:")
    print(result)


    # Q3 - Test case:
    print("Q3 - Test case:")


    # Q4 - Test case:
    print("Q4 - Test case:")
    n = 5
    print_figure(n)