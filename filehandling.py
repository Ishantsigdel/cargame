# f = open("filehandling.py", "r")
# value = f.read()
# print(type(value))

# f = open("filehandling.txt", "r")
# print(f.readline())
# print(f.readline())

# f = open("filehandling.txt", "r")
# print(f.readline())
# f.close()

# f = open("filehandling.txt", "r")

# print(f.read(6))

# f = open("filehandling.txt", "r")

# f.read(42)

# print(f.read(7))

# f.close()


# f = open("filehandling.txt", "r")
# f.readlines()

# f = open("filehandling.txt", "w")
# f.write("Hi helloooooooo ")
# f.close()

# f = open("filehandling.txt", "r")
# print(f.read())

# file_path = 'filehandling.txt'
# with open(file_path, 'r') as file:
#     content = file.read()
# print(content)


# a = ["hello\n","world\n"]
# f.writelines(a)
# f.writelines("hello\n")
# f.writelines("world\n")


# import os
# if os.path.exists("filehandling.txt"):
#     os.remove("filehandling.txt")
# else:
#     print("The file donot exixt.")



# f = open("filehandling.txt", "r")
# header = f.readline().strip()

# print("Name Age Science Maths English Totalmarks")
# f = open("filehandling.txt", "r")

# header = f.readline().strip()

# print("Name   Age  Science  Maths  English  TotalMarks")
# print(" ")
# for line in f:
#     name, rest = line.split(" ", 1)
#     age, science, maths, english = map(int, rest.split(","))
    
#     total_marks = science + maths + english
#     print(f"Name: {name}, age: {age}")
    

# f.close()

# f = open("filehandling.txt", "a")
# f.write("Hi, I am ishant sigdel.")

# f = open ("filehandling.txt", "r")
# print(f.read()) 
# f.close()
# value = (f.read())
# print(type(value))

# import csv


# file_path = ''
# with open (file_path, mode = 'w', newline = '') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'Age', 'city'])
#     while True:
#         if input ("enter 1 for exit") == '1':
#             break
#         name = input("enter a name:")
#         age = int(input("enter the age:"))
#         city = input("enter a cityname:")


#         ra = [name.age.city]
#         csv_writer.writerow()
# import csv
# file_path = 'data.csv'

# with open(file_path, mode = "r")as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         print(row)

# import csv

# file_path = 'data.csv'

# with open(file_path, mode = 'r') as f:
#     csv_reader=csv.dictreader(f)
#     for row in csv_reader:
#         print(row['Name'], row['Age'], row['city'])

# import csv

# data = [
#     {'Name':'Alice', 'Age': 23, 'City':'London'},
#     {'Name':'Ishant', 'Age': 23, 'City':'Kathmandu'},
#     {'Name':'Niraj', 'Age': 23, 'City':'Darchula'}
# ]




# file_path = 'data.csv'
# fieldnames = ['Name','Age','City']

# with open(file_path, mode = 'w', newline = '') as f:
#     writer = csv.DictWriter(f, fieldnames = fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,5,7,11]

x1=[6,7,8,9,10]
y1=[2,3,5,7,11]

plt.plot(x,y, marker= 'o', linestyle= '--', color ='b', label='prime_numbers')
plt.plot(x1,y1, marker = 'o',linestyle = '-' ,color = 'r',label = ' Numbers' )

plt. xlabel('x Axis')
plt. ylabel('y Axis')
plt.title('Prime numbers plot')

plt.legend()
plt.show()