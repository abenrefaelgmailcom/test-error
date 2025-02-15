import math

def add(a, b):
    return a + b # 0.1 # 0.99999999999

# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



#a
'''A function that receives a number and a power and returns the number to the given power.
For example: power(2, 4) -> 16'''
def power(a, b):
    return a ** b

#b
'''Add a sqrt function to the calculator that gets a number, returning its root. For example for
9 will return the number 3  because the root 9 is .3 sqrt.math( math import )'''
def sqrt(number: int) -> float:
    return math.sqrt(number)
#c
'''Add a factorial function to the calculator that gets a number, and returns its assembly.
For example for 3 will return 6  because 1 * 2 * 3 = 6
For example for 5 will return 120  because 1 * 2 * 3 * 4 * 5 = 120
For 0 and 1 will return ,1
For a negative number, ValueError must be raised. Hint: ValueError raise
'''
def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(number)

# דוגמאות להפעלת הפונקציות
print(power(2, 4))  # output: 16
print(sqrt(9))      # output: 3.0
print(factorial(5)) # output: 120
