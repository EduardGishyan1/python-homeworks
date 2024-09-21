from math import gcd,trunc
from dataclasses import dataclass

dataclass(frozen=True)
class Fraction:
    def __init__(self,numerator:int,denominator:int = 1) -> None:
        self.setNumerator(numerator)
        self.setDenominator(denominator)
        self.simplify()
        
    
    def simplify(self) -> None:
        common_divisor = gcd(abs(self.denominator),abs(self.numerator))
        self.denominator = self.denominator // common_divisor
        self.numerator = self.numerator // common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator 
        

    def setNumerator(self,numerator:int) -> None:
        if not isinstance(numerator,int):
            raise TypeError("Numerator must be integer...")
        self.numerator = numerator
    
    def setDenominator(self,denominator:int) -> None:
        if not isinstance(denominator,int):
            raise TypeError("Denominator must be integer")
        
        elif denominator == 0:
            raise ZeroDivisionError("You can not division number by 0")
        
        else:
            self.denominator = denominator

    def __str__(self) -> str:
        if not self.denominator == 1:
            return f"Fraction is {self.numerator}/{self.denominator}"
        return f"Fraction is {self.numerator}"
    
    def __repr__(self) -> str:
        return f"Fraction{self.numerator,self.denominator}"
    
    def __add__(self,other:"Fraction") -> "Fraction":
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __sub__(self,other:"Fraction") -> "Fraction":
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __mul__(self,other:"Fraction") -> "Fraction":
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __truediv__(self,other:"Fraction") -> "Fraction":
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator,new_denominator)
    
    def __eq__(self,other:"Fraction") -> bool:
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __ne__(self, other: "Fraction") -> bool:
        return not self == other
    
    def __compare(self,other:"Fraction") -> int:
        return self.numerator * other.denominator - other.numerator * self.denominator
    
    def __lt__(self,other:"Fraction") -> bool:
        return self.__compare(other) < 0
    
    def __le__(self,other:"Fraction") -> bool:
        return self.__compare(other) <= 0

    def __gt__(self,other:"Fraction") -> bool:
        return self.__compare(other) > 0
    
    def __ge__(self,other:"Fraction") -> bool:
        return self.__compare(other) >= 0

    def __hash__(self) -> int:
        return hash((self.numerator,self.denominator))
    
    def __float__(self) -> float:
       return self.numerator / self.denominator
    
    def __int__(self) -> int:
        return self.numerator // self.denominator
    
    def __neg__(self) -> "Fraction":
        return Fraction(-self.numerator,self.denominator)
    
   
    def mixed_number(self) -> str:
        if abs(self.numerator) >= abs(self.denominator):
            whole_part = self.numerator // self.denominator
            remainder = abs(self.numerator) - abs(whole_part) * abs(self.denominator)
        
            if self.numerator < 0:
                whole_part = -abs(whole_part)
        
            if remainder == 0:
                return f'{whole_part}'  

            return f'{whole_part} {remainder}/{abs(self.denominator)}'
    
        return f'0 {self.numerator}/{self.denominator}'
    
    def __iadd__(self,other:"Fraction") -> "Fraction":
        sum_fraction = self + other
        return sum_fraction
    
    def __isub__(self,other:"Fraction") -> "Fraction":
        sub_fraction = self - other
        return sub_fraction

def main():
    try:
        obj = Fraction(14,15)
        obj2 = Fraction(2,3)
        print(id(obj))
        obj += obj2
        print(id(obj)) 
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

