user_string = input("Enter a string:\n")

reversed_user_string = ""

for i in range(len(user_string) - 1, -1, -1):
  reversed_user_string += user_string[i]


print(reversed_user_string)



# Alternatively, use the reversed() method to
# reverse the user_string iterator before iterating over it
reversed_iterator_user_string = ""

for c in reversed(user_string):
  reversed_iterator_user_string += c


print(reversed_iterator_user_string)