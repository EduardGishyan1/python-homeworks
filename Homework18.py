# Task1

# def foo(n):
#     if n <= 0:
#         return

#     print(n)
#     foo(n-1)

# foo(5)

# Task2

# def foo(n):
#     if n > 5:
#         return
#     foo(n+1)
#     print(n)
# foo(1)

# Task3

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# x = factorial(5)
# print(x)

# Task4

# def sum_numbers(num):
#     if num == 0:
#         return 0
#     return num + sum_numbers(num-1)
# x = sum_numbers(5)
# print(x)

# Task5

# def print_list(lst):
#     if not lst:  
#         return
#     else:
#         print(lst[0])  
#         print_list(lst[1:])

# print_list([1, 2, 3, 4, 5])

# Task6

# def length_of_list(lst):
#     if not lst:
#         return 0
#     else:
#         return 1 + length_of_list(lst[1:])

# length_of_list([1, 2, 3, 4, 5])

# Task7

# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# print(reverse_string("Hello"))

# Task8


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7))

# Task9

# def print_characters(string):
#     if not string: 
#         return
#     else:
#         print(string[0])
#         print_characters(string[1:])  

# print_characters("hello")

# Task10

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and is_palindrome(s[1:-1])

# print(is_palindrome("Hello"))

# Task11

# def sum_of_digits(num):
#     if num < 10:
#         return num
#     else:
#         return num % 10 + sum_of_digits(num // 10)

# print(sum_of_digits(12345))
