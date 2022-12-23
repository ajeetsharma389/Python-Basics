# remove duplicate value from list

tmpList =("Ajeet","Shiva","Rajesh","Ajeet")

#define a set to remove duplicate value

print (tmpList)
tmpSet = set(tmpList)

print(tmpSet)

# Print first character of each item

for x in tmpSet:
    print(x[0])

## Use the get method to print the value of the "model" key of the car dictionary.

car = { 
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
print(car["model"])


## Frozen set

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 


## Regaular expressio

import re
match = re.match(r"World", "Hello, World!")
if match is None:
 print("It doesn't match.")

 # Random Number
import random

print(random.randrange(1, 10))

#Looping Through a String

localString = "testString"

for x in localString:
    print(x,"\n")

# Replace String

rSstring="Hello"

print(rSstring.replace("H","M"))


num = input("Enter Number:")

for x in range(int(num)):
    if x%2 != 0:
        print("numer is odd",x)

fruits = ["apple", "banana", "aherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x[0]:## check first character as a
    newlist.append(x)

print(newlist)


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

