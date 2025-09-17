# Author: Ali Vaziri
# HW02

# Question 1:
def toInt(s):

    if s == "": # Base case: if the string is empty, return 0
        return 0
    else:
        last_digit = ord(s[-1]) - ord('0')  # Get the last character and convert it to int value
        return toInt(s[:-1]) * 10 + last_digit # Recursive call for the remaining string




# Test cases for the functions
if __name__ == "__main__":

    # Q1 - Test case:
    test_string = "2375"
    result = toInt(test_string)
    print(result)


    # Q2