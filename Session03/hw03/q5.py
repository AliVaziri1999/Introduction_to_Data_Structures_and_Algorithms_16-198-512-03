def delete_last_n(data, value, n):
    write = len(data) - 1  # pointer starts at the end
    removed = 0  # count how many we removed

    for read in range(len(data) - 1, -1, -1):  # start from right to left
        if data[read] == value and removed < n:
            removed += 1
        else:
            data[write] = data[read]
            write -= 1

    for i in range(write + 1):  # remove extra front
        data.pop(0)

    return data


data1 = [1, 2, 3, 4, 3, 3, 5, 3]
print(delete_last_n(data1, 3, 2))
'''
Output is:
[1, 2, 3, 4, 3, 5]
'''