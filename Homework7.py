#Task1    

# list = ["hello", "bye", "python", "language"]
# max_length = len(list[0])
# max_index = 0

# for i in range(len(list)):
#     length = len(list[i])
#     if length > max_length:
#         max_length = length
#         max_index = i

# print(list[max_index])
# print(max_index)
# print(max_length)

# Task2

# list = ["hello", "bye", "python", "language"]
# for i in range(len(list)):
#     list[i] = list[i][0].upper()
#     print(list[i])

# Task3

# list = [1,2,3,["Hello"],True,False]
# i = len(list)
# list2 = []
# while i > 0:
#     i -= 1 
#     list2.append(list[i])
# print(list2)

# Task 4

# list = [1,2,3,4,5,6,7,8,9,13,14,16,21]
# inp = input("Write number: ")
# if int(inp) in list:
#     print("Yes")
# else:
#     print("No")

# Task 5

# list = ["hello", "bye", "python", "language","python", "language"]
# x = {}
# for i in list:
#     if i in x:
#         x[i] += 1
#     else:
#         x[i] = 1 
# print(x)

# Task 6

# ls = [1,2,3,4,5,6,7,8,9,10]
# odd= []
# even = []
# for i in ls:
#     if i % 2 == 0:
#         even += [i]
#     else:
#         odd += [i]
# ls = odd + even 
# print(ls)

# Task 7

# inp = int(input("Enter the size: "))
# input_list = []

# for i in range(inp):
#     element = int(input("Write element: "))
#     input_list.append(element)

# for j in input_list:
#     print(j)
