# Task1 

class person:
    def __init__(self,age) -> None:
        self.age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value < 0:
            raise ValueError("Enter valid value...")
        self.__age = value

try:
    user = person(25)
    user.age = -5
except ValueError as e:
    print(e)
    
# Task2

class Rectangle:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.__width * self.__height
    @property
    def perimeter(self):
        return 2 * self.__width + 2 * self.__height
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError("Enter valid value for width...")
        self.__width = value
    
    @height.setter
    def height(self,value):
        if value < 0:
            raise ValueError("Enter valid value for height...")
        self.__height = value

user = Rectangle(5,30)
print(user.width)
print(user.height)
print(user.area)
print(user.perimeter)


# Task3

class Temperature:
    def __init__(self,temperature = 0.0) -> None:
        self.celsius = temperature
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError("Enter valid value for celsius...")
        
        self.__celsius = value
    
    @property
    def fahrenheit(self):
            return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self,value):
        
        if not isinstance(value,(int,float)):
            raise ValueError("Enter valid value for fahrenheit...")
        
        self.__celsius = (value - 32) * 5/9 
try:
    user = Temperature(20)
    user.fahrenheit = 100
    print(user.celsius)
    print(user.fahrenheit)
except ValueError as e:
    print(e)

# Task4

class Descriptor:
    def __init__(self,fget = None,fset = None,fdel = None,doc = None) -> None:
        self.__fget = fget
        self.__fset = fset
        self.__fdel = fdel
        self.__doc = doc
    
    def __get__(self,instance,owner):
        if self.__fget is None:
            raise AttributeError("Enter valid value...")
        return self.__fget(instance)
    
    def __set__(self,instance,value):
        if self.__fset is None:
            raise AttributeError("Enter valid value...")
        self.__fset(instance,value)
    
    def setter(self,fset):
        self.__fset = fset
        return self

class Student:
    def __init__(self,score) -> None:
        self.score = score
    
    @Descriptor
    def score(self):
        return f"Students score is: {self.__score}"
    
    @score.setter
    def score(self,value):
        if isinstance(value,(int,float)) and value in range(0,101):
            self.__score = value
        else:
            raise ValueError("Enter valid value for score...")
        
try:
    user = Student(98)
    print(user.score)
    user.score = 25
    print(user.score)
    
except ValueError as e:
    print(e)
    
except AttributeError as e:
    print(e)

# Task5

class ValidateString:
    def __init__(self,min_length = None) -> None:
        self.__min = min_length
    
    def __get__(self,instance,owner):
        return instance.__name
    
    def __set__(self,instance,value):
        if len(value) < self.__min:
            raise ValueError("Enter valid username...")
        instance.__name = value

class User:
    username = ValidateString(min_length=5)
    def __init__(self,name) -> None:
        self.username = name

try:
    usage = User("James")
    print(usage.username)
    
except ValueError as e:
    print(e)

# Task6

import random

max_salary = random.randint(500,10000)
salary = random.randint(500,10000)

class Custom_descriptor:
    def __init__(self,max_salary) -> None:
        self.__max_salary = max_salary
    
    def __get__(self,instance,owner):
        return instance._salary
    
    def __set__(self,instance,value):
        if value < 0:
            raise ValueError("Salary must be positive...")
        if value > self.__max_salary:
            raise ValueError("Higher than max salary...")   
        instance._salary = value 
        
class Employee:
    salary = Custom_descriptor(max_salary)
    def __init__(self,name,salary) -> None:
        self.salary = salary
        self.__name = name
    
    def __repr__(self) -> str:
        return f"Employee is {self.__name} ,salary is {self.salary}$"

try:
    user = Employee("Ann",salary)
    print(user)
    user.salary = 3000
    print(user)
    
except ValueError as e:
    print(e)

# Task7

class RangeDescriptor:
    def __init__(self,min_value,max_value) -> None:
        self.__min_value = min_value
        self.__max_value = max_value
    
    def __get__(self,instance,owner):
        return instance.__price
    
    def __set__(self,instance,value):
        if not value in range(self.__min_value,self.__max_value):
            raise ValueError(f"Your value must be between {self.__min_value} to {self.__max_value}")
        instance.__price = value
            
class Product:
    price = RangeDescriptor(1,100)
    def __init__(self,price) -> None:
        self.price = price

try:    
    user = Product(10)
    print(user.price)
    user.price = 20
    print(user.price)
except ValueError as e:
    print(e)

# Task8

class PasswordValidator:
    def __init__(self,minimum_length,contains_number) -> None:
        self.min_length = minimum_length
        self.len_numbers = contains_number
    
    def __set__(self,instance,value):
        self.count = sum(1 for i in value if i.isdigit())
        if len(value) < self.min_length:
            raise ValueError("Enter valid password...")
        if self.count < self.len_numbers:
            raise ValueError("Enter valid password...")
        print("Success...")
        instance.__password = value
    
    def __get__(self,instance,owner):
        return instance.__password

class Account:
    password = PasswordValidator(6,2)
    def __init__(self,password) -> None:
        self.password = password
    
try:
    user = Account("Python.1234")

except ValueError as e:
    print(e)
    