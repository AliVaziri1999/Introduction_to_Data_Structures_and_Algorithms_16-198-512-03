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
















# # Question 1
# def toInt(s):
#     # Base case: if the string is empty, return 0
#     # if not s:
#     if s == "":
#         return 0
#     else:
#         # Get the last character and convert it to its integer value
#         last_digit = ord(s[-1]) - ord('0')  # Convert character to integer
#         # Recursive call for the remaining string
#         return toInt(s[:-1]) * 10 + last_digit
#
#
#
# # Testing the function
# if __name__ == "__main__":
#     # Test cases
#     test_string = "2375"
#     result = toInt(test_string)
#     print(f"The integer value of the string '{test_string}' is: {result}")
#
#     test_string2 = "123456"
#     result2 = toInt(test_string2)
#     print(f"The integer value of the string '{test_string2}' is: {result2}")
#
#     test_string3 = "0"
#     result3 = toInt(test_string3)
#     print(f"The integer value of the string '{test_string3}' is: {result3}")
#
#     test_string4 = ""
#     result4 = toInt(test_string4)
#     print(f"The integer value of the string '{test_string4}' is: {result4}")