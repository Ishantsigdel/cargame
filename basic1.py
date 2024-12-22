# val = " I am Ishant"
# print ("Ishant" in val)
# print ("ishant" in val)
# print(" " in val)



# a=5
# b=6

# a =5 
# a = a + 3
# a += 3
# print(type(a))

# b = "yuu"
# b = b - 3
# b -= 3
# print(type(b))

# print (a < b  and a < c)
# print(a > b or a > c )
# print (a >= b or a >= c)
  

# c=3
# # if (a>b) and (a>c):
# #  print("A is greatest")
# # elif (b>a) and (b>c):
# #  print("B is greatest")
# # else: 
# #  print("C is greatest")

# greatest = max(a, b, c)

# print(f"The greatest number among {a}, {b} and {c} is {greatest}.")
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = float(input("Enter the third number: "))


# sum = a + b + c
# print(f"The sum of {a}, {b} and {c} is {sum}")

# if (a>b) and (a>c):
#   print("A is greatest")
# elif (b>a) and (b>c):
#   print("B is greatest")
# else: 
#  print("C is greatest")

# x = [1, 3, 4 ]
# print(type(x))

# x = (1, 3, 4 )
# print(type(x))

# x = "hello world"
# print(type(x))

# y = 28.487
# print(type(y))

# z = 1j
# print(type(z))

# a = ["Apple", "banana", "cherry"]
# print(type(a))

# a = ("Apple", "banana", "cherry")
# print(type(a))

# x = range(10)
# print(type(x))

# x = {
#     "name" : "Ishant",
#     "age" : 21

# }
# print(type(x))

# c = {"name", "age" }
# print(type(c))

# d = frozenset({"name", "age"})
# print(type(d))

# x = True
# print(type(x))

# d = None
# print(type(d))

# x = ["apple", "banana"]
# print("apple" in x)

# x=["apple", "banana"]
# y=["apple", "banana"]
# z = x

# print(x is z)


# value_x = 5
# value_y = 6

# print("value_x == value_y", value_x == value_y)

# Create a program that asks the user for their name and age, then prints a greeting like
# name = input("Enter your firstname: ")
# age = int(input("Enter your age: "))

# print(f"Hello {name}, you are {age} years old.")
# Write a program to swap the values of two variables without using a third variable.
# x = 1
# y = 2


# x, y = y, x
# print(x)
# print(y)
# Declare a variable for your favorite number and print its square.
# a = 10 

# print(f"The square of {a} is: ",a * a)

# a = int(input("Enter your favourite number: "))


# print(f"The square of {a} is: ",a ** 2 )
# Write a program that checks whether a number entered by the user is even or odd.

# num1 = int(input("Enter a number: "))

# if(num1 % 2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")
# Ask the user for a number and check if it's positive, negative, or zero.
# num = int(input("Enter a number: "))

# if(num > 0):
#     print(f"The {num} is positive.")
# elif(num < 0):
#     print(f"The {num} is negative.")
# else :
#     print(f"The {num} is zero")


# value = input("Enter a number: ")

# if value.isdigit():
#     num = int(value)
#     print("Converted to int: ", num)
# elif value.isalpha():
#     num = str(value)
#     print("Converted to string ", num)
# elif '.' in value:
#    num = float(value)
#    print("Converted to float: ", num)
# else:
#     print("Invalid number input")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}.")
# else:
#     print(f"{num1} and {num2} are equal.")

# a = int(input("Enter  number a: "))
# b = int(input("Enter  number b: "))
# c = int(input("Enter  number c: "))

# if a > b and a > c:
#     print(f"{a} is greatest")
# elif a == b and c == 0:
#     print(f"{a} and {b} are equal when c is zero.")
# elif a == b and b == c and a != 0:
#     print (f"{a}, {b} and {c} are equal")
# else:
#     print("Invalid")

# x = int(input("Enter a number: "))
# if x >= 0 and x < 10:
#  print (x,"is a positive single digit number:")
# elif x < 0:
#    print(x,"is not a positive number:")
# else:
#   print(x,"is positive multiple digit number:")
# Write a program to print the numbers from 1 to 10 using a for loop.

# for x in range(1, 111):
#    print(x)
# Create a program to calculate the sum of all numbers from 1 to n, where n is entered by the user.

# n = int(input("Enter a positive number(n): "))
# total_sum = 0

# for number in range(1, n+1):
#    total_sum += number

# print(f"The sum of total number between  1 and {n} is {total_sum}.")
# Print the multiplication table for a number entered by the user.

# num = int(input("Enter a number: "))

# print(f"Multiplication for {num} is :")

# for n in range(1, 11):
#    print(f"{num} x {n} = ", num * n )
# Write a program to count the number of vowels in a string entered by the user.

# text = input("Enter a string: ")

# vowels = "aeiouAEIOU"

# vowel_count = 0

# for char in text:
#    if char in vowels:
#       vowel_count += 1

# print(f"The total number of vowels in {text} is : {vowel_count}") 

# name = [ 1, "abc", 2, 2.5, True, "apple", "cherry"]

# for x in name:
#     if x == "apple":
#         print(x)

# for x in range (1, 21, 2):
#     print(x)

# odd_count = 0
# even_count= 0
# for num in range(20):
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
    
# print(f"Number of even numbers: {even_count}")
# print(f"Number of odd numbers:   {odd_count}")
# x = 2
# even_count = 0
# while x < 21:   
#     if x % 2 == 0:
#         print("Even numbers:",x)
#     even_count += 1

#     print("Final count :", even_count)


# x =2
# even_count = 0


# while x < 21:
#     if x % 2 == 0:
#         print("Even number",x)
#         even_count += 1


#     x +=1

# print(f"Total even numbers are: {even_count}")


# x =1 
# odd_count=0

# while x < 110:
#     if x % 2 != 0:
#         print("Odd number: ", x)
#         odd_count += 1
#     x +=1



# print(f"Total odd numbers: ", odd_count)

#Write a function add(a, b) that returns the sum of two numbers.

# def sum(a, b):
#     return a + b
   

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# result = sum(num1, num2)
# print(f"The  sum of {num1} and {num2} is {result}")

# num = int(input("Enter a number: "))
# for num in range(20):
#     if num == 5:
#         break
#     print("Num", num)

# print("Outside the loop.")

# sum = 0

# for num in range(1, 31):
    
#     if num == 10:
#         continue
#     sum += num

# print("The sum of all numbers between 1 and 30 except 10 is: ", sum)
# x = 4
# y = 8
# print("x =",x)
# print("y =",y)
# z = x
# x = y
# y = z
# print("x =",x)
# print("y =",y)

# a, b = b, a
# print("a = ", a)
# print("b = ", b)
# x = 4
# y = 9
# print("x =",x)
# print("y =",y)
# x = x + y
# y = x - y
# x = x - y


# print("x =",x)
# print("y =",y)
# i = 1
# while i <= 15:  
#     j = 1
#     while j <= i:  
#         print(j, end=" ")  
#         j += 1  
#     print() 
#     i += 1  

# for i in range(1, 6):  
#     for j in range(1, i+1   ): 
#         print(j, end="")  
#     print()  

# var = "Hello world"

# print(var[1])
# print(var[2])
# print(var[3])
# print(var[4])
# print(var[5])
# print(var[6])
# print(var[7])
# print(var[8])
# print(var[9])
# print(var[10])

# var = "Hello worldeee"

# count_e = var.count('e')
# print(count_e)

# string = "Hello worldeeeeee"
# count_e = 0
# for char in string:
#     if char == "e":
#         count_e += 1
# print("Total number of e:",count_e)

# var = "Hello world"
# print(len(var))
# count = 0
# for x in range(len(var)):
#     if var[x] == "e":
#         count += 1
# print(count)

# var = "Hello world world"
# a = 0
# for x in var:
#     a = a + 1

#     print(x, a)

# var = "Hello world world"

# print(var[6:11  ])
# var = "Hello world world"
# print(var[0:15:3])
# print(var[6:0:-1])

# var = "Hello world"
# var = "h" + var[1:]
# print(var)

# a = "  ########   hello world    "
# print(a.lstrip("#"))

# b = "HELLO world"
# print(a.lower())

# c = "hello world"
# print(c.upper())

# d = "Hello world"
# print(a.title())

# a = "hello world! how is is going"
# print(a.split())

# b = " "
# c=  ["Hi", "world", "whats", "up"]
# print(b.join(c))

# var = "1324"
# print(var.isdigit())

# a = int(input("Enter a number:"))
# b = int (input("ENter a number:"))
# c = f"The sum of {a} and {b} is {a + b}"
# print(c)

# a = "hello {}"
# print(a.format("World"))


# var = "#############hello####world#######"
# var1 = var.strip("#")
# print(var1.replace("#",''))

# # var = "hello world"
# # var1 = "#############" + var.replace(" ","####") + "#######"
# # 
# total_length = len(var)
# removing_left_side_len = len(var.lstrip("#"))
# left_side_value = total_length - removing_left_side_len 

# removing_right_side_len = len(var.rstrip("#"))
# right_side_value = total_length - removing_right_side_len 

# numbers = [1, 2, 3, 4, 5 ]
# fruits = ["apple", "Banana", "Orange"]
# mixed_list = [10, 'hello ', True, 3.14 ]

# print(fruits[1:2])
# print(mixed_list[2:])

# fruit_list = ["apple", "banana", "orange"]
# fruits_list[1:3] = "mango", "pineapple", "sjdvn"
# fruit_list.insert(1, "mango")
# print(fruit_list)
# fruit_list.insert(2,"pineapple")
# print(fruit_list)
# print(fruit_list[4])


# fruit_list = ["apple", "banana","orange"]
# fruit_list.append("mango")
# print(fruit_list)
# car_list = ["BMW","suzuki","Honda"]
# fruit_list = ["apple", "banana","orange"]

# car_list.extend(fruit_list)
# print(car_list)

# mixed = [1, "apple", "banana", 2,5,7, "cherry", True, 4,9,10]
# even_list = []
# odd_list = []
# even_numbered_string =[]
# odd_numbered_string = []

# for i in range(11):
#     print(mixed[i])
#     if type(mixed[i]) == int and mixed[i] % 2 == 0:
#         even_list.append(mixed[i])
#     elif type(mixed[i]) == int and mixed[i] % 2 != 0:
#         odd_list.append(mixed[i])
#     elif type(mixed[i]) == str and (len(mixed[i]) % 2) == 0:
#         even_numbered_string.append(mixed[i])
#     elif type(mixed[i]) == str and (len(mixed[i]) % 2) != 0:
#         odd_numbered_string.append(mixed[i])



# print("Even list", even_list)
# print("odd list", odd_list)
# print("Evennumberedlist", even_numbered_string)
# print("odd numberedlist", odd_numbered_string)


# mixed = [1, "apple", "banana", 2,5,7, "cherry","aeio", True, 4,9,10]

# vowels = "aeiou"

# for item in mixed:
#     if type(item) == str:
#         for char in item:
#             if char.lower() in vowels:
#                 print(char, end=' ')

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# fruits = ["apple", "banana", "cherry"]
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# Games = ["football", "basketball", "cricket"]
# index = 0
# while index < len(Games):
#     print(Games[index])
#     index += 1

# games = ["football", "basketball", "cricket"]
# games.remove("basketball")
# print(games)

# games = ["football", "basketball", "cricket"]
# games.pop(0)
# print(games)
# games = ["football", "basketball", "cricket"]
# del games[2]
# print(games)
# games = ["football", "basketball", "cricket"]
# games.clear()
# print(games)


# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# del thislist[0]
# del thislist[1]
# del thislist[3]
# thislist.pop(0)
# thislist.pop(1)
# thislist.pop(3)
# if thislist == "cheery" and "grapes":
# thislist.remove("apple")
# thislist.remove("banana")
# thislist.remove("banana")
# thislist.remove("banana")
# thislist.remove("apple")
# case1 =[]
# for items in thislist:
#     if thislist.count(items) == 1:
#         case1.append(items)
# print("case1",case1)

# case2 = []
# for items in thislist:
#     if thislist.count(items) > 1:
#         case2.append(items)
# print("case2", case2)

# case3 = []
# for items in thislist:
#     if items not in case3:
#         case3.append(items)
# print("case3", case3)

# thislist = [x for x in thislist if "a" in x]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]


# fruits = [ x for x in thislist if "c" in x]
# print(fruits)
# numbers = [1,2,3,4,5,6,7]
# numbers = [ x * 2 for x in numbers if x % 2 == 0 ]
# print(numbers)

# numbers = [1,2,3,4,5,6,7]
# even_numbers =[]
# for x in numbers:
#     if x % 2 == 0:
#        even_numbers.append(x * 2)
# print("even_numbers", even_numbers)
# numbers = [1,2,3,4,5,6,7]

# numbers = [x if x % 2 == 0 else "false" for x in numbers]
# print(numbers)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],

# ]

# x = matrix[0]
# print(x)
# print(type(x))
# print(x[1])


# y = matrix[1]
# print(matrix[1][2])
# add all numbers of matrix using loops 
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],

# ]

# sum = 0
# for row in matrix:
#     for num in row:
#         sum += num
# print("The total sum is : ",sum)

# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# thislist.sort(reverse=True)
# print(thislist)

# new_list = sorted(thislist)

# newlist = [1, 2, 3]
# list2 = newlist.copy()
# list2.append(5)
# list2.append(6)
# list2.append(7)

# print("list2", list2)
# print(newlist)
# newlist = [1, 2, 3]
# list2 = newlist[:]
# list2.append(6)
# print(list2)

# a = ["HI"]
# b = [4,5,6]
# c = a + b
# print(c)

# a = ("apple","banana","cherry")
# b = list(a)
# b.append("mango")
# a = tuple(b)
# print(a)

# fruits = ("apple","banana","cherry", "strawberry")

# (green, *blue, yellow ) = fruits
# print(green)
# print(blue)
# print(yellow)

# a = {}
# print(type(a))

# my_set = {"a","b","c","4","5",6,7}
# for x in my_set:
#     print(my_set)

# my_set = {"apple","banana","cherry","apple"}
# print(my_set)

# my_set = {"apple","banana","cherry",""}
# my_set.add("apple")
# print(my_set)

# fruits = {"apple","banana","cherry","apple" }
# cars = { "BMW", "Honda", "Suzuki"}
# fruits.update(cars)
# print(fruits)
# fruits.discard("pineapple")


# fruits = {"apple","banana","cherry","apple" }

# x = fruits.pop()
# print(x)
# print(fruits)

# set1 = {"a", "b", "c"}
# set2 = { 1,2,3,"b"}
# set3 = {"apple", "banana", "cherry", "apple"}
# set4 = set1|set2|set3
# print(set4)



# set1 = {"a", "b", "c"}
# set2 = { 1,2,3,"b"}
# set4 = set1 & set2 
# print(set4)

# set2 = { 1,2,3,"b","c"}
# set1 = {"a", "b", "c"}
# set3 = { "a","b", "c","d"}
# set1.intersection_update(set2,set3)
# print(set1)

# set1 = {2,3,4,5}
# set2 = {1,2,3,4,5}
# set4 =  {1,2,3,4}

# set3 = set1^set2^set4
# print(set3)

# fruits = {"apple","banana","cherry"}
# cars = {"BMW", "Honda", "Suzuki"}
# set = fruits.isdisjoint(cars)
# print(set)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5}

# set = set1.issubset(set2)
# print(set)

# x = ((1,2), (2,3),(4,5),(6,7))
# which tuples value is largest print it
# Tuple(1,2) and sum is 3.

# empty_dict = { }
# my_dict = {
#     "name" : "IShant",
#     "age" : 23,
#     "city" : "kathmandu"
# }
# print(my_dict["name"])
# print(my_dict.get("address",123))
# my_dict["age"] = 31
# my_dict ["gender"] = "female"
# print(my_dict)

# mixed_dict = {
#     1: "one",
#     "2" : "two",
#     (1,2): "tuple"
# }

# car = {
#     "brand" : "Ford",
#     "model" :  "mustang",
#     "year" : 1963
# }

# x = car.keys()

# print(x)

# car["color"] = "Black"

# print(x)

# x = car.values()

# student = {
#     "name" : "abc",
#     "rollno" : 12,
#     "address" : "ktm"

# }


# for k,v in student.items():
#     if k == "rollno" and v == 12:
#         student["rollno"] = 1
# if student.get("phone_no") == None:
#     student["phone_no"] = 123456
# print(student)
# myfamily = {}
# n = int (input("Enter the number of child:"))

# for x in range(n):
#     name = input("Enter a name:")
#     year = int(input("Enter a year: "))
#     myfamily[f"child{x}"] = {
#         "name" : name,
#         "year" : year
#     }
# (myfamily["child1"]["year"]) = 2007
# print(myfamily)

# record = {
#     1:{
#         "name" : "ishant",
#         "age" : 23,
#         "marks" : {
#             "english" :  70,
#             "Maths" : 80,
#             "Science" : 90

#         }

#     },
#     2:{
#         "name" : "niraj",
#         "age" : 23,
#         "marks" : {
#             "english" :  60,
#             "Maths" : 70,
#             "Science" : 80

#         }

#     },
#     2:{
#         "name" : "niraj",
#         "age" : 23,
#         "marks" : {
#             "english" :  60,
#             "Maths" : 70,
#             "Science" : 80

#         }

#     },
#     2:{
#         "name" : "niraj",
#         "age" : 23,
#         "marks" : {
#             "english" :  60,
#             "Maths" : 70,
#             "Science" : 80

#         }

#     },
#     3:{
#         "name" : "dipak",
#         "age" : 23,
#         "marks" : {
#             "english" :  70,
#             "Maths" : 90,
#             "Science" : 80

#         }
     

# }


# def addition(a,b):
#     sum = a + b
#     return sum


# result = addition(2,3)

# print(result)

# def get_stats(numbers):
#     min_value = min(numbers)
#     max_value = max(numbers)
#     sum_value = sum(numbers)
#     return min_value, max_value, sum_value

# numbers = [1,2,3,4,5]
# result = get_stats(numbers)
# print(result)
# print(type(numbers))

# print("minimum" , min_value)

# def get_stats(numbers):
#     return{
#         'min' : min(numbers),
#         'max' : max(numbers),
#         'sum' : sum(numbers)

#     }

# numbers = [1,2,3,4,5]
# stats = get_stats(numbers)
# print("maximun", )

# def substraction(a,b = 0):
#     difference = a - b
#     return difference

# result = substraction(4,2)
# print(result)

# Without parameter
# def substraction():
#     a = 6
#     b = 3
#     result = a - b
#     return result

# res = substraction()
# print(res)

# with parameter without return
# def substraction(a,b):
#     result = a -b
#     print("result",result)

# substraction(7,3)
# without parameter without return
# def substraction():
#     a = 9
#     b = 4
#     result = a -b
#     print("result", result)

# substraction()

# def My_function():
#     x = 5
#     print("Inside function ",x)
#     return x


# My_function()
# x = 15
# print("outside function: ", x)


# x = 5

# def My_function():
#     global x
#     x = x + 5
#     print("Inside function ",x)
#     # return x


# My_function()
# print("outside function: ", x)

# create function to find the number is odd or even.
# create function to check palindrome .
# create function to create armstrong
# armstrong = 123
# 1^2+2^2+3^2 = 123


# def odd_even (a):
#     if a % 2 == 0:
#         return(f"{a} is even.")
#     else:
#         return(f"{a} is odd.")
    

# num = int(input("Enter a number:"))
# oddeven = odd_even(num)
# print(oddeven)x

# def check_palindrome(word):
#     word_arranged = word.replace(" ","").lower()
#     if word_arranged == word_arranged[::-1]:
#         return(f"{word} is a palindrome")
#     else:
#         return(f"{word} is not a palindrome")
    
# string = input("Enter a word: ")
# palindrome = check_palindrome(string)
# print(palindrome)


# def is_armstrong(number):
#     digits = list(map(int, str(number)))
#     num_digits = len(digits)
#     armstrong_sum = sum(digit ** num_digits for digit in digits)
#     return armstrong_sum == number

# test_number = 134
# if is_armstrong(test_number):
#     print(f"{test_number} is an Armstrong number.")
# else:
#     print(f"{test_number} is not an Armstrong number.")
        
# def my_function(*kids):
#     print("The youngest child is " +kids[0])

# my_function("ishant", "ishan","isha")
# def my_function(**kids):
#     print("His last name is " +kids["lname"])

# my_function(fnamne = "ishant", lname = "Sigdel")

# x = lambda a : a + 10
# print(x(5))
    
# x = lambda a, b: a * b
# print(x(5,6))

# x = lambda a,b,c : a + b + c
# print(x(2,3,4))

'''0 1 1 2 3 5 8 ......... '''

# class person :
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#     def great(self):
#         print(f"Hi my name is {self.name} and i am {self.age} years old. ")

# p1 = person ("ishant", 23)
# p2 = person("isha", 23)
# p3 = person("nishan", 13)


# p3.great()

# class rect_area:
#     def __init__(self, length,breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print("Area: ", self.length * self.breadth)

# rectangle_box = rect_area(10, 5)
# rectangle_window = rect_area (20, 10)

# rectangle_box.area()

# without parameter
# class rect_area:
       

#     def area(self,length,breadth):
#         print("Area: ", length * breadth)

# rectangle_box = rect_area()
# rectangle_window = rect_area ()

# rectangle_box.area(10,20)
# with return type
# class rect_area:
#     def __init__(self, length,breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         result = self.length * self.breadth
#         return result
    
# rect_box = rect_area(4,5)
# result_rect_box = rect_box.area()

# rect_box.area()

# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class dog(Animal):
#     def bark(self):
#         return "dog barks"

# my_dog = dog()
# print(my_dog.speak())
# print(my_dog.bark())

# class A:
#     def method_A(self):
#         return "method A"
# class B:
#     def method_B(self):
#         return "Method B"

# class C(A, B):
#     def method_C(self):
#         return "Method C"

# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())

# class A:
#     def method_A(self):
#         return "method A"
# class B(A):
#     def method_B(self):
#         return "Method B"

# class C(B):
#     def method_C(self):
#         return "Method C"

# obj_C = C()
# # print(obj_C.method_A())
# # print(obj_C.method_B())
# print(obj_C.method_C())

# class rectangle:
#     def __init__ (self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
# class square(rectangle):
#     def __init__ (self, length):
#         super().__init__(length,length)

# square = square(5)

# print("Area of square ", square.area())

# def  divide():
#     try:
#         x = int(input("Emter a number for x: "))
#         y = int(input("Emter a number for y: "))
#         result = x / y 
#         print("result: ",result)

#     except ZeroDivisionError as e:
#         print("y cannot be 0 ")

    

# divide()
# def  divide():
#     try:
#         x = int(input("Emter a number for x: "))
#         y = int(input("Emter a number for y: "))
#         result = x / y 
#         print("result: ",result)

#     except ZeroDivisionError as e:
#         print("Y cannot be 0")
#         x = int(input("Emter a number for x: "))
#         y = int(input("Emter a number for y: "))
#         result = x / y 
#         print("result: ",result)

#     except ValueError:
#         print("You have entered a character.")
        

    

# divide()

# def  divide():
#     try:
#         x = int(input("Emter a number for x: "))
#         y = int(input("Emter a number for y: "))
#         result = x / y 
#         print("result: ",result)

#     except Exception as e:
#         print(f"Error: {e}")
#         x = int(input("Emter a number for x: "))
#         y = int(input("Emter a number for y: "))
#         result = x / y 
#         print("result: ",result)

# divide()

# try:
#     print("a")
# except NameError:
#         print("variable is not defined")
# except:
#         print("Something else went wrong")

# x = int(input("Enter a name: "))
# if x < 0:
#     raise  Exception("No number less than zero.")


# try:
#         x = input("Enter a name: ")
#         if x == int:
#             raise Exception("Name cannot be a number: ")

# except Exception as e:
#         print(e)
#         x = input("Enter a name:")

# class negative_error (Exception):
#     def __init__(self, message):
#         super().__init__(message)
        
# class zero_error (Exception):
#     def __init__(self, message):
#         super().__init__(message)

# x = int(input("Enter the age:"))

# try:
#     if x < 0:
#         raise negative_error("Sorry, no numbers less zero.")

#     elif x == 0:
#         raise  zero_error ("Sorry, age cannot be zero.")

# except negative_error as e:
#     print(f"Error:{e}")
#     x = int(input("Enter the age:"))
#     print("The age is :", x)

# except zero_error as e:
#     print(f"Error:{e}")
#     x = int(input("Enter the age:"))
#     print("The age is :", x)

# try:
#     x = int(input("Enter the number first: "))
#     y = int(input("Enter the number second: "))
#     result = x / y
#     print("result", result)

# except ZeroDivisionError as e:
#     print(e)
#     print("Zero value cannot be entered.")
#     x = int(input("Enter the number first: "))
#     y = int(input("Enter the number second: "))
#     result = x / y
#     print("result", result)

# import traceback
# def divide():
#     print("Hello")
#     try:
#         x = int(input("Enter the number first: "))
#         y = int(input("Enter the number second: "))
#         result = x / y
#         print("Result :",result)

#     except Exception as e:
#         traceback.print_exc()
#         print(f"Handles all exception")
    
# divide()

# def area_of_circle(r):
#     Area = 3.14159 * (r**2)
#     print("Area of circle : ", Area)
#     return Area


# area_of_circle(7)


# def even_or_odd (a):
#     if a % 2 == 0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")

# even_or_odd(int(input("Enter a number: ")))


# def count_vowels(char):
#     vowel_count = 0
#     vowels = "aeiouAEIOU"
#     for x in char:
#         if x in vowels:

#             vowel_count += 1

#     print("Vowel count is :",vowel_count)



# count_vowels("Ishant")


# def is_palindrome(char):
#     cleaned_string = ''.join(filter(str.isalnum, char)).lower()
#     if cleaned_string == cleaned_string[::-1]:
#         print("True. It is pallindrome.")
#     else:
#         print("False. It is not a pallindrome.")
        

# is_palindrome(input("Enter a string:"))    

# import pandas as pd


# #  dict into dataframe
# data = { 'Name': ["Ishant","sigdel","Nishant"],
#         'Age':[25, 30,35],
#         'City':["Kathmandu","Dharan","pokhara"]
#        }

# df = pd.DataFrame(data)
# print(df)
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head())

# import pandas as pd
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df.to_string)


# import pandas as pd
# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)

# import pandas as pd 
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'], format="mixed")
# print(df.to_string())
# df.loc[7, 'Duration'] = 50
# print(df)
# for x in df.index:
#     if df.loc[x,'Duration' ] > 120:
#         df.loc[x, 'Duration'] = 100
#     print(df)

# for x in df.index:
#     if df.loc[x,"Duration"] > 200:
#         df.loc[x, "Duration"] = 50
#     print(df)


# print(df.duplicated())
# df.drop_duplicates(inplace = True)
# print(df)

# numbers = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)


# def squared():

#     numbers = [1,2,3,4,5]
#     for x in numbers:
#         result = x ** 2
#         print(result)

# squared()

# numbers = [1,2,3,4,5]

# def sq(x):
#     return x**2

# squared = list(map(sq,numbers))
# print(squared)

# numbers = [1,2,3,4,5,6,7,8,9]
# odd_numbers = list(filter(lambda x: x % 2 != 0,numbers))
# print(odd_numbers)



# numbers = [1,2,3,4,5,6,7,8,9]
# def even_num(x):
#     return  x % 2 == 0

# evennum = list(filter(even_num,numbers))
# print(evennum)

# from functools import reduce

# numbers = [1,2,3,4,5,6,7,8,9]
# sum = reduce(lambda x,y: x + y , numbers)
# print(sum)

# numbers = [3,4,7,5,2]
# max_num = reduce(lambda x,y:x if x > y else y, numbers )
# print(max_num)

# words = ["Hi"," ","Ishant"," ","sigdel"]
# sentence = reduce(lambda x,y: x + y , words)
# print(sentence)

# numbers = [ 3,4,6,8,9]
# product = reduce(lambda x,y: x * y, numbers, 1) 
# print(product)
# import random
# list = [1,2,3,43,4,5,5]
# random.shuffle(list)
# print(list)

# import math
# sqaure_root = math.sqrt(36)
# print(sqaure_root)

# factorial = math.factorial(5)
# print(factorial)
# import sqlite3
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)')
# conn.commit()
# conn.close()

# conn = sqlite3.connect('data.db')
# c = conn.cursor()
# name = input("Enter the name:")
# age = int(input("Enter the age:"))
# email = input("Enter the email:")
# c.execute("INSERT INTO users(name, age, email) VALUES (?, ?, ?)", (name, age, email))
# conn.commit()
# conn.close()

# conn = sqlite3.connect("data.db")
# c = conn.cursor()
# c.execute("SELECT * FROM users ")
# rows = c.fetchall()
# conn.close()

# for row in rows:
#     print(row)

# conn = sqlite3.connect("data.db")
# c = conn.cursor()
# name = input("Enter a name:")
# age = int(input("Enter the age: "))
# email = input("Enter the email:")
# user_id = int(input("Enter the user id:"))
# # c.execute("UPDATE users SET name = ? WHERE id = ? ", (name, user_id))
# c.execute("UPDATE users SET name=?, age=?, email=? WHERE id = ?", (name, age, email, user_id))
# conn.commit()
# conn.close()

# conn = sqlite3.connect("data.db")
# c = conn.cursor()
# user_id = int(input('Enter the user_id: '))
# c.execute("DELETE FROM users WHERE id=? ", (user_id,))
# conn.commit()
# conn.close()


# c.execute("CREATE TABLE IF NOT EXIXTS users(id INTEGER PRIMARYKEY AUTOUNCREMENT, name TEXT, age integer, email TEXT)")
# name = input("Enter the name:")
# age = int(input("Enter the age:"))
# email = input("Enter the email:")
# c.execute("INSERT INTO users(name,age,email),VALUES(?, ?, ?)", (name,age,email))
# c.execute("SELECT * FROM users")
# rows =c.fetchall()
# conn.close()

# for row in rows:
#     print(row)

# rows = c.fetchall()

# c.execute("UPDATE  users SET name=? WHERE id=?",(name,id))
# c.execute("DELETE FROM users WHERE id=?")

# def prime_number():

#     try:
#         num = int(input("Enter a number: "))
#         if num <= 1:
#             print("Number should be more than 1.")
#             return
#         for i in range(2, int(num ** 0.5)+1):
#             if num % i == 0:
#                 print("Number is not a prime number:")
#                 return
#         else:
#             print("number is a prime number:")
            

#     except ValueError:
#         print("Only numeric values are allowed")


# prime_number()

# def prime_numbers():

#     try:
#         num = int(input("Enter a number:"))
#         if num <= 1:
#             print("Number should be more than 1.")
#             return
#         for x in range(2, int(num ** 0.5) + 1):
#             if num % x == 0:
#                 print(f"{num} is not a prime number.")
#                 return
#         else:
#             print(f"{num} is a prime number.")
            
#     except ValueError:
#         print("Only numerical values are allowed.")

# prime_numbers()



# if num <= 1:

#     for x in range(2, int(num ** 0.5) + 1):
#         if num % x == 0:



# def fizz_buzz():

#     num = range(1,51)
#     for x in num:
#         if x % 3 == 0 and x % 5 == 0:
#             print("fizzbuzz", x)
#         elif x % 3 == 0:
#             print("fuzz", x)
#         elif(x % 5 == 0):
#             print("buzz", x)
        
#         else:
#             print(x)


        

# fizz_buzz()
 
           
# def palindrome_checker(string):
    
#     string = ''.join(char.lower() for char in string if char.isalnum())
#     if string == string[::-1]:
#         print(f"{string} is a palindrome.")
#     else:
#         print(f"{string} is not a palindrome.")


# palindrome = input("Enter a string:")
# palindrome_checker(palindrome)


# def largest_number(numbers):

   
#     largest = numbers[0]
#     for x in numbers:
#         if x > largest:
#             largest = x
#     print(f"{largest} is the largest number.")
            
        
# user_input = input("Enter a list of numbers using space:")
# number_list = [int(i) for i in user_input.split()]
# largest_number(number_list)






def add(x,y):
    return x + y
def substract(x,y):
    return(x - y)
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        print("Invalid input.Must be more than zero.")
    else:
        return x / y



def calculator():
    print("Simple calculator.")
    print("Select operation")


    while True:
        choice = int(input("Enter a number between '1','2', '3', '4' "))
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        if choice in ('1', '2', '3','4'):
            
            if choice == '1':
                print(f"The result is:{add(num1,num2)}")
        else:
            print("invalid input)
            
        



calculator()


    











    

    













        























