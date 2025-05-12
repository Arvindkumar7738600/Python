#realational operators
a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b


#relation operators
a = 20
b = [8]

print(a == b) #false
print(a != b) #true
print(a >= b) #false
print(a <= b) #true


#assignment operators
num = 10
num +=10  #10+10=20
print("num :",num)

num = 10
num -=10  #10+10=0
print("num :",num)

num = 10
num *=10  #10+10=100
print("num :",num)

num = 10
num %=10  #10+10=0
print("num :",num)

num = 10
num **=10  #10+10=10000000000
print("num :",num)

#logical operators
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("and operators:", val1 and val2)

val1 = True
val2 = True
print("and operators:", val1 and val2)

val1 = False
val2 = False
print("and operators:", val1 or val2)

print("and operators:", (a == b) or (a > b))

#types of conversion
a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)
#print(a + b) this is not run bcz int and float are not add

a = int("2")
b = 4.25

print(type(a))
print(a + b)
#type casting tab work karti jab koi variable new fit ho
#fromm one data type to convert to another data type

a = 3.14
a = str(a)

print(type(a))

#INPUT IN PYTHON
name = input("enter your name:")
print("wellcome", name)

name = input("enter your age:")
print("entered", name)

val = input("enter some value: ")
print(type(val) ,val)

#finally

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks; "))

print("wellcome", name)
print("age", age)
print("marks", marks)


name = ("arvind")
print(name)

