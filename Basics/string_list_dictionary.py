#  Strings 

x = "abcd"
y=" xyz"
z= x + y

print(x)
print(z)

# convert number to string use str()  ex ->  str(5)

#  %d and %f -> if we use them in string then they will take the values after then % after the string , , ex
# %d for int %f for float 
number = 5
a = "Hello %d" %number
b = "Hello %f" %number

# limit number of zero after .   
c = "Hello %.2f" %number

print(a) 
print(b) 
print(c) 

#  /n for next line /t for tab 
#  in  in is used to check if string cotains any sub string   ex-   gives True / False 

print("abc" in "abcdef")   # gives True or False 

#  List

l = []
ll = ["abcd" , 123 , 4.5]
print(ll)


#  list methods

#  append 
ll.append(2)

#  inser  ->  ll.inser(index , value)

ll.insert(2,45)

#  pop  ex   ll.pop(index)

ll.pop(1)


#   length  --> string / list  len(string) or len(list)

#   imp ->  convert string to list of characters  
# list(string)

l2 = list("abcd")  # output -> ['a', 'b', 'c', 'd']
print(l2)
print("ab" in l2)
print("a" in l2)

#  in in list  ex ->  "ab" in list -> o/p = False


#     Tuples  created with  ()
# ex x= ("abcd" , 2 , 3, 4.5)
# donot have append , insert , remove , etc 



#      Dictionaries 
#    created with  {}  

d = {'name': 'abcd' , 'age':20}

#  how to get valuse in dictionary  ->  d[key]  ex d['name] 
print(d['name'])

#   delete  del d['name]


# Sample dictionary
d = {"name": "Nipun", "age": 20}

# 1. copy()
d_copy = d.copy()
print("Copy:", d_copy)

# 2. get()
print("Get name:", d.get("name"))

# 3. setdefault()
d.setdefault("city", "Delhi")
print("After setdefault:", d)

# 4. update()
d.update({"age": 26})
print("After update:", d)

# 5. keys()
print("Keys:", d.keys())

# 6. values()
print("Values:", d.values())

# 7. items()
print("Items:", d.items())

# 8. pop()
d.pop("city")
print("After pop city:", d)

# 9. popitem()
d.popitem()
print("After popitem:", d)

# 10. fromkeys()
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("Fromkeys:", new_dict)

# 11. clear()
d.clear()
print("After clear:", d)


#  for searching we can use in or 

# for key, value in d.items():
#     if value == 25:
#         print("Found at key:", key)

