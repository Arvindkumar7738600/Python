#lets starts

#Dictionary in python[ use to store data values in key:Values]

info = {
    "key" : "value",
    "name" : "arvind",
    "learning" : "python",
    "age" : 18,
    "is young" : True,
}

print(info)
print(type(info))
print(info["key"])
print(info["learning"])


info["name"] = "Arru" #OVERWRITE
info["age"]= "20"
print(info)

null_dict = {}
null_dict["name"] = "macbook"
print(null_dict)

#NESTED DICTIONARIES
Students = {
    "name" : "arvind kumar",
    "subjects" : {
        "pht" : 96,
        "chem" :90,
        "math" : 92,
    }
}
print(Students["subjects"]["chem"])


#METHODS

#myDIct.keys()   returns all keys
print(list(Students.keys()))


#myDicts.values()   returns all values
print(list(Students.values()))


#mtDict.items()   return all (key, val) pairs as tuples
print(Students.items)
pairs = list(Students.items())
print(pairs[0])

#myDict.get("key")   returns the key acording to value
print(Students["name"])
print(Students.get("name"))  #same print 

 #error
print("hlw")
print("wellcome")
print("macbook")
print("arvind side")

#myDict.update(nemDict)  inserts the specified items to the dicitionary
Students = {
    "name" : "arvind kumar",
    "subject" : "python",
}

new_dict = {"city" : "delhi", "age": 17} 
Students.update(new_dict)
print(Students)


#SET IN PYTHON
#nums = {1, 2, 3, 4}   
#set2 = {1, 2, 2, 3}  
#repeated elements stored only once, so it resolved to {1, 2}

collection = {1, 2, 3, 2, "hello", "arvind"}
print(collection)  #duplicate not allowed
print(type(collection))
print(len(collection))  #total no of items


#null_set = set()
collection = set()
print(type(collection))

#SET METHODS

#set.add()  [add of elemnts]
collection = set()
collection.add(1)
collection.add(2)
collection.add("a")
collection.add("a")
print(collection)
#immutal = hash value     [ immutable = not change]
#mutable = unhash value   [ mutable = change value] 

#set.removal() 


#set.clear()  empties the set.
collection = set()
collection.add(1)
collection.add(2)
collection.add("a")
collection.add("a")
collection.clear()  #all clear
print(len(collection))


#set.pop()  removes a random value.
collection = {1, 2, 3, 2, "hello", "arvind"}
print(collection.pop())
print(collection.pop())
print(collection.pop())


#set.union(set2)  combine both set value and return new
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.union(set2))



#set.intersection(set2)  combine common values and return new
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.intersection(set2))

#reall the concept
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(len(set1))
print(len(set2))
print(set1.union(set2))