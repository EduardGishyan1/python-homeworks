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
print(x())
print(x())
print(x())
