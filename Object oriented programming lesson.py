#Object Oriented-Project:based on objects-classes-data-functions
#class-blueprint for creating an object
#object-instance of a class
#attribute-variable inside an object that stores data
#method-functions inside a class that defines a behaviour
#__init__:a construct that initialize an object
#self-#describes

# class Car:
#     def __init__(self,brand,model,year):#pre-defined function or constructor of object
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display_info(self):#define method
#         print(f"{self.brand} : {self.model} {self.year}")
# car1=Car( "Toyota", "land cruiser", 2022)
# car2=Car( "Volkswagen", "Passat", 2024)
# car3=Car( "Mercedes Benz" ,"G-Wagon" ,2022)
# car1.display_info()
# car2.display_info()
# car3.display_info()

#four pillars of OOP
#data hiding-restriction direct access to data(Encapsulation)
class BankAccount:
    def __init__(self,account_number,balance,name,):
        self.account_number=account_number
        self.balance=balance
        self.name=name
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount} is Successsful.\nNew balance : {self.balance}")
    def get_balance(self):
        return self.balance
account=BankAccount("12365400001",154500,"Handson Musa")
account.deposit(450000)
print(self.name)
print(account.get_balance())

#Inheritance or code reusability
class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("Animal makes a sound")
class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} Moows! Moows!")
cow1=Cow("Aurora")
cow2=Cow("Blacky")
cow2.make_sound()
cow1.make_sound()
#polymorphism(multiple forms)-allows same method to have same properties
#abstraction-hiding complexity

