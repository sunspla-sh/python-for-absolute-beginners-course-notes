penne = 16.68

sauce = 6.98

garlic = 16.78

seasoning = 15.26

baguettes = 3.00

meatballs = 4.39

subtotal_integer = (
  (penne * 100)
  + (sauce * 100)
  + (garlic * 100)
  + (seasoning * 100)
  + (baguettes * 100)
  + (meatballs * 100)
)

print(subtotal_integer / 100)

subtotal_round = (
  penne
  + sauce
  + garlic
  + seasoning
  + baguettes
  + meatballs
)

print(round(subtotal_round, 2))

