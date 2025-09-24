def findDuplicate(arr):
    find = [False] * len(arr)
    result = []

    for num in arr:

        if num < 1 or num > len(arr) - 1:  # values in range 1 ... n-1
            raise ValueError("Number out of range")

        if find[num]:
            result.append(num)
            if len(result) == 2:
                return result
        else:
            find[num] = True

    return result


array1 = [1, 2, 2, 4, 4]
print(findDuplicate(array1))

array2 = [1, 2, 3, 4, 4, 5, 6, 7, 5]
print(findDuplicate(array2))

'''
Output:
[2, 4]
[4, 5]
'''