# fruits=("apples","oranges","bananas","avocado")
# mixed_tuple=(10,"hello",20,"handson")
# #accessing info in a tuple using indexing(tuples are immutable;you cannot change them)
# print(mixed_tuple[0])
# print(fruits[3])
# print(fruits[0])
# print(fruits[0:3])#tuple slicing
# print(fruits[:2])
# print(fruits[1:])
# #'tuple' object has no attribute 'append' therefore convert a tuple to a list,add an element convert back to tuple
# fruits_list=list(fruits)
# fruits_list.append("strawberry")
# fruits=tuple(fruits_list)
# print(fruits)
# for fruit in fruits:
#     print(fruit)
# person=("Alice",25,"teacher","mother")#you can attach directly to a variable (person)
# name,age,job,family=person
# print(name)
# print(age)
# print(job)
# print(family)
#tuple faster,immutable,stores different types of data unlike lists
#create a tuple of five cities check if city in tuple else print city not found
# cities=("Nairobi","Kisumu","Mombasa","Nakuru","Eldoret")
# user_city=input("Enter a city :").capitalize()
# if user_city in cities:
#     print(f"{user_city} is at index {cities.index(user_city)}")
# else:
#     print("Oh! sorry,City is not found.Please try again another city.")
#assign
#create a tuple of numbers and count how many times a specific number appears
# numbers=(10,4,10,8,10,5,7,10,8,6,8,2)
# user_number=int(input("Enter a number :"))
# count=numbers.count(user_number)
# print(f"The number {user_number} appears {count} times.")

#dictionaries are key value of pairs
# car={
#     "name":"ford ranger",
#     "manufacturer":"ford",
#     "model":2.5,
#     "year":2025,
#     "transmission":"manual",
#     "chasis number":5485745
#
# }
# car["paint"]="brown"
# print(car)
# del car["year"]
# print(car)
# print(car["name"]) use print(car.get("name")) to avoid code from breaking
# print(car.get("name"))
# print(car.get("year"))
# print(car.get("manufacturer"))
# print(car.get("chasis number"))
# print(car.get("model"))

#assignment
names=("Peter","Kendy","Elsie","Kelsie","Wadsworth")
user_name=input("Enter user name :").capitalize()
if user_name  in names:
    print(f"{user_name} is at {names.index(user_name)}")
else:
    print("Invalid User name.Enter a valid user name.")

score={"Peter":"B",
"Kendy":"A-",
"Elsie":"B+",
"Kelsie":"A",
"Wadsworth":"C+"}
# scored grade :dict{"name"})
user_score=dict["Peter":"B","Kendy":"A-","Elsie":"B+","Kelsie":"A","Wadsworth":"C+"]
for user_score in score:
    print(f"{user_name} scored a {(user_score)}")
print(score)





