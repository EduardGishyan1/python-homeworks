import array
from typing import Any,Iterator

class DynamicArray:
    def __init__(self,capacity :int = 10,value : Any = 0) -> None:
        self.__size = 0
        self.setCapacity(capacity)
        self.__arr = array.array("i", [value] * self.__capacity)
    
    def push_back(self,value:Any):
        if self.__capacity == self.__size:
            self.__arr = self.__resize()
        self.__arr[self.__size] = value
        self.__size += 1

    def __resize(self):
            new_capacity = self.__capacity * 2
            new_arr = array.array("i",[0] * new_capacity) 
            for i in range(self.__size):
                new_arr[i] = self.__arr[i]
            self.__capacity = new_capacity
            return new_arr
    
    def setCapacity(self,quantity):
        if isinstance(quantity,int) and quantity > 0:
            self.__capacity = quantity
        else:
            raise ValueError("Enter valid value...")
    
    def __getitem__(self,index:int) -> Any:
        if not isinstance(index,int):
            raise ValueError("Enter valid value")
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise ValueError("Index out of range.")
        return self.__arr[index]

    def __setitem__(self,index:int,value:Any) -> None:
        if not isinstance(index,int) or index < 0:
            raise ValueError("Enter valid value")
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise ValueError("Index out of range.")
        self.__arr[index] = value

    def __str__(self) -> str:
        return f"Array is {[self.__arr[i] for i in range(self.__size)]}"
    
    def __repr__(self) -> str:
        return f"Array is {self.__arr}"
    
    def __len__(self):
        return self.__size
    
    def current_capacity(self):
        return self.__capacity
    
    def __add__(self,other:"DynamicArray") -> "DynamicArray":
        if not isinstance(other,DynamicArray):
            raise TypeError("Enter valid operand for +")
        
        result = DynamicArray(self.__size + other.__size)
        for i in range(self.__size):
            result.push_back(self[i])
        for j in range(len(other)):
            result.push_back(other[j])
        return result
    
    def __iadd__(self,other:"DynamicArray") -> "DynamicArray":
        if not isinstance(other,DynamicArray):
            raise TypeError("Enter valid operand for +=")
        
        if self.__capacity < self.__size + other.__size:
            self.__arr = self.__resize()

        for i in range(other.__size):
           self.push_back(other[i])

        return self
    
    def __eq__(self, other: "DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            if self.__size != other.__size:
                return False
            return all(self[i] == other[i] for i in range(self.__size))
        else:
            raise TypeError("Enter valid type...")
    
    def __ne__(self, other: "DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            return not self == other
        else:
            raise TypeError("Enter valid type...")

    def __lt__(self,other:"DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            return self.__size < other.__size
        else:
            raise TypeError("Enter valid type...")    
    def __le__(self,other:"DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            return self == other or self < other
        else:
            raise TypeError("Enter valid type...")
    
    def __gt__(self,other:"DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            return self.__size > other.__size
        else:
            raise TypeError("Enter valid type...")
    def __ge__(self,other:"DynamicArray") -> bool:
        if isinstance(other,DynamicArray):
            return self > other or self == other
        else:
            raise TypeError("Enter valid type...")
    
    def __iter__(self) -> Iterator[Any]:
        for i in range(self.__size):
            yield self.__arr[i]
    def __hash__(self) -> int:
        raise TypeError("Dynamic array is mutable and can not be hashed")

first_object = DynamicArray(3)
second_object = DynamicArray(3)
