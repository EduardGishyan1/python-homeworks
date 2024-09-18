# Task1

# text = "find the letter z"

# for i in range(len(text)):
#     if text[i] == "z":
#         print(f"z: {i}")
#         break
# else:
#     print("Character not found")

# Task2

# capitalize = "capitalize"
# first = capitalize[0]
# x = chr(ord(first) - 32)
# capitalize = x + capitalize[1:]
# print(capitalize)

# Task3

# title = "hello, world! are you ready?"
# new_title = ""
# for i in title:
#     if ord(i) in range(97,122):
#         new_title += chr(ord(i) - 32)
#     else:
#         new_title+= i
# title = new_title
# print(title)

# Task4

# text = "reverse me"
# reverse = ""
# index = len(text) - 1
# while index != 0:
#     reverse += text[index]
#     index-=1
# print(reverse)

# Task5

# word = "radar"
# if word == word[::-1]:
#     print("Yes")
# else:
#     print("No")

# Task6

# word1 = "hello"
# word2 = "world"
# print(word1 + " " + word2)

# Task7

# text = "banana"
# new_text = ""
# for i in text:
#     if i == "a":
#         new_text += "x"
#     else:
#         new_text += i
# text = new_text
# print(text)

# Task8 

# sentence = "Hello world"
# words = sentence.split()
# longest_word = ""
# max_length = 0
# for word in words:
#     if max_length < len(word):
#         longest_word = word
#         max_length = len(word)
# print(longest_word)

# Task9

# s = "12soe3"
# s.split()
# for char in s:
#     if("0" <= char <= "9"):
#         print(char)


# Task 10

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


# Task11


# def x(n):
#     return str(n) == str(n)[::-1]

# def y(n):
#     steps = 0
#     while not x(n):
#         reversed_n = int(str(n)[::-1])
#         n += reversed_n
#         steps += 1
#     return steps

# Task12

# sentence = "Hello world"
# words = sentence.split()
# longest_word = ""
# max_length = 0
# for word in words:
#     if max_length < len(word):
#         longest_word = word
#         max_length = len(word)
# print(longest_word)

# Task13

# s = "12soe3"
# for char in s:
#     if char.isdigit():
#         print(char)


# Task 14

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


# Task 15

# def reverse(n):
#     return str(n) == str(n)[::-1]

# def reverse_int(n):
#     steps = 0
#     while not reverse(n):
#         reversed_n = int(str(n)[::-1])
#         n += reversed_n
#         steps += 1
#     return steps

# print(reverse(123))  
# print(reverse(555))  
# print(reverse(49))   
