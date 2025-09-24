def reverseMe(stack):
    temp1 = []
    temp2 = []

    while stack:
        temp1.append(stack.pop())  # Move stack to temp1

    while temp1:
        temp2.append(temp1.pop())  # Move temp1 to temp2

    while temp2:
        stack.append(temp2.pop())  # Move back temp2 to stack


# checking the output:
s = [1, 2, 3, 4, 5]
print("Before reverse:", s)

reverseMe(s)
print("After reverse: ", s)
'''
Output is:
Before reverse: [1, 2, 3, 4, 5]
After reverse:  [5, 4, 3, 2, 1]
'''