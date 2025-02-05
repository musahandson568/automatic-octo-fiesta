# is a reusable block of codes,helps us make organised,efficient programs easier to debug e.g.print,capitalize,len,max which are built in functions
from operator import add

# fruits=["pineapples","watermelon","oranges","grapes"]
#user-defined functions
# def great(name):
#     print(f"Hello ,{name} welcome to Today's lesson.")
# great("Handson")
# great("Keyrell")
# #lambda functions in terms of argument and expression
# add=lambda x,y:x+y
# # print(add(x:5,y:6))
# #lambda arguments:expression
# def name():
#     print("Handson","Keyrell")
# name()
# def sum(a,b):
#     return a+b
# result=add(9,10)
# print(f"The sum :{result}")
# def car(name="Honda"):
#     print(f"I like {name}")
# car("Ford wild truck")
#variable length arguments
# numbers=[1,5,15,28,35,49,85,97]
# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(2,8,25,48))
#
# def multiply(x,y):
#     return x*y
# print(multiply(4,9))
# #keyword arguments
# def display_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# display_info(name="Handson",age=25,estate="Unique Estate")
#
# #assignment1.1 on function
# def max_of_three_numbers(a,b,c):
#     return max(a,b,c)
# print(max_of_three_numbers(40,86,14))
#assignment 1.2 check if number is even or odd
# def check_even_number(n):
#     if n %2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_number(9))
# print(check_even_number(8))

#check if number is prime
def is_prime(n):
    if n <2:is_prime
    return False
    for i in range(2,int(n**0.5)+1):
        if i+n% i==0:
            return False
            return True
print(is_prime(47))
print(is_prime(200))
print(is_prime(7))


