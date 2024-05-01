# Dictionaries

## Introduction To Dictionaries

- A **Dictionary** is a data type that stores a collection of key-value pairs

    - The keys of a dictionary must be ```hashable```, usually any immutable data type will work as a key

        - Similarly to how an ```iterable``` can be iterated over due to its built-in functionality, a ```hashable``` can be hashed due to its built-in functionality

    - The values of a dictionary can by any data type

    - The syntax for creating a dictionary is a pair of curly brackets (```{}```) with key-value pairs inside them

    - Accesing a value in a dictionary is done with the dictionary name, followed by square brackets (```[]```) with the key of the value you'd like to access inside them

    - Example

        ```python
        consoles = {
          'nintendo': 'wii'
          'microsoft': 'xbox'
          'sony': 'playstation'
        }

        print(consoles['microsoft']) # prints xbox
        ```

- Dictionaries are unordered (although they remember insertion order of key-value pairs in Python 3.7+)

    - When comparing dictionaries, the equal to operator (```==```) does not consider order, only that all key-value pairs are in both dictionaries

    - Example

        ```python
        ex_1 = {
          'name': 'bob',
          'creature': 'ape'
        }

        ex_2 = {
          'creature': 'ape',
          'name': 'bob'
        }

        print(ex_1 == ex_2) # prints True
        ```

- Dictionaries are mutable

- If you attempt to access a key that does not exist in a given dictionary, you will get an error

    - Example

        ```python
        ex_1 = {
          'name': 'bob',
          'creature': 'ape'
        }
        print(ex_1['age']) # KeyError: 'age'
        ```

- The ```in``` operator returns ```True``` if a given key is in a dicitonary, otherwise it returns ```False```

    - Example

        ```python
        ex_1 = {
          'name': 'bob',
          'creature': 'ape'
        }
        print('name' in ex_1) # prints True
        print('age' in ex_1) # prints False
        ```

- The ```not in``` operator returns ```True``` if a given key is NOT in a dicitonary, otherwise it returns ```False```

    - Example

        ```python
        ex_1 = {
          'name': 'bob',
          'creature': 'ape'
        }
        print('name' not in ex_1) # prints False
        print('age' not in ex_1) # prints True
        ```

## Introduction To Dictionaries Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable and assign it a dictionary that has 5 key value pairs

    2. Print and access the value held at the third key in the dictionary

    3. Use the in keyword to check if a key appears in the dictionary and print the result

    4. Use not in to check if a key does not appear in the dictionary and print the result

## Introduction To Dictionaries Exercises Solutions

- See solutions in [09-introduction-to-dictionaries.py](./python-projects/09-introduction-to-dictionaries.py)

## Dictionary Methods 1

- The ```.keys()``` method is a dictionary method that returns all of the keys from a given dictionary as a set-like, iterable ```dict_keys``` object

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }

        print(fruit.keys()) # prints dict_keys(['apple','orange','pear'])

        for k in fruit.keys():
          print(k)

        # The above for loop prints the following:
        # apple
        # orange
        # pear
        ```

- The ```.values()``` method is a dictionary method that returns all of the values from a given dictionary as an iterable ```dict_values``` object

    - Note that unlike ```dict_keys```, the ```dict_values``` object is not set-like, because there can be identical values in a dictionary while keys must be unique

    - To check if a given value is in a dictionary, the ```in``` and ```not in``` operators can be used with the ```.values()``` method

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }

        print(fruit.values()) # prints dict_values([5, 0, 2])

        for v in fruit.values():
          print(v)

        # The above for loop prints the following:
        # 5
        # 0
        # 2

        print(5 in fruit.values()) # prints True
        print(0 not in fruit.values()) # prints False
        ```

- The ```.items()``` method is a dictionary method that returns all of the key-value pairs from a given dictionary as a set-like, iterable ```dict_items``` object

    - Each key-value pair in the ```dict_items``` object is represented by a tuple

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }

        print(fruit.items()) # prints dict_items([('apple', 5),('orange', 0), ('pear', 2)])

        for k, v in fruit.items():
          print(k, v)

        # The above for loop prints the following:
        # apple 5
        # orange 0
        # pear 2
        ```

- The ```.get()``` method is a dictionary method that attempts to find and return a value within a dictionary based on an argument

    - Unlike the square bracket (```[]```) syntax for accessing items in a dictionary, the ```.get()``` method does not return a KeyError if it fails

    - By default, the ```.get()``` method returns ```None``` if the key is not found, but this can be customized with a second parameter to return a different default value

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        print(fruit.get('banana')) # prints None
        print(fruit.get('banana', 'Sorry that fruit is missing')) # prints Sorry that fruit is missing
        ```

- The ```len()``` function returns the number of key-value pairs in a dictionary

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        print(len(fruit)) # prints 3
        ```

## Dictionary Methods 1 Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable and assign it the following dictionary:
        
        ```
        {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
        ```

    2. Make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

    3. Print the length of the dictionary.

    4. Use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.

    5. Print all of the values from the dictionary using the .values() method.

    6. Use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.

    7. Use the .get() method to check the dictionary for the key ```"Promise of the Real"``` and create a message that will print if the key is not found in the dictionary.

## Dictionary Methods 1 Exercises Solutions

- See solutions in [09-dictionary-methods-1.py](./python-projects/09-dictionary-methods-1.py)

## Dictionary Methods 2

- The ```.fromkeys()``` method creates a new dictionary with keys and values using a first, iterable argument as one or more keys and a second, value argument as the value of those keys

    - Note that when used on an existing dictionary, the previous key-value pairs are not copied into the new dictionary

    - Example

        ```python
        test = {}.fromkeys("asdf", "test")
        print(test) # prints {'a': 'test, 's': 'test', 'd': 'test', 'f': 'test'}

        sample = {}.fromkeys([1,2], "test")
        print(sample) # prints {1: 'test, 2: 'test'}

        ex = {'hi': 'bob'}.fromkeys([1,2], 'test')
        print(ex) # prints {1: 'test, 2: 'test'}
        ```

- The ```.pop()``` method is a dictionary method that removes and returns a single value from a given dictionary by its key

    - Note that if the key does not exist, a KeyError will be thrown

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        print(fruit) # prints {'apple':5, 'orange':0, 'pear':2}
        print(fruit.pop('pear')) # prints 2
        print(fruit) # prints {'apple':5, 'orange':0}
        ```

- The ```.popitem()``` method is a dictionary method that removes the last item that was added to the dictionary and returns it as a tuple

    - In Python 3.7+, dictionaries remember key-value pair insertion order, so ```.popitem()``` removes the last inserted key-value pair

    - In Python 3.6 or less, dictionaries do not remember key-value pair insertion order, so ```.popitem()``` removes a random key-value pair

        - Note that some Python 3.6 or less versions do technically remember insertion order, however this is an implementation detail (e.g. an artifact of how dictionaries were implemented) and not an actual language standard until 3.7+

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        print(fruit) # prints {'apple':5, 'orange':0, 'pear':2}
        print(fruit.popitem()) # prints ('pear', 2)
        print(fruit) # prints {'apple':5, 'orange':0}
        print(fruit.popitem()) # prints ('orange', 0)
        print(fruit) # prints {'apple':5}
        ```

## Dictionary Methods 2 Exercises

- Do all of this in a .py file in Pycharm.

    1. Use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the string "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.  "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of those key: value pairs on a different line.  For example, the first 3 lines in the output should be the following:

        ```
        b consonant

        c consonant

        d consonant
        ```

    2. Paste this dictionary into your .py file then pop and print "Big Mac" from it

        ```
        fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
        ```

    3. Use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new fast_food_items dictionary.

## Dictionary Methods 2 Exercises Solutions

- See solutions in [09-dictionary-methods-2.py](./python-projects/09-dictionary-methods-2.py)

## Dictionary Methods 3

- The ```.clear()``` method is a dictionary method that removes all key-value pairs from an existing dictionary

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        print(fruit) # prints {'apple':5, 'orange':0, 'pear':2}
        fruit.clear()
        print(fruit) # prints {}
        ```

- The ```.copy()``` method is a dictionary method that creates and returns an exact copy of a dictionary with its own reference

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }
        copy_fruit = fruit
        
        print(fruit) # prints {'apple':5, 'orange':0, 'pear':2}
        print(copy_fruit) # prints {'apple':5, 'orange':0, 'pear':2}
        
        fruit['pear'] = 7
        
        print(fruit) # prints {'apple':5, 'orange':0, 'pear':7}
        print(copy_fruit) # prints {'apple':5, 'orange':0, 'pear':7}

        copy_fruit = fruit.copy()

        fruit['pear'] = 9

        print(fruit) # prints {'apple':5, 'orange':0, 'pear':9}
        print(copy_fruit) # prints {'apple':5, 'orange':0, 'pear':7}
        ```

- The ```.update()``` method is a dictionary method that adds existing key-value pairs from one dictionary to another or overwrites key-value pairs from one dictionary with matching keys from another

    - Example

        ```python
        fruit = {
          'apple': 5,
          'orange': 0,
          'pear': 2
        }

        recent_purchase = {
          'peach': 1
        }

        fruit.update(recent_purchase)

        print(recent_purchase) # prints {'peach': 1}
        print(fruit) # prints {'apple': 5, 'orange': 0, 'pear': 2, 'peach': 1}

        more_apples = {
          'apple': 9
        }

        fruit.update(more_apples)

        print(more_apples) # prints {'apple': 9}
        print(fruit) # prints {'apple': 9, 'orange': 0, 'pear': 2, 'peach': 1}
        ```

## Dictionary Methods 3 Exercises

- Do all of this in a .py file in Pycharm.

    1. Paste these 2 dictionaries into your file

        ```
        internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
        another_one = {"shroud": "Twitch"}
        ```

    2. Use .update() to add the contents of another_one to internet_celebrities.

    3. Create a variable and assign it a copy of internet_celebrities.

    4. Use the .clear() method to get rid of the contents of internet celebrities.

    5. Print internet_celebrities.

    6. Print the variable you created in step 3.

## Dictionary Methods 3 Exercises Solutions

- See solutions in [09-dictionary-methods-3.py](./python-projects/09-dictionary-methods-3.py)

## Dictionary Methods 4

- The ```.setdefault()``` method is a dictionary method that adds keys with default values to a dictionary if they do not already exist

    - Note that if the key already exists, it will NOT be changed

    - Example

        ```python
        computers = {
          "Google": "ChromeBook",
          "Apple": "MacBook",
          "Microsoft": "Surface Pro"
        }

        print(computers.setdefault("Apple", "Macintosh")) # returns MacBook because key Apple already exists

        print(computers) # prints {'Google': 'ChromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro'}

        print(computers.setdefault("Lenovo", "ThinkPad")) # returns ThinkPad because key Lenovo did NOT previously exist
        
        print(computers) # prints {'Google': 'ChromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}
        ```

## dict()

- The ```dict()``` function can create a new dictionary from keyword arguments or from a positional argument of an iterable containing other iterables of exactly two objects each

    - Example

        ```python
        empty = dict()

        print(empty) # prints {}

        with_values_keyword_args = dict(a=1,b=2,c=3)
        
        print(with_values_keyword_args) # prints {'a': 1, 'b': 2, 'c': 3}

        with_values_iterable = dict([('x', 1), ('y', 2), ('z', 3)])

        print(with_values_iterable) # prints {'x': 1, 'y': 2, 'z': 3}
        ```
