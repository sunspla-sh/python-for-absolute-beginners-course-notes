user_string = input("Enter any string:\n")

letter_sum = 0

for l in user_string:
  letter_sum += 1

print('The string you entered was the following: ' + user_string)
print('The length of your string is ' + str(letter_sum))