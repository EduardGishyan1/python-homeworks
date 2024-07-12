# Task1

# def foo(n):
#     if n >= 0:
#         print(n)
#         foo(n-1)
# foo(10)

# Task2

# def foo(n):
#     if type(n) == int and n > 0:
#         for i in range(n):
#             print(i)
#     else:
#         print("argument must be a valid number")
# foo(-5)

# Task3

# def foo(ls):   
#     if ls:
#         if type(ls) == list:
#             for i in ls:
#                 print(i)
#         else:
#             print("argument must ba a list")
#     else:
#         print("list must be valid")
# foo([1,2,3,4,5])

# Task4

# def foo(num):
#     try:
#         sum = 0
#         for i in str(num):
#             sum += int(i)
#         print(sum)
#     except:
#         print("argument must be a digit")
# foo(123)

# Task5

# def foo(str):
#     found = False
#     try:
#         for i in str:
#             if ord(i) >= 65 and ord(i) <= 90:
#                 print(i)
#                 found = True
#                 break
#         if not found:
#             print("No uppercase letter")
#     except:
#         print("argument must be a string")

# foo("thjHjh")

# Task6

# def foo(ls):
#     try:
#         max_number = ls[0]
#         min_number = ls[0]

#         for i in ls:
#             if i > max_number:
#                 max_number = i
#             if i < min_number:
#                 min_number = i
#         print(f"max number is {max_number}")
#         print(f"min number is {min_number}")
#     except:
#         print("Lists elements must be a digit")

# foo([1,2,3,4])