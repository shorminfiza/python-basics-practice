#My Python Practise Code ;)


#Chapter 1
#Data-types and variables

print("Hello boss")

age = 23
price = 24.888

print(23+56)

x,y,z = 4,"Tomato", 'Get exited!'
print(x,y,z)

"""This is a multi lined comment
but it's not cool"""

name = "Fiza"
print(name,age,price)
print(type(name))

old = False
a = None

print(old,a)
print(2**4) #power
print(11/2) #returns an integer value

#relational operators(== , != , >= , <=)

a = 50
b = 40
print(a==b) #false
print(a!=b) #true

#logical operators(and,or,not)

print(not False)
print(not(a>b))

val1 = True
val2 = True
print("AND operator:",val1 and val2) #works like and or not gate
print("OR operator:",(a==b) or (a>b))

#type conversion vs type-casting

a = 2
b = 4.45

sum = a + b #converts to float cuz that is superior
print("Type convo:",sum)
"""
a = "2"
b = 5

sum = a + b #error cuz string and int cannot sum
"""
#type casting

a = int("2")
b = 5

sum = a + b #works just fine!
print("Type cast:",sum)


#taking user input but wait! The type is always <str>
name = input("Write your dumb name:")
print("Hello there",name)
print("The type of your name even if you entered a number:",type(name))

#typecast the input value
val3 = int(input("Whats your age dude?"))
print(val3, "Type of your age",  type(val3))


name1 = '''SRK'''
name2 = 'Shormin'
name3 = "Fiza"
print(name1,name2,name3)

line1 = "I am boss"
line2 = "Absolutely nonsense"

print("Should I say!", end=" ")
print(line2)


#Chapter 2
#Conditional Statements

str1 = 'My name is Khan'
str2 = '''Say my name'''
str3 = "Real or not real?"

print(len(str1)) 
print(str1 + ' ' + str2) #concatination pro!
print(str1[5])

#to slice any string
print(str1[1:5])
print(str2[:4])
print(str3[7:len(str3)])
print(str2[-3:-1]) #negative slicing

#use of some functions

mystr = "I am SHORMIN FIZA"

print(mystr.endswith("MIN\n"))
print(mystr.capitalize()) #capitalizes the first character
print(mystr.replace('O','A'))
print(mystr.find('a')) #returns 1st index of the first occurrer
print(mystr.count("I"))
#Conditional statements

age1 = input("Enter your age: ")
if(int(age1) >= 18):
    print("Adult")
elif(int(age1)<18):
    print("Kid")
else:
    print("Wrong input!!")


#Chapter three

#List in python works like array and is mutable

student = ["Fiza",98,45.5, "EWU"]
x,y,z,k = student
print(student)
print(x,y,z)
student[0] = "Keya"
print(student[0])
print(student[0:2])

list = [12,34,53,35]
#add one element at the end
list.append(70)
print(list)
#sorts in ascending order
list.sort()
print(list)
#sorts in descending order
list.sort(reverse=True)
print(list)
#reverses the list
list.reverse()
print(list)
#insert element at index
list.insert(2,'ASF')
print(list)
#to remove at the first occurance
list.remove(34)
print(list)
#to remove from an index
list.pop(2)
print(list)

thislist = ["apple","banana","mango","pineapple","guava"]
thistuple = ("kiwi","orange")
thislist[1:2] = ["Jackfruit","Melon"]
print(thislist)
thislist.extend(thistuple)
print(thislist)

for x in thislist:
    print(x)
#or you can use the for loop as-
for i in range(len(thislist)):
    print(thislist[i])
#Or we can while loop!
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


#Tuple acts like list but its mutable

tup = (1,2,2,3,4)
print(tup[0])
print(tup.index(2))
print(tup.count(2))

#Chapter 4
#Dictionary which acts like structure (key:value pair)

fiza = {
    "Name" : "Shormin Fiza",
    "Subjects" : {
        "CSE" : 98,
        "Maths" : 80,
        "Robotics" : 100
    },
    "Age" : 18,
    "Is Adult" : True,
    69 : 0
}

print(fiza)
print(fiza["Name"])
print(fiza["Subjects"]["Robotics"])

#Special Methods 

print(fiza.keys())
#fprint(list(fiza.keys()))

for x in "Banana":
    print(x);

ni = " Hola amigo! Yo soy Fiza"

print("Fiza" in ni)
if "Fiza" in ni:
    print("Si")

print(ni.upper())
print(ni.lower())
print(ni.strip())
print(ni.replace("F","P"))

a = "HEll0"
b = "WORLD"
c = 69
print(a+" "+b+str(c))

#or use f string

d = f"My name is {c}"
print(d)

 