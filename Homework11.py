# Task1

# index = 2
# value = 3
# list = [1,2,4,5]
# new_list = []
# for i in range(len(list)):
#     if i == index:
#         new_list.append(value)
#     new_list.append(list[i])
# print(new_list)

# Task2

# remove = 2
# ls = [1,2,3,2,4,5]
# new_ls = []
# one = False
# for j in ls:
#     if remove in ls:
#         if j == remove and not one:
#             one = True
#         else:
#             new_ls.append(j)
#     else:
#         print("No")
# print(new_ls)

# Task3 

# list = [1,2,3,5,6,7,8,10,12,23,4,5]
# new_list = []
# for i in range(len(list)):
#     if len(list) - 1 == i:
#         print(list[i])
#     else:
#         new_list.append(list[i])
# print(new_list)

# Task4

# list = [1,2,3]
# while len(list) > 0:
#     list.pop()
# print(list)


# Task5

# ls = [x**2 for x in range(1,11)]
# print(ls)

# Task6

# ls = [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]if i % 2 == 0] # Karox enq nayev grel i & 1 == 0
# print(ls)

x = b"hello"
print(type(x.decode()))
a = "hello"
a.encode()
print(a)
print(type(a))
# print(bytearray(a))