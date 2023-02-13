

# List is equiv to array in other programming language
# can have mixed typed
# Mutable
list = ['Yannick', 'brinette', 'Jasper']

list.append('Gianni')
list.remove('Jasper')
count = 0

print("List | Mutable array")
print("***************************\n")

for n in list:
    print("name",count,":", n)
    count += 1



# dictionary is the equiv of HashMap in java
# mutable
print("\nDictionary | Mutable (Same as HashMap in Java)")
print("***************************\n")
dic = {}

dic["Yannick"] = {"address": "32 cool ave", "state" : "Iowa"}
dic["Green"] = {"address": "455 Davenport ave Sw", "state" : "Illinois"}

dic["Slick"] = {"address": "455 Davenport ave Sw", "state" : "New York"}
dic["James"] = {"address": "32 cool ave", "state" : "Iowa"}

#print(dic["Yannick"]["state"])

for key, value in dic.items():
    print("name:",key, "| full address:", value['address'], "| state:", value['state'])


# sets | mutable
print("\nSet | Mutable (Same as HashSet in Java)")
print("******************************************\n")
numbers = {5, 4, 6}
numbers.add(98)
numbers.add(99)
numbers.remove(4)

for x in numbers:
    print(x)

# Tuple | Immutable
print("\nSet | Immutable list (Same as HashSet in Java)")
print("******************************************\n")
tuple1 = (1, 2, 3, 4)

for x in tuple1:
    print("el:",x)
