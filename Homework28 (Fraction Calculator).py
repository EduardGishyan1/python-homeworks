from math import gcd
from dataclasses import dataclass

@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        common_divisor = gcd(abs(self.numerator), abs(self.denominator))

        object.__setattr__(self, 'numerator', self.numerator // common_divisor)
        object.__setattr__(self, 'denominator', self.denominator // common_divisor)
        
        if self.denominator < 0:
            object.__setattr__(self, 'numerator', -self.numerator)
            object.__setattr__(self, 'denominator', -self.denominator)


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
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
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
        result = self + other
        object.__setattr__(self,"numerator",result.numerator)
        object.__setattr__(self,"denominator",result.denominator)
        return self

    def __isub__(self,other:"Fraction") -> "Fraction":
        result = self - other
        object.__setattr__(self,"numerator",result.numerator)
        object.__setattr__(self,"denominator",result.denominator)
        return self

def main():
  try:
    f1 = Fraction(1, 2)  
    f2 = Fraction(1, 3)  

    print("Fraction 1:", f1)
    print("Fraction 2:", f2)

    f3 = f1 + f2
    print("Sum:", f3)

    f4 = f1 - f2
    print("Difference:", f4)  

    f5 = f1 * f2
    print("Product:", f5)

    f6 = f1 / f2
    print("Division:", f6)  

    f7 = -f1
    print("Negated Fraction 1:", f7)  
  
  except ZeroDivisionError as e:
     print(e)

if __name__ == "__main__":
    main()


