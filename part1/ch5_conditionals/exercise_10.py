# Exercise: 10
# Task: Solve a quadratic equation ax² + bx + c = 0 using the quadratic formula

from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print("The roots are", x1, "and", x2)

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
