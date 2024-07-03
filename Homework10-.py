# Task1

# sentence = "Hello world"
# words = sentence.split()
# longest_word = ""
# max_length = 0
# for word in words:
#     if max_length < len(word):
#         longest_word = word
#         max_length = len(word)
# print(longest_word)

# Task2

# s = "12soe3"
# s.split()
# for char in s:
#     if("0" <= char <= "9"):
#         print(char)


# Task 3

# def uppercase(string):

#     for i in string:
#         upper_string = ""
#         if i > "a" < "z":
#             upper_char = chr(ord(i) - 32)
#             upper_string += upper_char
#         else:
#             upper_char = i
#             upper_string += upper_char
#         print(upper_string)
# uppercase("Hello world")


# Task4

# def x(n):
#     return str(n) == str(n)[::-1]

# def y(n):
#     steps = 0
#     while not x(n):
#         reversed_n = int(str(n)[::-1])
#         n += reversed_n
#         steps += 1
#     return steps

# print(y(123))  
# print(y(555))  
# print(y(49))   