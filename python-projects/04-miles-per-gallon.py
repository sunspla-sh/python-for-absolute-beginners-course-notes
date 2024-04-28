from random import randint

rand_gal = randint(10, 25)
rand_mile = randint(200, 400)

mpg = rand_mile // rand_gal

print((
  "Miles per gallon: "
  + str(mpg)
  + "\nMiles: "
  + str(rand_mile)
  + "\nGallons: "
  + str(rand_gal)
))