class Person:
    def __init__(self,name,age):
        self.name = name
        self.set_age(age)
    
    def display_message(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.__age}")

    def greet(self):
        print(f"Hello {self.name}")

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            print("Age must be between 0 and 100")


person_data = Person("James",54)
person_data.greet()
person_data.display_message()
person_data.set_age(55)
print(person_data.get_age())
