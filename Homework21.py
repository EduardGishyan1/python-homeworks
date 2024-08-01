# Task1

def my_map(func:"callable",iterables:"list")->list:
    '''Map function

       This function Takes function and an iterable as an input and returns a list of the results

       Example:
        >>> def foo(x):
        ...     return x * 2
        >>> my_map(foo,[1,2,3,4,5])
        output: [1,4,9,16,25]
    '''
    ls = [func(i) for i in iterables]
    return ls
    
def foo(x):
    return x * 2

lst = [1,2,3,4,5]

#print(my_map(foo,lst))

# Task2

def my_filter(func:"callable",iterable:"list")->list:
    '''Mimics of python's built-in filter() function 

       This functions takes a function and iterable as input

       Returns:
            A list of items from the Iterable 

        Example:

            >>> def foo(x):
            ...      return x % 2 == 0
            >>> my_filter(foo,[1,2,3,4,5])

            output is [2,4]
    '''
    ls = [i for i in iterable if func(i)]
    return ls

def foo(x):
    return x % 2 == 0

ls = [1,2,3,4,5]
print(my_filter(foo,ls))

# Task3

def my_zip(*iterables:"tuple")->list:
    '''
    Mimics of python's built in zip() function

    as input takes iterables and returns a list of tuples

    >>> my_zip([1,2,3,4],[5,6,7])
    [(1,5),(2,6),(3,7)]
    '''
    min_length = min([len(i) for i in iterables])
    result = [tuple([it[j] for it in iterables]) for j in range(min_length)]
    return result

#print(my_zip([1,2,3,4],[5,6,7]))

# Task4

ls = [1,2,3,4,5]
x = iter(ls)

while True:
    try:
        z = next(x)
        print(z)
    except StopIteration:
        break

# Task 5

def get_nth_element(iterable,n):
    it = iter(iterable)
    for _ in range(n):
        try:
            element = next(it)
        except StopIteration:
             raise IndexError("Index out of range") 
    return element
#print(get_nth_element([1,6,3,5],5))

# Task6

def apply_function(func,iterable):
    ls = [i for i in iterable if func(i)]
    return ls

def foo(x):
    return x & 1 != 0

#print(apply_function(foo,[1,2,3,4,5]))
