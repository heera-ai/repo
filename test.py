import pandas
import numpy as np 


print("This work is done without any fancy IDE, it uses only a simple text editor ")

name = input('Enter your name : ')
print(f"hi {name}, welcome to the python calculator")

i = int(input(" choose a number for function : 1. addition\
	2. subtraction\
	3. multiplication\
	4. division\n" ))

p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

if (i == 1):
	result = p + q
	print(f'Result is : {result}')

elif (i == 2):
	result = p - q
	print(f'Result is : {result}')

elif (i == 3):
	result = p * q
	print(f'Result is : {result}')

elif (i == 4):
	result = p / q
	print(f'Result is : {result}')



