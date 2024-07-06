# Task1

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# union = set1.union(set2)
# print(union)

# intersection = set1.intersection(set2)
# print(intersection)

# symmetric_difference = set1.symmetric_difference(set2)
# print(symmetric_difference)

# Task2

# users = {
#     '1': {'ID': '1', 'first_name': 'James', 'last_name': 'Doe', 'email': 'python@example.com', 'password': 'password123', 'phone_number': '1234567890'},
#     '2': {'ID': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'py@example.com', 'password': 'securepwd', 'phone_number': '0987654321'},
#     '3': {'ID': '3', 'first_name': 'Ann', 'last_name': 'Williams', 'email': 'pyth@example.com', 'password': 'mysecretpw', 'phone_number': '5555555555'}
# }

# first_name = input("enter your name: ")
# last_name = input("enter last_name: ")
# found_user = None
# for id,info in users.items():
#     if info['first_name'] == first_name and info['last_name'] == last_name:
#         found_user = info
# if found_user:
#     print("User found")
#     print(f"ID: {found_user['ID']}")
#     print(f"first_name: {found_user['first_name']}")
#     print(f"last_name: {found_user['last_name']}")
#     print(f"email: {found_user['email']}")
#     print(f"password: {found_user['password']}")
#     print(f"phone_number: {found_user['phone_number']}")
# else:
#     print("Not found")