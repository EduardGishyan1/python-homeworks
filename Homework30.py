class Person:
    __slots__ = ("name","age","email")
    def __init__(self,name,age,email) -> None:
        self.name = name
        self.age = age
        self.email = email
    
    def display(self):
        return f"Person's name is {self.name} , age is {self.age} email is {self.email}"

try:
    person = Person("James",30,"example@.com")
    print(person.name)
    print(person.age)
    print(person.email)
    print(person.display())
    person.address = "New York"
    
except AttributeError as e:
    print(e)