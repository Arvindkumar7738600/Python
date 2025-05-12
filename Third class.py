marks = [87, 81.5, 87.5, 95.2, 45.1]
print(marks)
print(len(marks))
print(marks[0])
print(marks[3])

student = ["arvind", 85, "jharkhand"]
print(student)

student = ["arvind", 85, "jharkhand"]
print(student[0])
student[0] = "Arru"    #(python allowed students[0])
print(student)


#list Slicing

marks = [87, 64, 33, 95,76]
print(marks[0 :4])
print(marks[1 :])

#list of methods (similar to strings slicing)

list = [2, 1, 3]
list.append(4)  #adds one elements at the end.(2, 1, 3, 4)
print(list)

list = [2, 1, 3] #sort in ascending order (1, 2, 3)
list.sort()
print(list)

list = [2, 1, 3] #sort in descending order (3, 2, 1)
print(list.sort(reverse=True))
print(list)

#it is apply on int value and char 
list = ["arvind", "kumar", "yadav"]
print(list.sort(reverse=True))
print(list)

list = ['2', '5', '3','9']
list.reverse() #reverses list
print(list)

list = [2, 1, 3]
list.insert(1, 5)  #insert elements at index
print(list)

list = [2, 1, 3, 1]
list.remove(1)  #removes first occurence of elements [2, 3, 1]
print(list)

list = [2, 1, 3, 1]
list.pop(2) # removes elements at idx
print(list)

#TUPLES IN PYTHON
# ~ A built in data type that lets us create immulatble sequnces of values.

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])
print(tup[1])

tup = (1,)
print(tup)
print(type(tup))

tup = (1)
print(tup)
print(type(tup))

tup = (1.5)
print(tup)
print(type(tup))

#tuples method 

tup = (2, 1, 3, 1)
print(tup.index(1))


tup = (2, 1, 3, 1)
print(tup.count(1)) #1 kitne baar count aa rha hai elements mai.

#QUESTION PRACTICE 
#WAP to ask the user to enter names of 3 favourite movies and store them in  LIST.
movies = []
mov1 = input("enter 1st movies name: ")
mov2 = input("enter 2nd movies name: ")
mov3 = input("enter 3rd movies name: ")
print(movies) 


