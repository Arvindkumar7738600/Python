#Loops in python  [ it is uesd to repeat instructions.]
count = 1
while count <= 5 :
    print("hello")
    count +=1

    print(count)


i = 1
while i <=4:
    print("hello arvind")
    i+=1

#i want to print number 1 to 5
i = 1
while i <= 5:
    print(i)
    i+=1
    print("loop ended")

#QUESTION PRACTICE

#print number from 1 to 100
i = 1
while i <=100: #this is a stopping condition.
    print(i)
    i+=1

# print number from 100 to 1.
i = 100
while i >=1:
    print(i)
    i-=1


#print the multiplication table of a number n.  suppose n = 4
i = 1
while i <= 10:
    print(4*i)
    i+=1

#print  the elements of the following list using a loops
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding..")
    i +=1



#BREAK AND CONTINUE 

#BREAK - USSED TO TERMINATE THE LOOPS WHEN ENCOUNTERED.
i = 1 
while i <= 5:
    print(i)
    if(i ==3):
        break
    i +=1
    print("end of loop")



nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding..")
    i +=1

    print("end of loops")


#CONTINUE~ current itration and continue execution of the loops wiith the next iteration.
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

#loops in python[list, string, tuples, etc]
list = [1, 2, 3, 5]

for num in list:
    print(num)


#for loops :-
veggies = ["patato", "vegetable", "ladyfinger", "Seeets"]

for val in veggies:
    print(val)

 
tup = (1, 2, 3, 4, 5, 6)

for num in tup:
    print(num)


str = "arvindkumar"

for char in str:
    if(char == 'a'):
        print("a found")
        break
    print(char)

print("END")

#Lets Practice
# Question 01

nums =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        break
    idx += 1

#Question no 02  ( RANGE )

Seq = range(10)

for i in range(10):
    print(i)

for i in range(2, 10): #range(start, stop)
    print(i)

for i in range(2, 100, 2): #range(start, stop, step)
    print(i)

#{02 using for and range}

#print number 100 to 1.
for i in range (100, 0, -1):
    print(i)

#print the multiplication table of a number n.
n = int(input("entr a number : "))

for i in range(1, 11):
    print(n * i)

#PASS STATEMENTS (null)

for i in range (5):
    pass
print("some uneful work")


#LETS PRACTICE

#01 WAP to find the sum of the first n natural munber. (using while)
n =  5

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum =", sum)


# 03WAP to find the factorial of first n number (using for)
n =  5
fact = 1
i = 1   #(i= inisalise)
while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)