# Lists

## Introduction To Lists

- A **list** is a data type that contains zero or more values in an ordered sequence

    - Values within a list are also known as **items** and can be of any data type (even other lists)

    - Example

        ```python
        ex_list_1 = [5,4,3,2,1]
        ex_list_2 = [2.7,9.31]
        ex_list_3 = ['blue','green','yellow']
        ex_list_4 = [True, False, False, False, False, False]
        ex_list_5 = [[1,2,3], [5,4], [0]]
        ex_list_6 = [5, 'blue', True, [1,2,3]]
        ```

- The ```list()``` function converts an iterable data type into a list and returns it

    - Example

        ```python
        ex_string = 'hello'
        ex_list = list(ex_string)
        print(ex_list) # prints ['h','e','l','l','o']
        ```

- The ```in``` operator returns ```True``` if a given item is in a list, otherwise it returns ```False```

    - Example

        ```python
        checked_list = [1,2,3,4]
        print(1 in checked_list) # prints True
        print(5 in checked_list) # prints False
        ```

- The ```not in``` operator returns ```True``` if a given item is NOT in a list, otherwise it returns ```False```

    - Example

        ```python
        checked_list = [1,2,3,4]
        print(1 not in checked_list) # prints False
        print(5 not in checked_list) # prints True
        ```

## Introduction To Lists Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.

    2. Create another variable and assign it a call of the list() function with a string as its argument.

    3. Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2 and print the result.

    4. Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from step 2 and print the result.

## Introduction To Lists Exercises Solutions

- See solutions in [08-introduction-to-lists.py](./python-projects/08-introduction-to-lists.py)

## Indexes and List Slicing

- Similar to strings, each item in a list has an **index** number starting from zero (```0```) up to the length of the list minus one (```len(example_list) - 1```), and we can access an item in a list by its index

    - Additionally, we can access items in a list in reverse order by using a **negative index** number, where the last item in the list is represented by negative one (```-1```) and the first item in the list is represented by the negative length of the list (```-len(example_list)```)

    - Example

        ```python
        test_list = ['hi', 'my', 'name', 'is', 'bob']
        print(test_list[0]) # prints hi
        print(test_list[4]) # prints bob
        print(test_list[-1]) # prints bob
        print(test_list[-len(test_list)]) # prints hi
        print(test_list[len(test_list) - 1]) # prints bob
        print(test_list[len(test_list)]) # IndexError: list index out of range
        ```

- **List Slicing** is the act of creating smaller lists from a given list

    - The syntax for list slicing is similar to the syntax for string slicing, in that we use square brackets (```[]```) with a colon (```:```) and the indexes that we wish to slice from the given string

    - The indexes used for slicing can be positive or negative

    - Example

        ```python
        ex_list = ['hi', 'my', 'name', 'is', 'bob']
        print(ex_list[:2]) # prints ['hi', 'my']
        print(ex_list[2:3]) # prints ['name']
        print(ex_list[1:]) # prints ['my', 'name', 'is', 'bob']
        print(ex_list[:-3]) # prints ['hi', 'my']
        print(ex_list[-3:]) # prints ['name', 'is', 'bob']
        print(ex_list[-3:-1]) # prints ['name', 'is']
        ```

- List slices or individual list items can be **reassigned** new values with the assignment operator (```=```)

    - Example

        ```python
        ex_list = [5.5,4.4,3.3]
        print(ex_list[2]) # prints 3.3
        print(ex_list) # prints [5.5,4.4,3.3]
        ex_list[2] = 'hello'
        print(ex_list[2]) # prints hello
        print(ex_list) # prints [5.5,4.4,'hello']
        ex_list[1:] = ['my', 'fav']
        print(ex_list) # prints [5.5,'my','fav']
        ex_list[1:] = ['test']
        print(ex_list) # prints [5.5,'test']
        
        new_list = [1,2,3,4,5,6,7,8]
        new_list[1:7] = []
        print(new_list) # prints [1,8]
        
        sample_list = [1,2,3,4,5,6,7,8]
        sample_list[1:7] = 'hi'
        print(sample_list) # prints [1, 'h', 'i', 8]
        ```

## Indexes and List Slicing Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]

    2. Access the first list from the list of lists in step 1 by index then print it.

    3. Access the 14 from the list in step 1 then print it.

    4. Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]

    5. Use a negative integer to access "chair" from the variable in step 4 by index then print it.

    6. Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

    7. Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]

    8. Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.

    9. Print the slice [8.76, 6.54] from the variable you created in step 7.

    10. Print the slice [0.98, 8.76] from the variable you created in step 7.

## Indexes and List Slicing Exercises Solutions

- See solutions in [08-indexes-and-list-slicing.py](./python-projects/08-indexes-and-list-slicing.py)

## del and List Methods

- The ```del``` operator removes items from lists

    - Example

        ```python
        planets = ['pluto', 'mars', 'earth', 'venus']
        print(planets) # prints ['pluto', 'mars', 'earth', 'venus']
        del planets[0]
        print(planets) # prints ['mars', 'earth', 'venus']
        ```

- The ```.remove()``` method is a list method that takes an argument and removes the first item matching the argument from the list, or it throws an error if the item cannot be found

    - Example

        ```python
        planets = ['pluto', 'mars', 'earth', 'earth', 'venus']
        print(planets) # prints ['pluto', 'mars', 'earth', 'venus']
        planets.remove('earth')
        print(planets) # prints ['pluto', 'mars', 'earth', 'venus']
        ```

- The ```.append()``` method is a list method that takes an argument and appends that argument as an item onto the end of the list

    - Example

        ```python
        planets = ['pluto', 'mars', 'earth']
        print(planets) # prints ['pluto', 'mars', 'earth']
        planets.append('neptune')
        print(planets) # prints ['pluto', 'mars', 'earth', 'neptune']
        ```

- The ```.insert()``` method is a list method that takes two arguments and adds an item to a list, where the first argument is the index where the item should be added and the second argument is the item to be added to the list 

    - Example

        ```python
        planets = ['pluto', 'mars', 'earth']
        print(planets) # prints ['pluto', 'mars', 'earth']
        planets.insert(1, 'mercury')
        print(planets) # prints ['pluto', 'mercury', 'mars', 'earth']
        ```

- The ```.sort()``` method is a list method that can sort lists made entirely of numbers or lists made entirely of strings

    - By default, numbers are sorted least to greatest and strings are sorted in alphabetical (ascii) order, but this can be reversed by using the ```reverse=True``` keyword parameter parameter

    - Example

        ```python
        num_list = [9, -8, 50, 2.555]
        print(num_list) # prints [9, -8, 50, 2.555]
        num_list.sort()
        print(num_list) # prints [-8, 2.555, 9, 50]
        num_list.sort(reverse=True)
        print(num_list) # prints [-8, 2.555, 9, 50]

        str_list = ['Ringo', 'John', 'George', 'Paul']
        print(str_list) # prints ['Ringo', 'John', 'George', 'Paul']
        str_list.sort()
        print(str_list) # prints ['George', 'John', 'Paul', 'Ringo']
        str_list.sort(reverse=True)
        print(str_list) # prints ['George', 'John', 'Paul', 'Ringo']
        ```

- The ```.index()``` method is a list method that attempts to find the first index number matching a given argument

    - Example

        ```python
        metals = ['copper', 'gold', 'silver', 'silver', 'iron']
        print(metals.index('silver')) # prints 2
        print(metals.index('tin')) # ValueError: 'tin' is not in list
        ```

- The ```.pop()``` method is a list method that removes the last item from a list and returns it

    - An optional index argument can be used to remove from alternative position in the list instead of the end of the list

    - Example

        ```python
        fruit = ['apple', 'orange', 'pear', 'banana']
        print(fruit) # prints ['apple', 'orange', 'pear', 'banana']
        last_item = fruit.pop()
        print(fruit) # prints ['apple', 'orange', 'pear']
        print(last_item) # prints banana
        index_one_item = fruit.pop(1)
        print(fruit) # prints ['apple', 'pear']
        print(index_one_item) # prints orange
        ```

## del and List Methods Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

    2. Use del to remove "tiger" from the list assigned to arctic_animals.

    3. Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.

    4. Use the .append() method to add the string "arctic fox" to the list arctic_animals.

    5. Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.

    6. Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.

    7. Use print() to display the list assigned to arctic_animals

    8. Use .index() to get the index number of "reindeer" from arctic_animals then print it.

    9. Use .pop() to get the last item from the list arctic_animals then print it.

## del and List Methods Exercises Solutions

- See solutions in [08-del-and-list-methods.py](./python-projects/08-del-and-list-methods.py)

## Lists vs Strings

- Both lists and strings are iterable

- Lists are mutable

- Strings are immutable

- Immutable data types are copied by value

    - ```int```

    - ```float```

    - ```complex```

    - ```str```

    - ```tuple```

    - ```bytes```

    - ```bool```

    - ```frozenset```

- Mutable data types are copied by reference

    - ```list```

    - ```dict```

    - ```set```

    - ```bytearray```

- The ```deepcopy()``` function makes a copy of a list, allowing you to assign that identical copy to a new variable instead of simply referencing the old list

    - Example

        ```python
        from copy import deepcopy
        ex_1 = [5,4,3,2]
        ex_2 = ex_1
        ex_1.pop()
        print(ex_1) # prints [5,4,3]
        print(ex_2) # prints [5,4,3]
        ex_2 = deepcopy(ex_1)
        ex_1.pop()
        print(ex_1) # prints [5,4]
        print(ex_2) # prints [5,4,3]
        ```

- The line continuation character ```\``` (backslash) is used to continue an expression on a new line

    - Example

        ```python
        t_1 = 1 + 2 \
            + 3 + 4
        print(t_1) # prints 10
        s_1 = "hi my \
        name is bob"
        print(s_1) # prints hi my name is bob
        ```