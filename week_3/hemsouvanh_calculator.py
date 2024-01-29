''' Author: Brock Hemsouvanh
    Date: 2024-01-28
    hemsouvanh_calculator.py Description: Uses function methods to do basic arithmetic.
'''
#arithmetic functions below
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def divide(num1, num2):
  return num1 / num2

def multiply(num1, num2):
  return num1 * num2

#some random variables for testing
num1 = 4
num2 = 2

#print concatenated function returns. Note the type conversion, "str" before the result function return.
print("The result for addition is " + str(add(num1, num2)) + ".")

print("The result for subtraction is " + str(subtract(num1, num2)) + ".")

print("The result for division is " + str(divide(num1, num2)) + ".")

print("The result for multiplication is " + str(multiply(num1, num2)) + ".")