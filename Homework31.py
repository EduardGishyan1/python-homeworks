# Task1

def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length-i-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1] , arr[j]
                swapped = True
            if not swapped:
                break
  

ls = [8,2,3,67,38929,1204]
bubble_sort(ls)
print(ls)

# Time complexity O(n^2)
# Space complexity O(1)

# Task2

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)

# Time complexity O(n^2)
# Space complexity O(1)

# Task3 

# Iterative 

def BinarySearch(arr,target):
    high = len(arr) - 1
    low = 0
    
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        elif arr[mid] > target:
            high = mid - 1

ls = [10,20,30,40,50,60,70,80]
print(BinarySearch(ls,70))

# Recursive

def Binary_Search(arr,target,low,high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return Binary_Search(arr,target,mid + 1,high)
    
    elif arr[mid] > target:
        return Binary_Search(arr,target,low,mid - 1)

ls = [10,20,30,40,50,60,70,80]
print(Binary_Search(ls,60,0,len(ls)-1))
