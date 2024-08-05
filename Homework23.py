# Task1

#x = lambda factor:lambda x: factor * x
#print(x(5)(3))

# Task2

def make_adder(n):
    def foo(x):
        return x + n
    return foo
#print(make_adder(5)(4))

# Task3

def double(j):
    return j * 2

def apply_twice(f,x):
    return f(f(x))

#print(apply_twice(double,5))

# Task4

def func1(x):
    return x + 1
def func2(x):
    return x + 2

def compose(f,g):
    def foo():
        return f(g(0))
    return foo
x = compose(func1,func2)()
#print(x)

# Task5

def power_factory(n):
    def foo(x):
        return n ** x
    return foo

x = power_factory(5)(2)
#print(x)

# Task6

ls = [2,3,4,5]
x = map(lambda x: x * x,ls)
#print(list(x))

# Task7

ls = [1,2,3,4,5,6]
f = filter(lambda x: x % 2 == 0,ls)
#print(list(f))

# Task8

def make_greeting(greeting):
    def foo(name):
        print(f"{greeting} {name}")
    return foo

#name = make_greeting("Hello")
#name("James")
#name("Thomas")

# Task9

def make_accumulator(start=0):
    def add(value):
        nonlocal start
        start += value
        print(start)
    return add
#x = make_accumulator(5)
#x(3)
#x(-2)

# Task10

def make_config(key,value):
    def foo():
        return {key:value}
    return foo

y = make_config("Hello","world")()
#print(y)

# Task11

def make_logger(level):
    levels = {"DEBUG":1,"INFO":2,"WARNING":3,"ERROR":4,"CRITICAL":5}
    
    if level not in levels:
        raise ValueError("Invalid log level")
    
    def foo(msg_level,msg):
        if levels[msg_level] >= levels[level]:
            print(f"{msg} {msg_level}")
            return 1 
    return foo
    
#func = make_logger("WARNING")
#func("ERROR","This is an error message:")

# Task12

def make_memoize(f):
    cache = {}
    
    def memoized_function(*args):
    
        if args in cache:
            return cache[args]
        
        result = f(*args)
        cache[args] = result
        return result
    
    return memoized_function

def expensive_computation(x):
    return x * x

#memoized_computation = make_memoize(expensive_computation)

#print(memoized_computation(4)) 


# Task13 

def bar(n):
    functions = []
    
    for i in range(n):
        def multiplier(x, index=i):
            return x * index
        functions.append(multiplier)
    
    return functions

funcs = bar(5)

#for idx, func in enumerate(funcs):
    #print(f"Function {idx} __closure__: {func.__closure__}")
    #print(f"{idx} {func(10)}")

# Task14

def add(x:int,y:int)->int:
    return x + y
def sub(x:int,y:int)->int:
    return x - y
def mul(x:int,y:int)->int:
    return x * y
def div(x:int,y:int)->int:
    if y == 0:
        raise ZeroDivisionError("Enter valid number")
    return x / y

dict = {"+":add,"-":sub,"/":div,"*":mul}

#operator = input("Enter operator: ")
#x = int(input("Enter number: "))
#y = int(input("Enter number: "))
#print(dict.get(operator)(x,y))

# Task15

def manipulate_string(s,operation):
    def upper():
        ls = []
        for i in s:
            if ord(i) >= 97:
                 z = chr(ord(i) - 32)
                 ls.append(z)
            else:
                ls.append(i)
        return "".join(ls)

    def lower(): 
        ls = []
        for i in s:
            if ord(i) <= 97:
                z = chr(ord(i) + 32)
                ls.append(z)
            else:
                ls.append(i)
        return "".join(ls)
    
    def title():
       x = s.split()
       ls = [word.capitalize() for word in x]
       title_text = " ".join(ls)
       return title_text
    
    def reverse():
        return s[::-1]
    
    dict = {"upper":upper,"lower":lower,"title":title,"reverse":reverse}

    print(dict.get(operation)())

#manipulate_string("Hello","upper")

# Task16

def calculate_area(shape,**kwargs):
    def rectangle():
        if len(kwargs) == 2 and "width" in kwargs and "height" in kwargs:
            height = kwargs["height"]
            width = kwargs["width"]
            area_of_rectangle = height * width
            print(area_of_rectangle)
        else:
            print("error")
            return
    
    def circle():
        if len(kwargs) == 1 and "radius" in kwargs:
            radius = kwargs["radius"]
            area_of_circle = 3.14 * radius ** 2
            print(area_of_circle)
        else:
            print("error")
            return

    def triangle():
        if len(kwargs) == 2 and "base" in kwargs and "height" in kwargs:
            base = kwargs["base"]
            height= kwargs["height"]
            area_of_triangle = base * height * 0.5
            print(area_of_triangle)
        else:
            print("error")
            return
    
    def square():
        if len(kwargs) == 1 and "side" in kwargs:
            side = kwargs["side"]
            area_of_square = side ** 2
            print(area_of_square)
        else:
            print("error")
            return

    funcs = {"rectangle":rectangle,"circle":circle,"triangle":triangle,"square":square}
    shape_function = funcs.get(shape)
    if shape_function:
        shape_function()
    else:
        print("error")

#calculate_area("square",side = 5)

# Task17

def convert_temperature(value,from_unit,to_unit):
    def Celsius():
        if to_unit == "Fahrenheit":
            return value * 1.8 + 32 
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            print("error")
            return
    def Fahrenheit():
        if to_unit == "Celsius":
            return (value - 32) * 0.555
        elif to_unit == "Kelvin":
            return (value + 459.67) * 0.555
        else:
            print("error")
            return
    def Kelvin():
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 1.8 + 32
        else:
            print("error")
            return
    dictionary = {"Celsius":Celsius,"Fahrenheit":Fahrenheit,"Kelvin":Kelvin}
    var = dictionary.get(from_unit)
    if var:
       print(var())
    else:
        print("error")

#convert_temperature(5,"Kelvin","Fahrenheit")

# Task18

def compound_interest(principal,rate,periods,time):
     return principal * (1 + rate / periods) ** (periods * time)
def loan_payment(principal,rate,periods):
    if rate == 0:
        return principal / periods
    monthly_rate = rate / 12
    return principal * (monthly_rate * (1 + monthly_rate) ** periods) / ((1 + monthly_rate) ** -periods)

def investment_return(principal,final_value,time):
    return (final_value / principal) ** (1 / time) - 1

def financial_calculator(operation,**kwargs):
    dictionary = {
    "compound_interest":compound_interest,
    "loan_payment":loan_payment,
    "investment_return":investment_return
     }
    if operation in dictionary:
        x = dictionary[operation]
        return x(**kwargs)
    else:
        print("error")
j = financial_calculator("compound_interest",principal = 100,rate = 5,periods = 10,time = 5)
#print(j)

# Task19

def mean(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    return "error"
def median(numbers):
    if not numbers:
        print("error")
        return
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid] / 2)

def mode(numbers):
    frequence = {}
    for num in numbers:
        if num in frequence:
            frequence[num] += 1
        else:
            frequence[num] = 1
        max_count = max(frequence.values())
    ls = [item for item,count in frequence.items() if count == max_count]
    return ls

def standard_deviation(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev

def analyze_data(data,operation):
    dictionary = {"mean":mean,"median":median,"mode":mode,"standard_deviation":standard_deviation}
    if operation in dictionary:
        x = dictionary[operation]
        print(x(data))
    else:
        print("error")
        return

#analyze_data([1,2,3,4,7,5],"mean")

# Task20

import os

def read(file_name):
    content = open(file_name, "r")
    print(content.read())
    content.close()

def write(file_name,content):
    file = open(file_name,"w")
    file.write(content)
    file.close()
def append(file_name,content):
    file = open(file_name,"a")
    file.write(content)
    file.close()
def delete(file_name):
    os.remove(file_name)

def file_manager(file_name,operation ,content):
    dictionary = {"read":read,"write":write,"append":append,"delete":delete}
    if dictionary[operation]:
        x = dictionary[operation]
        if dictionary[operation] == read or dictionary[operation] == delete:
            return x(file_name)
        else:
            return x(file_name,content)
print(file_manager("d.txt","write","Hello"))

# Task21 

def sorting(lst):
    lst.sort()
    return lst
def reversing(lst):
    return lst[::-1]
def mapping(lst):
    x = map(lambda x: x if x % 2 == 0 else None,lst)
    return list(x)
def filtering(lst):
    y = filter(lambda x: x if x % 2 == 1 else None,lst)
    return list(y)

def transform_list(operation,lst):
    dict = {"sorting":sorting,"reversing":reversing,"mapping":mapping,"filtering":filtering}
    if dict[operation]:
        x = dict[operation]
        return x(lst)
#print(transform_list("mapping",[1,8,3,2,5]))

# Task22

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    if x < 0:
        raise ValueError("invalid number")
    return x ** 0.5

def factorial(n):
    if n < 0:
        raise ValueError("invalid value")
    value = 1
    for i in range(1,n+1):
        value *= i
    return value

def math_operations(number,operation):
    var = {"square":square,"cube":cube,"square_root":square_root,"factorial":factorial}
    try:
        x = var[operation]
        print(x(number))
    except KeyError:
        raise NameError(f"{operation} is not a valid")
    except ValueError:
        print(f"{operation} is not a valid")
#math_operations(25,"square_roo")

# Task23

def word_count(text):
    x = text.split()
    dictionary = {}
    for word in x:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print(dictionary)


def character_count(text):
    dictionary = {}
    for letter in text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    print(dictionary)

def find_word(text,word):
    text = text.lower()
    word = word.lower()

    quantity = text.split().count(word)
    print(quantity)

def replace_word(text,word,rep_word):
    x = text.replace(word,rep_word)
    print(x)

def process_text(text,operation,**kwargs):
    dictionary = {"word_count":word_count,"character_count":character_count,"find_word":find_word,"replace_word":replace_word}
    try:
        x = dictionary[operation]
        if x == word_count or x == character_count:
            x(text)
        else:
            x(text,**kwargs)
    except:
        raise ValueError("Invalid value")

#process_text("Hello","replace_word",word = "H",rep_word = "O")
