# SOLID principles

# single responsibility
# Bad example

class Post:
    def __init__(self,title:str,content:str) -> None:
        self.title = title
        self.content = content
        self.comments:list = []
        
    def add_comment(self,comment:str):
        self.comments.append(comment)
    
    def display(self):
        print(f"Title {self.title}")
        print(f"Content {self.content}")
        print("Comments:")
        for comment in self.comments:
            print(comment)
            
    def save_database(self):
        print("Post saved in database")
    
    def send_notification(self,user_email):
        print(f"Sending notification to {user_email}")
        
post = Post("First Post","My first post")
post.add_comment("Good!")
post.display()
post.save_database()
post.send_notification("user@example.com")

# good example

class Post:
    def __init__(self,title:str,content:str) -> None:
        self.title = title
        self.content = content
        self.comments:list = []
        
    def add_comment(self,comment:str):
        self.comments.append(comment)
    
    def display(self):
        print(f"Title {self.title}")
        print(f"Content {self.content}")
        print("Comments:")
        for comment in self.comments:
            print(comment)
            
class DataBaseService:
    def save_post(self):
        print("Post saved in database")

class NotificationService:
     def send_notification(self,user_email):
        print(f"Sending notification to {user_email}")

post = Post("First Post","This is my first post")
post.add_comment("Fine!")
post.display()

DataBaseService.save_post(post)
NotificationService.send_notification(post,"user@example.com")

# O open/closed

# Bad example

class Discount:
    def apply_discount(self,amount,discount_type):
        if discount_type == "percentage":
            return amount * 1.5
        elif discount_type == "fixed":
            return amount - 20


# Good example

from abc import ABC,abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self):
        ...

class PercentageDiscount(Discount):
    def apply(self,amount):
        return amount * 1.5
    
class FixedDiscount(Discount):
    def apply(self,amount):
        return amount - 20
    
# L Liskov

# Bad Example

class Vehicle:
    def start_engine(self):
        return "engine started"

class ElectricCar(Vehicle):
    def start_engine(self):
        raise Exception("Electric cars don't have engine")
    
# Good Example

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...

class GasolineCar(Vehicle):
    def start(self):
        return "Engine Started"
    
class ElectricCar(Vehicle):
    def start(self):
        return "Electric system activated"

# I Interface Seggregation

# Bad Example

class MultiFunctionDevice:
    def print(self):
        pass
    
    def scan(self):
        pass
    
    def fax(self):
        pass

# Good example

class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class FaxMachine:
    def fax(self):
        pass
    
# D Dependency Inversion

# Bad example

class FileStorage:
    def save(self,data):
        pass

class DataProcessor:
    def __init__(self) -> None:
        self.storage = FileStorage()
    
# Good Example

class StorageInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass

class FileStorage(StorageInterface):
    def save(self, data):
        pass

class DataProcessor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage