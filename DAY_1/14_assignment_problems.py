# Q1. Write a program that asks the user for their name and age, then prints a
# sentence like:

name = input("enter your name: ")
age = input("enter your age: ")
print("hello" " " + name + " " "you are",age +" " "years old!")
print(f"hello {name},you are {age} years old!")


# # Q2. Take two numbers as input from the user and print their sum, difference,
# # product, and quotient.

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print("sum",num1+num2)
print("difference",num1-num2)
print("product",num1*num2)
print("quotient",num1/num2)

# Q3. Ask the user to enter two integers and one float. Convert them all to floats
# and print their average.

num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
num3 = float(input("enter number 3: "))
average = (num1+num2+num3)/3
print("The average of three number is",average)





# Q4. The user enters a string containing a number (e.g., ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

user_input  = input("enter a number: ")

as_int = int(user_input)
as_float = float(user_input)
as_str = str(as_int)
print(f"value: {as_int},type:{type(as_int)}")
print(f"value:{as_float},type:{type(as_float)}")
print(f"value:{as_str},typ:{type(as_str)}")





# Q5. Evaluate and print the result of the following expression:
# x=10+3*2**2
x=10+3*2**2
print(x)

# # Q6. Write a program to swap values of two numbers entered by the user.
a = 10
b = 20
c = a
a = b
b = c 
print(a,b)


# Q7. Ask the user for a temperature in Celsius (string input). Convert it to ,
# then calculate and print temperature in Fahrenheit.
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +
# 32

celsius_input = input("enter temperature in celsius:")
celsius_temp = float(celsius_input)
fahrenheit_temp = (celsius_temp * (9/5)) +32
print(f"{celsius_temp}c is equal to {fahrenheit_temp}f")

# # Q8. Take the radius (r) as user input and print the area.
# # Use the formula: Area = π * r
# # 2 (value of π = 3.14)


radius = int(input("enter the radius: "))
pi =3.14

area = pi*(radius*radius)
print(f"the area of the circle with radius {radius} is : {area}")

# # Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
# # compute simple interest:
# # SI = (P ∗ R ∗ T)/100

p = float(input("enter the priniciple amount(p): "))
r = float(input("enter the rate of interest(r): "))
t = float(input("enter a time in years(t): "))
si = (p*r*t)/100
print("simple interest is ",si)


# # # Q10. Take a decimal number as input (like ) and output its:
# • integer part -
# • fractional part -
# 45
# .78

number = 45.78

integer_part = int(number)
fractional_part = number - integer_part

print(f"Integer part: {integer_part}")
print(f"Fractional part: {round(fractional_part, 2)}")

