# print("Hi !")

# in the Terminal type:
# python SelfPractice01.py
# python -i SelfPractice01.py

# Notice: you should be in the same directory of .py code

# print(hash("a"))
# print(hash("B-"))
#
# hash("Look at me!")
# f = "Look at me!"
# print(hash(f))

# n=10
# for i in range(n):
#     print(i)  # O(n)

# while n > 1:
#     n = n // 2   # log n

# temperature = 98.06
# original = temperature
#
# print(temperature)
# print(" ")
# print(original)
#
# print("================")
#
# # temperature = temperature + 98.06
# #
# # print(temperature)
# # print(" ")
# # print(original)

# # empty tuple
# t0 = ()
# print(t0, type(t0))   # () <class 'tuple'>
#
# # one-element tuple
# t1 = (17,)
# print(t1, type(t1))   # (17,) <class 'tuple'>
#
# # just a number in parentheses
# t2 = (17)
# print(t2, type(t2))   # 17 <class 'int'>

# print('Don\'t worry')
# print('C:\\Python\\') #invalid escape sequence '\P' print('C:\Python\\')
# print('20\u20AC')
# """ akjbsk
# sdlf]
# sdg"""

# # list
# L = [1, 2, 2, 3]
# print(L)   # [1, 2, 2, 3]

# # set
# S = {1, 2, 2, 3, 8, 9, 5}
# print(S)   # {1, 2, 3}   (تکراری‌ها حذف شدند)
# S2 = {9, 1, 8, 3, 5, 7}
# print(S2)
#
# # frozenset
# F = frozenset([1, 2, 2, 3, 5, 5, 9, 3])
# print(F)   # frozenset({1, 2, 3})

# F = frozenset(["dog", "cat", "elephant", "ant"])
#
# print("hash dog:", hash("dog"))
# print("hash cat:",hash("cat"))
# print("hash elephant:", hash("elephant"))
# print("hash ant:", hash("ant"))
#
# print(F)

# t = (1, 2, 3)     # یک tuple
# #t.append(4)     # خطا می‌ده! چون tuple تغییرپذیر نیست

# x = int(5)
# y = float(3.14)
# print(x)
# print(y)
# y2 = int(3.14)
# print(y2)

# x = None
# # and: چون شرط اول False می‌شود، شرط دوم اصلاً بررسی نمی‌شود
# print(x is not None and x > 0)   # False
# # or: چون شرط اول True است، شرط دوم اصلاً بررسی نمی‌شود
# print(x is None or x > 0)        # True

# s1 = "hello"
# s2 = "hello"
# print(s1 == s2)  # True  (کاراکتر به کاراکتر یکی هستن)
# print(s1 is s2)  # True یا False (بسته به حافظه و cache پایتون)
#
# S1 = {1, 2, 3}
# S2 = {3, 2, 1}
# print(S1 == S2)  # True  (چون محتوا یکسانه، ترتیب مهم نیست)
# print(S1 is S2)  # False (چون دو شیء متفاوت هستن)
#
# a = 1000
# b = 1000
# print(a == b)   # True  (چون مقدارشون یکیه)
# print(a is not b)   # False (چون دو شیء جدا در حافظه هستند)

# print(7/2)
# print(7//2)