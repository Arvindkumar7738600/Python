#FUNCTIONS IN PYTHON :- block of statements that perform a specific task.
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(12, 5)
calc_sum(5, 17)

def calc_sum(a, b):
    return a + b

sum = calc_sum(4, 7) #function call; arguments
print(sum)

# FUNCTIONS OF AVERAGE  3 NUMBERS
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(54, 60, 20)

def print_hello():   #(no input no outputs val)
    print("hello")

print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

#average of 4 numbers

def calc_avg(a, b, c, d):
    sum = a + b + c + d
    avg = sum / 4
    print(avg)
    return avg

calc_avg(12, 34, 54, 34)

#FUNCTIONS IN PYTHON
       #01 Built in functions print() , len() , type() , range()
       #02 User defiened functions

print("arvind","ankita") #sep = " "
print("arvind", end = " ") #end = "\n"
print("arruuu")   #end likhne se ek hi line ma represent o use kiya jata hai.

#DEFAULT PARAMETERS :- Assign a default value to parameter which is used when no arrguments is passed.

def cal_prod(a, b= 3):  #a is not be 0
    print(a * b)
    return a * b

cal_prod(1)


#LETS PRACTICE

#01 WAF to print the length of a list. ( list is the parameters)

name = ["arru", "arvind", "ankita", "sweetie"]
heroes = ["thor", "superman", "ironman", "hulk", "spiderman"]

def print_len(list):
    print(len(list))

print_len(name)
print_len(heroes)

#02 WAF to the elements of a list in a single line. (list is the parameters)

heroes = ["thor", "superman", "ironman", "hulk", "spiderman"]

print(heroes[0], end = " ")
print(heroes[1], end = " ")

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(heroes)


#03 WAF to  find the factorial of n. ( n is the parameters)
n = 5
fact = 1
for i in range (1, n+1):   #normal code
    fact *= i
print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):  #funtions code
        fact *= i
    print(fact)

cal_fact(6)


#04 WAF to convert to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(90)

#05 num  function  odd  sting    even  string






#RECURSION :-when a functons calls itself repeatedly
def show(n):
    if(n == 0):      #condition
        return
    print(n)
    show(n-1)      #phir se 

show(10)

#returns n! FACTORIAL
def fact(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n * fact(n-1)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
   
print(fact(5))


#LETS QUESTION PRACTICE

#01 WAP a recursive functions to calculate the sum of the first n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 
    print(n)
    calc_sum(n-1)

calc_sum(5)



def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)


#02 Write a recursive functions to print all elments in a list(use list and index as parameters)
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "mango", "litchi", "banana"]

print_list(fruits)


#try to repeat this full lecture.