# colors = ["red", "green","yellow","blue"]
# print(colors[0])
# print(colors[3])

# a = 1
# while a <= 10:
#     print(a)
#     a = a + 1


# for x in range(10):
#     print(x)
#     if x == 5:
#         break

# num = [1,2,3,4,5,6,7,8,9,10]
# num.append(11)
# print(num)
# num.remove(5)
# print(num)
# num[num.index(7)] = 17
# print(num)

# fruits = ["apple", "banana", "cherry", "apple", "date", "date", "date"]
# count = fruits.count("apple")
# print(count)
# mount = fruits.count("date")
# print(mount)

# numbers = [4, 8, 15, 16, 23, 42]
# length = len(numbers)
# print(length)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# print("List = ",list3)
# list1.extend(list2)
# print("Merged list = ",list1)
# animals = ["dog", "cat", "rabbit"]
# for x in animals:
#     print(x)
# numbers = [8, 3, 1, 7, 4]
''' Numbers in python can be arranged in ascending and descending order by using sorted function or sort method
'''
# Ascending_num = sorted(numbers)
# Descending_num = sorted(numbers, reverse=True)
# print(Ascending_num)
# print(Descending_num)

# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# words = ["hello", "world", "python", "rocks"]
# words.reverse()
# print(words)
# fruits = ["", "banana", "cherry", "date"]
# for x in fruits:
#     if x == "banana":
#         print(f"{x} is in the fruits.")
# if "banana" and "apple" in fruits:
#     print("yes")
# else:
#     print("no")

# score = int(input("Enter the score: "))
# if score >= 90:
#     print("Grade A : ", score)
# elif score < 90 and score >= 80:
#     print(f"{score} : Grade B")
# elif score < 80 and score >= 70:
#     print(score, ": Grade C")
# else:
#     print("Not Graded")

# year  = int(input("enter a year: "))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.") 
# num  = int(input("enter a number: "))
# if num % 5 == 0 and num % 10 == 0:
#     print(f"{num} is divisible by 5 and 10")
# else:
#     print(f"{num} is not divisible by 5 and 10")

# letter = input("Enter a letter: ")
# vowels = "aeiouAEIOU"
# if letter in vowels:
#     print(f"{letter} is a vowel.")
# else:
#     print(f"{letter} is a consonent.")

# number = int(input("Enter a number: "))

# if number % number == 0 and number % 1 == 0:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# number = int(input("Enter a number: "))

# if number > 1:
#     for i in range(2, int(number**0.5)+1):
#         if number % i == 0:
#             print(f"{number} is not a prime number.")
#             break
#     else:
#         print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# number = int(input("Enter a number: "))

# a, b = 0, 1

# print("Fibonaccci series:")
# while a <= number:
#     print(a, end=" ")
#     a, b = b, a + b

# Write a program that adds all the digits if a number .

# num = input("Enter a number: ")

# sum_digit = 0

# for digit in num:
#     sum_digit += int(digit)

# print(f"The sum of {num} is {sum_digit}")

# numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))

# if len(numbers) < 2:
#     print("Enter more than 1 numbers.")
# else:
#     numbers.sort(reverse = True)

#     second_largest = None
#     for num in numbers:
#         if num != numbers[0]:
#             second_largest = num
#             break
#     if second_largest is None:
#         print("There is no second largest number:")
#     else:
#         print("Second largest is :", second_largest)

# whether the string is a palindrome or not

# string = input("Enter a string: ")

# string_sorted = string.replace(" ","").lower()

# if string_sorted == string_sorted[::-1]:
#     print(f"{string_sorted} is a palindrome. ")
# else:
#     print(f"{string_sorted} is not a palindrome. ")

# string = input("Enter a string: ")
# count = 0
# for x in string:
#     string.count(x)
#     count+= 1

# print(f"The total character in {string} is {count}.")

# string = input("Enter a string:")
# char = input("Enter a character to count: ")

# count = string.count(char)

# print(f"The total count of {char} is {count}.")

# number = int(input("Enter a number: "))

# if number > 1:
#     for i in range(2, int(number ** 0.5)+1):
#         if number % i == 0:
#             print(f"{number} is not a prime number.")
#             break
#     else:
#         print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# import sqlite3

# conne = sqlite3.connect("database.db")
# con = conne.cursor()
# con.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)")
# conne.commit()
# conne.close()

# conne = sqlite3.connect("database.db")
# con = conne.cursor()
# name = input("Enter the name:")
# age =int(input("Enter the age:"))
# email = input("Enter the email:")
# con.execute("INSERT INTO users(name,age,email) VALUES(?, ?, ?) ", (name,age,email))
# conne.commit()
# conne.close()

# conne = sqlite3.connect("database.db")
# con = conne.cursor()
# con.execute("SELECT * FROM users")
# rows = con.fetchall()
# conne.close()

# for row in rows:
#     print(row)



# conne = sqlite3.connect("database.db")
# con = conne.cursor()
# name = input("Enter the name:")
# age = int(input("Enter the age:"))
# email = input("Enter the email:")
# id = int(input("Enter the id:"))
# con.execute("UPDATE users SET name=?, age =?, email=? WHERE id=?", (name,age,email,id))
# conne.commit()
# conne.close()

# conne = sqlite3.connect("database.db")
# conn = conne.cursor()
# id = int(input("Enter the id: "))
# conn.execute("DELETE FROM users WHERE id=?",(id,))
# conne.commit()
# conne.close()


'''
con.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)")
con.execute("INSERT INTO users(name,age,email) VALUES(?, ?, ?) ", (name,age,email))
con.execute("SELECT * FROM users")
con.execute("UPDATE users SET name=?, age =?, email=? WHERE id=?", (name,age,email,id))
conn.execute("DELETE FROM users WHERE id=?",(id,))
'''


# def even_odd():
#     num = int(input("Enter a number:"))

#     print("even" if num % 2 ==0 else "odd")

        
# even_odd()


