from sys import exit

pos_int = int(input("Enter a positive integer:\n"))

if pos_int < 1:
  exit((
    "Error: You entered "
    + str(pos_int)
    + ", which is not a positive integer."
  ))

counter = pos_int
sum_int = 0

while counter > 0:
  sum_int += counter
  counter -= 1

print("The integer you entered was " + str(pos_int))
print((
  "The sum of all integers from 1 to "
  + str(pos_int)
  + " is "
  + str(sum_int)
))