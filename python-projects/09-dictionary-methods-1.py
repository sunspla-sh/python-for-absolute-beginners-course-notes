# Exercise 1 and Exercise 2
famous_songs = {
  'Queen': 'Bohemian Rhapsody',
  'Bee Gees': 'Stayin\' Alive',
  'U2': 'One',
  'Michael Jackson': 'Billie Jean',
  'The Beatles': 'Hey Jude',
  'Bob Dylan': 'Like A Rolling Stone'
}

# Exercise 3
print(len(famous_songs))

# Exercise 4
for k in famous_songs.keys():
  print(k)

# Exercise 5
for v in famous_songs.values():
  print(v)

# Exercise 6
for k,v in famous_songs.items():
  print(k,v)

# Exercise 7
print(famous_songs.get('Promise of the Real', 'Key not found!!!'))