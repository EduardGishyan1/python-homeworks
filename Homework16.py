# Task 1

# x = open("append_mode.txt",mode="a+")
# x.write("\tHello world")
# x.close()

# Task 2

# try:
#     x = open("exclusive_mode.txt",mode="x")
#     x.write("Hello")
# except FileExistsError:
#     print("file is already exists")

# x.close()

# Task 3

# filename = 'specific_position.txt'
# text = "Hello\n"

# try:
#     file = open(filename, 'r+')
#     content = file.read()
#     if not content:
#         file.write(text)
#         print(f"Text '{filename}'")

#     file.seek(24) 
#     file.write("Hello world")

# except FileNotFoundError:
#     file = open(filename, 'w')
#     file.write(text)
#     print(f"File '{filename}'")

# file.close()

# Task 4

# dict = {}
# try:
#     fs = open("count_word.txt",mode="w+")
#     fs.write("example\nall\nword\nup\ndid\nhim\nhim")
#     fs.seek(0)
#     for i in fs:
#         if i.strip() in dict:
#             dict[i.strip()] += 1
#         else:
#             dict[i.strip()] = 1
#     print(dict)
# except FileNotFoundError:
#     print("file not found")

# fs.close()
