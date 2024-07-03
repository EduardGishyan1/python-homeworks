# Task1

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# transposed = [[0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transposed[j][i] = matrix[i][j]

# print(transposed)

# Task2

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# for i in range(len(matrix) - 1, -1, -1):
#     for j in range(len(matrix[i]) - 1, -1, -1):
#         if j == 0:
#             print(matrix[i][j])
#         else:
#             print(matrix[i][j], end=' ')
