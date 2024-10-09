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