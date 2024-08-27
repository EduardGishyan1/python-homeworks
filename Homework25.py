# Task1

# def fibonacci_generator():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b

# fib = fibonacci_generator()
# for _ in range(10):
#     print(next(fib))

# Task2

# def prime_generator():
#     num = 2
#     while True:
#         for i in range(2,int(num ** 0.5)+1):
#             if num % i == 0:
#                 break
#         else:
#             yield num
#         num += 1

# gen = prime_generator()

# for i in gen:
#     if i > 100:
#         break
#     print(i)


# Task3

# def infinite_sequence():
#     count = 0
#     while True:
#         yield count
#         count += 1

# func = infinite_sequence()
# for i in range(10):
#     print(next(func))

# Task4

# square = (i ** 2 for i in range(1,20))

# for i in square:
#     print(i)

# Task 5

# def read_file_lines(file_path):
#     open_file = open(file_path)
#     for line in open_file:
#         yield line.strip()
#     open_file.close()

# gen = read_file_lines("file.txt")
# for i in gen:
#     print(i)

# Task6

# def repeat_element(element,times):
#     for _ in range(times):
#         yield element
# x = repeat_element("hello",5)
# y = repeat_element("python",3)

# for i in x:
#     print(i)
# for j in y:
#     print(j)

# Task7

# def custom_range(start,stop = None,step = 1):
#     if stop is None:
#         stop = start
#         start = 0

#     i = start
#     while (i < stop if step > 0 else i > stop):
#         yield i
#         i += step

# m = custom_range(10)
# for i in m:
#     print(i)

# Task8

# ls = [i for i in range(1,51)]
# even = (j for j in ls if j % 2 == 0)
# for k in even:
#     print(k)

# Task9 

# def gen1():
#     for i in range(1,6):
#         yield i
# def gen2():
#     for j in gen1():
#         yield j
#     for k in range(6,11):
#         yield k

# gen = gen2()
# for i in gen:
#     print(i)

# Task 10

# def exception_propagator(iterable):
#         for i in iterable:
#             if i != "error":
#                 yield i
#             else:
#                 raise ValueError("An error occured!")

# ls = [1,2,"error",4,5]
# m = exception_propagator(ls)

# try:
#     for i in m:
#          print(i)
# except ValueError as e:
#      print(e)

# Task11

# def custom_reduce(func, iterable, initializer=None):
#     it = iter(iterable)

#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
    
#     for item in it:
#         value = func(value,item)
#     return value

# print(custom_reduce(lambda x,y: x + y,[1,2,3,4,5]))

# Task 12

# def custom_zip(*iterables):
#     min_length = min(len(i) for i in iterables)
#     res = []
#     for i in range(min_length):
#         yield tuple(item[i] for item in iterables)

# gen = custom_zip([1,2,3,4,5],[6,7,8,9,10,11,12])
# for i in gen:
#     print(i)

# Task 13

# def custom_filter(func,iterable):
#     if func is None:
#         for i in iterable:
#             if i:
#                 yield i
#         return
    
#     for i in iterable:
#         if func(i):
#             yield i

# gen = custom_filter(lambda x:x % 2 == 0,[1,2,3,4,5])
# for i in gen:
#     print(i)

# Task 14

# def custom_map(func,*iterable):
#     min_length = min(len(i) for i in iterable)
#     for i in range(min_length):
#         ls = [item[i] for item in iterable]
#         yield func(*ls)
        
# x = custom_map(lambda x,y:x + y,[1,2,3],[4,5,6])
# for i in x:
#     print(i)
