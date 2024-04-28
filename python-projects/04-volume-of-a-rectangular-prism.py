length = int(input("Enter a length.\n"))
width = int(input("Enter a width.\n"))
height = int(input("Enter a height.\n"))

def calc_rect_prism_volume(l, w, h):
  return l * w * h

print((
  "The volume of the rectangular prism is "
  + str(calc_rect_prism_volume(length, width, height))
  + " cubic feet."
))