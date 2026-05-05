# Q1. Write a program that takes as input. Using conditional statements,
# calculate the finaltax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%




salary = float(input("Enter your salary:"))
if (salary<30000):
    tax_rate = 5

elif (salary>=30000 and salary<=70000):
   tax_rate = 15

else:
  tax_rate = 25

print(f"For a salary of {salary}, the tax rate is {tax_rate}%.")


# Q2. Write a function that takes two integers a and b prints all even
# numbers between them (inclusive).


def print_even_numbers(a,b):
   start = min(a,b)
   end = max(a,b)

   for num in range(start, end+1):
      if num%2 == 0:
         print(num)
print_even_numbers(4,15)




# Q3. Write a function that prints the digits of a number, .
# For eg: 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]


def print_digits(n):
   n_str = str(n)
   for digit in n_str:
      print(digit)

print_digits(312)

# Q4. Write a function to return the count the number of digits in a number, n

def count_digits(n):
   return len(str(abs(n)))
print(count_digits(12345))
print(count_digits(-789))


# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
# and 5. 

for i in range(1,101):
   if i%3 ==0 and i%5==0:
      print(i)

#Q7. Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit”.

while True:
   user_input = input("enter the number ya band karne ke liye quit likhe")
   #check karna ke user ne exit karne ke liye Quit to nahi likha
   if user_input.strip().lower() == "quit":
      print("program band ho raha ha bye")
      break

   try:
      #input ko decimal float me conver karna 
      number = float(user_input)
      if number>0:
         print(f"{number} ek positive number hai")
      elif number<0:
         print(f"{number} ek negative number hai" )
      else:
         print("yeh zero ha")

   except ValueError:
        print("ghalati mehrabi karke ek valid number likhe")
