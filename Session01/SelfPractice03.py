# data = "HELLOXWORLD"
# j = 0
# while j < len(data) and data[j] != "X":
#     j += 1
#
# print(j)   # 5 (اندیس کاراکتر X)


# data = "123456789"
#
# c = 0
# while c < len(data) and  data[c] != "5":
#     c += 1
#
# print(c)

# data = [5, 8, 12]
# total = 0
# for val in data:
#     print("val:", val)
#     print("total:", total)
#     # total += val
#     total += val
# print(total)   # 25

# data = [7, 3, 9, 2, 15, 4]
# big_index = 0
# for j in range(len(data)):
#     if data[j] > data[big_index]:
#         big_index = j
#
# print("Max value =", data[big_index])  # 15
# print("Index =", big_index)            # 4

# data = [3, 7, 2, 9, 5]
# target = 9
# found = False
#
# for item in data:
#     if item == target:
#         found = True
#         break
#
# print(found)   # True

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue   # اگر زوج بود، این تکرار رو رد کن
#     print(i)

# def count(data, target):
#     n = 0
#     for item in data:
#         if item == target:   # اگر پیدا شد
#             n += 1
#     return n
#
# print(count([1,2,3,2,2,5], 2))   # خروجی: 3

