str1 = "This is a string."
str2 = "Arvindkumar"
str3 = """this is a string"""

'this is arvindkumar" tutorial'

# \n means  NEXT LINE
#\tab means MORE SPACE
str1 = "This is a string. We are creating it in python."
print(str1)

str1 = "This is a string.\n We are creating it in python."
print(str1)

#BASIC CONCATENTION
str1 = "arvind"
str2 = "kumar"
final_str = (str1 + str2)
print(final_str)


#length of str:-  len(str)

str1 = "arvind"
print(len(str1))
str2 = "kumar"
print(len(str2))
final_str = (str1 +" " + str2)
print(final_str)
#LENGTH MAI SPACE V COUNT HOTA HAI
print(len(final_str))


#indexing :- access character postion
str = "apna college"
ch = str[0]
print(ch)
ch1 = str[6]
print(ch1)

#slicing :- Acccessing parts of a string   str[starting_idx : ending_idx]
str = "apna college"
print(str[1:4])

str = "apna college"
print(str[3:12])

# part 2 :- negative index ~ backward counting
str = "apple"
print(str[-3 : -1])
print(str[-5 : -2])


#string functions
#str = "i am a coder"

#str.endswith("er")
str = " I am studyinf=g python from itself"
print(str.endswith("self"))

#str.capitalize() capitalizes 1st char
str = "i am studying python from ApnaColllege"
#print(str) # dubara ese change nhi hoga char
#change karne ke liye nayi function mai
str = str.capitalize()
print(str)



#str.replace(old, new)replaces all occurrences of old 
str = "i am studying python from ApnaColllege"
print(str.replace("python", "javascript"))



#str.find(word)return 1st index of 1st occurrences
str = "i am studying python from ApnaColllege"
print(str.find("o"))
print(str.find("A"))
print(str.find("q"))


#str.count("am")ciunts the occurrence of substr
str = "i from studying python from ApnaColllege"
print(str.count("from"))  #kitne baar from hai



#lets Practice Question
#WAP to input users first nme and print its length.
name = input("enter your name")
print("length of your name is ", len(name))

#question 
#WAP to find occurrence of '$' in a string.
str = "Hi, $ symbol this is known as dollar $9923"
print(str.count("$")) #answe is 2






#conditional statements 
#if-elif-else(SYNTAX)

#if ka mtlb yeh condition ho sakta hai 
#elif ka mtlb 1st statement agr sahi nhi huwa toh second line mai chek kaarna
age = 21

if(age >=18):
    print("can vote and apply for license")

age = 15

if(age <=18):
    print("not for vote and not apply for license")




    
    light = "green"

    if (light == "red"):
        print("stop")
    elif(light == "green"):
        print("go")
    elif(light == "yellow"):
        print("look")

    print("end of code")


    
    num =5 

    if(num >2):
        print("greater than 2")
    elif(num >3): #elif mai agr statemet 1 true hai toh phir statement 2 nhi krega cheak
        print("greater than 3")


#else (agr uper ki sari ki sari statement fale hai tab else run kregi)
    
    light = "blue"

    if (light == "red"):
        print("stop")
    elif(light == "green"):
        print("go")
    elif(light == "yellow"):
        print("look")
    else:
        print("light is broken and damage")

    print("end of code")

    age = 12
    if(age >= 18):
        print("can vote") #indentation space
    else:
        print("cannot vote")


#condtional Statements
#grade students based on marks
#given data marks >=90, grade ="A"
#90>marks>=80,gtade ="B"
        
    marks = int(input("enter student marks : "))

    if(marks >= 90):
        grade = "A"
    elif(marks >= 80 and marks < 90):
        grade = "B"
    elif(marks >= 70 and marks < 90):
        grade = "C"
    else:
        grade = "D"

    print("grade of the student ->", grade)

#NESTING
age = 35

if(age >= 18):
    if(age >= 70):
        print("cannot drive")
    else:
        print('can drive')
else:
    print("cannot drive")



#lets Practice Question
#1.wap to check if a number entered by the users is odd or even

num = int(input("enter number: "))

rem = num % 2

if(rem == 0):
    print("even")
else:
    print("odd")


#2.Wap to find greatest of 3 number by the user.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
   print("second number is largest", b)
else:
    print("third is largest", c)


#3.Wap to check if a number is a multiple of 7 or not.

x = int(input("enter a number: "))

if(x % 7 == 0):
    print("this is multible of 7")
else:
    print("this not a multiple of 7")

#04 wap to check if  number is a multiple of 4 or not.

x = int (input("enter a number: "))

if(x % 4 == 0):
    print("this is multiple of 4")
else:
    print("this is not multiple of 4")
    