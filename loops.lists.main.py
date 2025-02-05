#for loop are used on list
# car=str(input("The car is :"))
cars=["Mercedes","Honda","Toyota","Audi","Volkswagen"]
for car in (cars):
    print(input("The car is :"),)
    response=""
    print("Thank you")
while response!="cars":
 print(input("The car is :"))
 response=""
print("Thank you")
#lists
fruits=["Apple","Oranges","Mangoes","Banana"]
more_fruits=["Pears","Grapes","Strawberry"]
numbers=[1,2,3,4,5]
students=["Handson","Kaka","Tonny","Elsie","Kyrell"]
#accessing a list
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(students[0])
print(students[-1])
print(students[-2])
#modify a list using indexing
numbers[1]=20
print(numbers)
#Adding elements to a list
fruits.append("banana")
print(fruits)
fruits.insert(0,"Blackberry")
print(fruits)
#Using an extent function
fruits.extend(more_fruits)
print(fruits)
#Removing from a list
fruits.remove("Mangoes")
print(fruits)
fruits.pop(0)
print(fruits)
del fruits[1]
print(fruits)
#looping through a list
for fruit in fruits:
    print(fruit[0])
for i in range(len(fruits)):
    if i==3:
        print(fruits[3])
#check if an item is in the list
if "watermelon" in fruits:
    print("Strawberry is in the list")
elif "watermelon" not in fruits:
    print("watermelon is not in the list")
fruits.append("watermelon")
print(fruits)
#sorting and reversing a list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#list slicing
print(numbers[0:4])
print(numbers[-3:])
#list compression
evens=[i for i in numbers if i %2 ==0]
print(evens)

#assignment
numbers=[]
for i in range(5):
   num=int(input("Enter a number :"))
   numbers.append(num)
print(f"The numbers entered : {numbers}  ")
print("Sum of numbers :",sum(numbers))

#assignment
#write a program asking user to enter names one by one into a list ,arrange names in alphabetical order
names=[]#an empty list to store names
for i in range(5):#to get five names from the user
    name=input("Enter a name:")
    names.append(name)#adds name to a list
names.sort()#sorts name alphabetically
print(f"Names in alphabetical order are :{names}")
longest_name=max(names,key=len)
print(f"The longest name is :{longest_name}")

