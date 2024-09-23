from typing import List, Any, Optional

class DynamicArray:
    def __init__(self, capacity: int = 10) -> None:
        self.__capacity = capacity
        self.__size = 0
        self.__array: List[Optional[Any]] = [None] * self.__capacity

    def __resize(self, new_capacity: int) -> None:
        new_array: List[Optional[Any]] = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def __getitem__(self, index: int) -> Any:
        if index >= self.__size:
            raise IndexError("Index out of bounds")
        return self.__array[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        if index >= self.__capacity:
            self.__resize(max(index + 1, self.__capacity * 2))
        self.__array[index] = value
        self.__size = max(self.__size, index + 1)

    def __str__(self) -> str:
        return f"DynamicArray({self.__array[:self.__size]})"
    
    def __repr__(self) -> str:
        return f"DynamicArray({self.__array[:self.__size]})"
    
    def __len__(self) -> int:
        return self.__size
    
    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = DynamicArray(self.__size + len(other))
        for i in range(self.__size):
            result[i] = self.__array[i]
        for i in range(len(other)):
            result[i + self.__size] = other[i]
        return result
    
    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        for i in range(len(other)):
            self.__setitem__(self.__size + i, other[i])
        return self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        return self.__array[:self.__size] == other.__array[:other.__size]
    
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        return self.__size < len(other)
    
    def __le__(self, other: object) -> bool:
        return self.__size <= len(other)

    def __gt__(self, other: object) -> bool:
        return not self.__le__(other)
    
    def __ge__(self, other: object) -> bool:
        return not self.__lt__(other)

    def __iter__(self):
        for i in range(self.__size):
            yield self.__array[i]

    def __hash__(self) -> int:
        raise ValueError("DynamicArray objects are not hashable")

a = DynamicArray()
b = DynamicArray()
a[3] = "hello"
print(a)
print(b)
c = a + b
print(a[-1])
a[8] = "world"
print(a)
print(b)
print(a[5])
