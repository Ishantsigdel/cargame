# import module as mo
from module import sum as sm, diff as df, product as pd,divide as di, modulus as mo, floordiv as fd



num = int(input("enter a number from 1 to 7:"))
if num == 1:
    print("The sum is:",sm((int(input("enter a number: "))),(int(input("enter a number: ")))))
if num == 2:
    print("The diff is:",df ((int(input("enter a number"))),(int(input("enter a number")))))
if num == 3:
    print("The product is:",pd((int(input("enter a number"))),(int(input("enter a number")))))
if num == 4:
    print("The  quotient is:",di((int(input("enter a number"))),(int(input("enter a number")))))
if num == 5:
    print("The modulus is:", mo((int(input("enter a number"))),(int(input("enter a number")))))
if num == 6:
    print("The floordivision is:",fd((int(input("enter a number"))),(int(input("enter a number")))))











# print("select 1 for sum: ",sm(2,3))
# print("select 2 for diff: ")
# print("select 1 for sum: ")

# mo.sum(2,3)
# mo.diff(2,3)
# mo.product(2,3)
# mo.divide(9,3)
# mo.modulus(-8,3)
# mo.floordiv(10,3)


