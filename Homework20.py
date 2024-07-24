# Task1

def custom_message(name,lastname,greet = "Hello"):
    full_name = f"{greet} {name} {lastname}"
    return full_name

#print(custom_message("Eduard","Gishyan","Welcome"))

# Task2

def shopping_card(*shopping,tax = 0):
    value = 0
    for i in shopping:
        value += i
    if tax > 0.00:
        value += (value * tax) / 100
    return value

#print(shopping_card(1,2,3,4,5,tax = 10))

# Task3

def user_profile(name,lastname,*,age,city):
    profile = f"Name {name} Lastname {lastname} age {age} city {city}"
    return profile

#print(user_profile("James","Doe",age = 30,city = "New york"))

# Task4

def operation(*ls,operator = "sum"):
    if operator == 'sum':
        value = 0
        for i in ls:
            value += i
        return value
    elif operator == 'max':
        max_number = ls[0]
        for i in ls:
            if max_number < i:
                max_number = i
        return max_number
    elif operator == 'min':
        min_number = ls[0]
        for i in ls:
            if min_number > i:
                min_number = i
        return min_number
    elif operator == "avg":
        sum = 0
        for i in ls:
            sum += i
        average = sum / len(ls)
        return average

ls = [1,2,3,4,5]
#print(operation(*ls,operator = 'avg'))

# Task5

def foo(name,price,category):
    print(f"name {name} price {price} category {category}")

products = {
    "name":"laptop",
    "price":1000,
    "category":"electronics"
        }

#foo(**products)

# Task6

def report(title,total_sales,new_customers,*,top_seller = "James",average_sale = 500):
    total = (f"Title {title}\n"
            f"total sales {total_sales}\n"
            f"new customers {new_customers}\n"
            f"top seller is {top_seller}\n"
            f"average sale {average_sale}")
    
    return total

#print(report("cars",1000,50,top_seller = "Ann" , average_sale = 700))

# Task7


timestamp = 1

def foo(severity,*args,**kwargs):
    global timestamp
    user = kwargs['user'] if "user" in kwargs else 'unknown'
    log_entry = f"Timestamp {timestamp} user: {user} - "
    log_entry += ' '.join(str(i) for i in args)
    timestamp += 1
    print(log_entry)
#foo("error","File not found",user = "James")
#foo("warning","It's warning",user = "Ann")

# Task8

def update(**kwargs):
    print("Updating user settings...\n")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

    processing(**kwargs)

def processing(**kwargs):
    print("\nSettings\n")
    for key,value in kwargs.items():
        print(f"settings {key}:{value}")

#update(language = "English", theme = "dark", notifications = True)
