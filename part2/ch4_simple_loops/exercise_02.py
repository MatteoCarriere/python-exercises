# Exercise: 2
# Task: Repeatedly ask for a number, print its square root, report invalid if negative, exit on 0
 
from math import sqrt
 
while True:
   int_num = int(input("Please type in a number: "))
   if int_num > 0:
        print(sqrt(int_num))
   elif int_num < 0:
        print("Invalid number")
   elif int_num == 0:
        print("Exiting...")
        break
 