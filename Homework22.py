# Task1

def make_multiple_of(n):
    def multiplier(k):
        return k * n
    return multiplier

multiply_by_3 = make_multiple_of(5)
#print(multiply_by_3(10))

# Task2

def make_counter():
    count = 0
    def add():
        nonlocal count
        count += 1
        return count
    return add

x = make_counter()
#print(x())
#print(x())
#print(x())


def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def decrement():
        nonlocal count
        if count > 0:
            count -= 1
            return count
        else:
            print("Counter cannot be less than 0")
            return count
    return increment,decrement

increment,decrement = counter()
print(increment())
print(increment())
print(decrement())
