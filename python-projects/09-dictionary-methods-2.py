# Exercise 1
consonant_dict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", 'consonant')

for k,v in consonant_dict.items():
  print(k,v)

# Exercise 2
fast_food_items = {
  "McDonald's": "Big Mac",
  "Burger King": "Whopper",
  "Chick-fil-A": "Original Chicken Sandwich"
}
print(fast_food_items.pop("McDonald's"))

# Exercise 3
fast_food_items.popitem()
print(fast_food_items)