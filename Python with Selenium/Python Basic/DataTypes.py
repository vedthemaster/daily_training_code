a= 100
b= 10.2356
c= 100+ 3j

# complex_number = complex(input("Number :"))
# print(complex_number)

print("The type of variable having value", a, "is",type(a))
print("The type of variable having value", b, "is",type(b))
print("The type of variable having value", c, "is",type(c)) 
# print("The type of variable having value", complex_number, "is",type(complex_number)) 

string1 = "This is first string"
string2 = ' This is second string'

print(string1, "joined with", string2)
print(string1 + "joined with" + string2)

# List DataType 

list1 = ["hello", 5,25.5,5,"biro!", "How", "are", "you"]
print(list1)
# print(list1[-1])
# print(list1[0][1])
print(list1[1:3])
# del list[3]
list1.append("?")
print(list1)

# Tuple DataType
tpl1 = ("hello", 5,25.5,5,"biro!", "How", "are", "you")
print(tpl1)

print(tpl1[3])


# Dictonary DataType

dict1 = {"Orange":"Orange", "Apple":"Greeen","Banana": "Yellow"}
dict2 = {}
print(dict1)
dict2["day"] = "Monday"
dict2["colour"] = "Red"
dict2["number"] = 25
print(dict2)
print(type(dict2))
print(dict2["number"])
print(len(dict2))

x= dict2.get("colour")
u= dict2.keys()
y= dict2.values()
print(x)
print(u)
print(y)
print(dict1.items())

# Set DataType

set1 = {1,2,3,4,5,6,7,8,9,"one","two","three","one","One"}
set2 = {11,12,12.2,24,"one",2,4}

set1.add("Four")
print(set1)
set1.discard("one")
set1.remove("One")
print(len(set1))

for i in set1:
    print(i,end=" ")
uni = set1.union(set2)
inter = set1.intersection(set2)
print(uni)
print(inter)

set1.pop()
print(set1)
set1.clear()
print(set1)
# del set1
# print(set1)


