# # Question 3:
# def rearrange(L, k):
#
#     if not L: # Base case is empty list
#         return []
#
#     first = L[0]
#     rest = L[1:]
#
#     if first < k:
#         return [first] + rearrange(rest, k) # Place it in front, then recurse
#     else:
#         return rearrange(rest, k) + [first] # Place it at the back, after recursion
#
#
# # Q3 - Test cases:
# print("Q3 - Test cases:")
# print(rearrange([3, 4, 8, 9, 5, 2], 8))  # [3, 4, 2, 5, 9, 8]
# print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))  # [3, 4, 5, 2, 9, 8, 8, 8]
# print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))  # [1, 2, 6, 7, 3, 4, 8]


# # Question 3 (Professor's expected version):
# def rearrange(L, k):
#
#     if not L: # Base case is empty list
#         return []
#
#     first = L[0]
#     rest = L[1:]
#
#     if first < k:
#         return rearrange(rest, k) + [first] # put smaller element at the front, then recurse
#     else:
#         return [first] + rearrange(rest, k) # put larger element at the back, after recursion
#
#
# # Q3 - Test cases:
# print("Q3 - Test cases:")
# print(rearrange([3, 4, 8, 9, 5, 2], 8))  # [3, 4, 2, 5, 9, 8]
# print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))  # [2, 5, 3, 4, 9, 8, 8, 8]
# print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))  # [2, 1, 6, 7, 3, 4, 8]


# # Question 3 (Correct version, matches professor):
# def rearrange(L, k):
#
#     if not L:  # Base case is empty list
#         return []
#
#     first = L[0]
#     rest = L[1:]
#
#     if first < k:
#         return [first] + rearrange(rest, k) # put smaller element at the front, then recurse
#     else:
#         return rearrange(rest, k) + [first] # put larger element at the back, after recursion
#
#
# # Q3 - Test cases:
# print("Q3 - Test cases:")
# print(rearrange([3, 4, 8, 9, 5, 2], 8))  # [3, 4, 2, 5, 9, 8]
# print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))  # [2, 5, 3, 4, 9, 8, 8, 8]
# print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))  # [2, 1, 6, 7, 3, 4, 8]


# # Question 3: rearrange using recursion (no loops, no slicing).
# # Move all values < k to the front, and all values >= k to the back.
# # This version mutates L in place and also returns it.
#
# def rearrange(L, k):
#     def _partition(S, start, stop):
#         # Base case: when pointers meet or cross, we are done
#         if start >= stop:
#             return
#         # If the front element is already < k, keep it and move start forward
#         if S[start] < k:
#             _partition(S, start + 1, stop)
#         else:
#             # S[start] >= k: swap it with the element at 'stop' and shrink from the right
#             S[start], S[stop] = S[stop], S[start]
#             _partition(S, start, stop - 1)
#
#     if len(L) <= 1:
#         return L
#     _partition(L, 0, len(L) - 1)
#     return L
#
#
# # Q3 - Test cases (should match professor's examples exactly):
# print("Q3 - Test cases:")
# print(rearrange([3, 4, 8, 9, 5, 2], 8))            # -> [3, 4, 2, 5, 9, 8]
# print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))      # -> [2, 5, 3, 4, 9, 8, 8, 8]
# print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))         # -> [2, 1, 6, 7, 3, 4, 8]


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
print(rearrange([3, 4, 8, 9, 5, 2], 8))           # -> [3, 4, 2, 5, 9, 8]
print(rearrange([8, 8, 3, 4, 8, 9, 5, 2], 8))     # -> [2, 5, 3, 4, 9, 8, 8, 8]
print(rearrange([8, 7, 6, 1, 2, 3, 4], 3))        # -> [2, 1, 6, 7, 3, 4, 8]
