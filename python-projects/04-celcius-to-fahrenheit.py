cel = int(input("Enter an integer temperature in celcius.\n"))

def fahrenheit_round(c):
  return round(1.8 * c + 32, 1)


def fahrenheit_10(c):
  return ((18 * c) / 10) + 32

print((
  "The Fahrenheit equivalent of "
  + str(cel)  
  + " degress Celcius is "
  + str(fahrenheit_round(cel))
  + "."
))

print((
  "The Fahrenheit equivalent of "
  + str(cel)  
  + " degress Celcius is "
  + str(fahrenheit_10(cel))
  + "."
))