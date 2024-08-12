# Task1

# def flatten_list(nested_list):
#     flattened = []
#     for element in nested_list:
#         if isinstance(element, list):
#             flattened.extend(flatten_list(element)) 
#         else:
#             flattened.append(element)
#     return flattened

# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# flattened = flatten_list(nested_list)
# print(flattened)

# Task2

# def foo(ls):
#     if not ls:
#         return 0
#     return ls[0] + foo(ls[1:])
# print(foo([1,2,3,4,5]))

# Task3

# def foo(ls):
#     if len(ls) == 1:
#         return True
#     if ls[0] > ls[1]:
#         return False
#     return foo(ls[1:])
# print(foo([1,2,3,4,10,14]))

# Task4

# def prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     return check(n,2)
# def check(n,i):
#     if i * i > n:
#         return True
#     elif n % i == 0:
#         return False
#     return check(n,i+1)
# print(prime(17))

# Task5

# def max(a,b,c):
#     def max_two(a,b):
#         if a > b:
#             return a
#         return b
#     def max_of_three(a,b,c):
#         return max_two(a,max_two(b,c)) 
#     return max_of_three(a,b,c)
# print(max(1,2,3))      

# Task6

# def fibonnaci(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0,1]
#     fibs = fibonnaci(n-1)
#     fibs.append(fibs[-1] + fibs[-2])
#     return fibs
# print(fibonnaci(5))

# Task7

# def power(n):
#     if n == 1:
#         return True
#     if n % 2 != 0 or n == 0:
#         return False
#     return power(n//2)
# print(power(6))
