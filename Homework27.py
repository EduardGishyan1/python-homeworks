# Task1

# class Employee():
#     def __init__(self,employee_id,name,salary):
#         self.__employee_id = employee_id
#         self.__name = name
#         self.__validate_salary(salary)
#         self.__salary = salary
    
#     def __validate_salary(self,salary):
#         if salary < 0:
#             raise ValueError("Enter positive salary")

#     def set_employee_id(self,new_employee_id):
#         self.__employee_id = new_employee_id

#     def get_employee_id(self):
#         return self.__employee_id  


#     def set_name(self,new_name):
#         self.__name = new_name

#     def get_name(self):
#         return self.__name


#     def set_salary(self,new_salary):
#         self.__validate_salary(new_salary)
#         self.__salary = new_salary
    
#     def get_salary(self):
#         return self.__salary

# try:
#     object = Employee(12345,"Jacob",-2000000)
#     object.set_name("James")
#     print(object.get_name())

# except ValueError as e:
#     print(e)

# Task2

# class Book():
#     def __init__(self,title,author,price):
#         self.__title = title
#         self.__author = author
#         self.__price = self.setPrice(price)

    
#     def setTitle(self,new_title):
#         self.__title = new_title
    
#     def getTitle(self):
#         return self.__title
    
#     def setAuthor(self,author):
#         self.__author = author

#     def getAuthor(self):
#         return self.__author
    
#     def setPrice(self,price):
#         if price < 10:
#             raise ValueError("Enter higher than 10")
#         else:
#             self.__price = price
#             return self.__price

#     def getPrice(self):
#         return self.__price


# try:
#     object = Book("When to rob a bank","Unknown",100000000000)
#     print(object.getAuthor())
#     object.setPrice(2)
#     print(object.getPrice())
#     print(object.getTitle())

# except ValueError as e:
#     print(e)

# Task3

# class Student():
    
#     def __init__(self,name,roll_number,grades):
#         self.__name = name
#         self.__roll_number = roll_number
#         self.__grades = grades
#         self.grades = []
    
    
#     def add_grades(self,grade):
#         self.grades.append(grade)
#         return self.grades
    
#     def avg_grade(self):
#         if self.grades:
#             count = 0
#             sum_grades = 0
#             for i in self.grades:
#                 count += 1
#                 sum_grades += i
#             self.avg_grade =  sum_grades / count
#             return self.avg_grade
#         else:
#             self.error_message()

#     def display_message(self):
#         if self.grades:
#             print(f"Student's average score is {self.avg_grade}")
#         else:
#             self.error_message()
#         print(f"Student's name is {self.__name}")
#         print(f"Students roll number is {self.__roll_number}")
    
#     def error_message(self):
#         print("Student have no grades")
            
    
# class ShopingCard:
#     def __init__(self) -> None:
#         self.__items = []

#     def add_item(self,name,price):
#         item = {"name":name,"price":price}
#         self.__items.append(item)
#     def remove_item(self,name):
#         for item in self.__items:
#             if item["name"] == name:
#                 self.__items.remove(item)
#                 return
#         else:
#             print(f"{name} not found")

#     def total_items(self):
#         print(f"Total number of items {len(self.__items)}")

# object = ShopingCard()
# object.add_item("mouse",500)
# object.add_item("laptop",1000)
# object.remove_item("laptop")
# object.total_items()


class Product:
    def __init__(self,product_id,product_name,quantity_in_stock) -> None:
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock
    
    def setProductId(self,productId):
        self.__product_id = productId
    def getProductId(self):
        return self.__product_id
    def setProductName(self,productName):
        self.__product_name = productName
    def getProductName(self):
        return self.__product_name
    def setQuantity(self,quantity):
        self.__quantity_in_stock = quantity
    def getQuantity(self):
        return self.__quantity_in_stock
    
    def add_stock(self,amount):
        if amount > 0:
            self.__quantity_in_stock += amount
        else:
            print("Enter postive number...")
    def reduce_stock(self,amount):
        if amount > 0:
            self.__quantity_in_stock -= amount
        else:
            print("Enter postive number...")
obj = Product(3333344444,"mouse",5)
obj.add_stock(5)
obj.reduce_stock(7)
print(obj.getQuantity())
