# Task1

# ls = [1,2,3,4,5,6,7,8]
# ls2 = [1,2,3,4,5,6,7,8]
# check = True
# for i in range(len(ls)):
#         if ls[i] == ls2[i]:
#             check = True
#         else:
#             check = False
#             break
# if check:
#      print("arjeqnery nuynn en")
# else:
#     print("arjeqnery tarber en")

# Task2


# size = int(input("Enter size: "))
# ls = []

# for i in range(size):
#     element = input("Enter element: ")
#     if element.isdigit():
#         element = int(element)
#         ls.append(element)
#     else:
#         print("Please enter valid integers only.")
#         break 

# if len(ls) == size:
#     max_number = ls[0]
#     min_number = ls[0]

#     for num in ls:
#         if num > max_number:
#             max_number = num
#         if num < min_number:
#             min_number = num

#     max_value_index = ls.index(max_number)
#     min_value_index = ls.index(min_number)
#     difference = max_value_index - min_value_index
#     print(difference)

# Task3

# elements = input("grir tver anjatelov bacatnerov: ")
# elements_list = elements.split()
# for element in elements_list:
#     print(element)


# Task 4

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# size = len(matrix)
# for i in range(size):
#     j = size - 1 - i
#     matrix[i][i], matrix[i][j] = matrix[i][j], matrix[i][i]

# for row in matrix:
#     print(row)

# Task 5

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# size = len(matrix)
# sum = 0
# for i in range(size):
#     sum += matrix[i][i]
# print(sum)

# Task 6

# matrix = [
#     [1,2,3],
#     [4,8,6],
#     [7,8,9],
# ]
# size = len(matrix)
# sum = 0
# for i in range(size):
#     j = size - 1 - i
#     sum += matrix[i][j]
# print(sum)

# Task 7

# matrix = [
#     [1,2,3],
#     [4,15,6],
#     [1713,8,29]
# ]
# max_number = matrix[0][0]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > max_number:
#             max_number = matrix[i][j]
# print(max_number)