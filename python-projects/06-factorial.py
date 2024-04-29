from sys import exit

factor = int(input("Enter a positive integer:\n"))

if factor < 1:
  exit((
    "Error: You entered "
    + str(factor)
    + ", which is not a positive integer."
  ))

def calc_factorial(f):
  total = 1
  for i in range(1, f + 1):
    total *= i
  return total


print((
  "The factorial of "
  + str(factor)
  + " is "
  + str(calc_factorial(factor))
))