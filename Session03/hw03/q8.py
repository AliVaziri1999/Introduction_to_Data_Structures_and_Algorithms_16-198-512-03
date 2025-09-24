# def rearrange_iter(S, k):
#     i, j = 0, len(S) - 1
#     while i <= j:
#         if S[i] < k:
#             i += 1                 # good element stays; move on
#         else:
#             S[i], S[j] = S[j], S[i]  # move bad element to the right side
#             j -= 1                  # right region shrinks
#     # in-place; no return needed


def rearrange_iter(L, k):
    i, j = 0, len(L) - 1

    while i <= j:
        if L[i] < k: # element stays on left
            i += 1
        else:
            L[i], L[j] = L[j], L[i] # swap with right side
            j -= 1 # shrink right boundary
    return L

# test case (same arrays from hw2 q3 to comparison)
print(rearrange_iter([3, 4, 8, 9, 5, 2], 8))
print(rearrange_iter([8, 8, 3, 4, 8, 9, 5, 2], 8))
print(rearrange_iter([8, 7, 6, 1, 2, 3, 4], 3))
'''
output:
[3, 4, 2, 5, 9, 8]
[2, 5, 3, 4, 9, 8, 8, 8]
[2, 1, 6, 7, 3, 4, 8]
'''