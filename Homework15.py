# Task1

reserved = ["admin","root"]
users = {
    'username':None, 'email': None, 'password': None, 'phone_number': None
}
list = []
users_count = input("enter quantity of users: ")
if users_count.isdigit():
        for i in range(int(users_count)):
            for key in users.keys():
                if key == "username":
                     username = input("enter username: ")
                     if len(username) > 5 and len(username) < 20 and username.isalnum() and username.lower()  not in reserved:
                          users["username"] = username
                     else:
                          print("Should be between 5 and 20 characters long.Can only contain alphanumeric characters.Should not be a reserved name")
                          break
                elif key == "email":
                     email = input("enter email: ")
                     if "@" in email and not email.startswith("@") and not email.endswith("@"):
                          users["email"] = email
                     else:
                        print("Should have a valid email format (e.g., user@example.com).")
                        break
                elif key == "password":
                     password = input("enter password: ")
                     sign = [i for i in password if i in "!@#$%^&*"]
                     isuppercase = [j for j in password if ord(j) > 65 and ord(j) < 97]
                     islowercase = [k for k in password if ord(k) > 97 and ord(k) < 122]
                     repeat_password = input("repeat password: ")
                     if len(password) >= 8:
                        if sign and isuppercase and islowercase:
                            if password == repeat_password:
                                users["password"] = password
                            else:
                                print("repeat password is incorrect")
                                break
                        else:
                            print("incorrect password")
                            break
                     else:
                        print("Should be at least 8 characters long.Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).")
                        break
                elif key == "phone_number":
                    phone_number = input("enter phone_number: ")
                    if phone_number.isdigit() and phone_number.startswith("0") or phone_number.startswith("+"):
                        users["phone_number"] = phone_number
                    else:
                        print("The number should only contain digits, with optional ‘+’ at the beginning")
                        break 
            list.append(users.copy())
            print(list)
else:
    print("quantity must be valid number")
    exit()

# Task2
# Implementation of Set Functions 

set1 = {1,2,3,4,6,10,12}
set2 = {4,5,12,6,1,2}

# union()

union_set = set()
for i in set1:
    union_set.add(i)
for i in set2:
    union_set.add(i)
print(union_set)

# intersection()

intersection = set()

for i in set1:
    if i in set2:
        intersection.add(i)
print(intersection)

# symetric_difference()

symetric_difference = set()

for i in set1:
    if not i in set2:
        symetric_difference.add(i)
for j in set2:
    if not j in set1:
        symetric_difference.add(j)
print(symetric_difference)

# difference()

set1_difference_set2 = set()
set2_difference_set1 = set()
for i in set1:
     if not i in set2:
          set1_difference_set2.add(i)
print(set1_difference_set2) 
for j in set2:
     if not j in set1:
          set2_difference_set1.add(j)
print(set2_difference_set1)
