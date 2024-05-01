# Tuples

## Introduction To Tuples

- **Tuples** are an iterable data type consisting of a collection of items enclosed in parenthesis (```()```), where each item has an index value (starting from ```0``` to ```length - 1```) with which it can be accessed

    - Similar to lists, the items in a tuple can be any data type and tuples can be sliced with square bracket (```[]```) and colon (```:```) syntax

    - Unlike lists, tuples are immutable

        - Due to this immutability, tuples can be used as keys in dictionaries

        - Also, tuples use less memory than lists

    - Tuples can also be created with the ```tuple``` function, which accepts any iterable as an argument

    - Example

        ```python
        t_1 = ('a','b','c')
        t_2 = (2.7, False, [1,2,3])
        t_3 = (1,1,0,0,0)

        print(t_1) # prints ('a', 'b', 'c')
        print(t_2) # prints (2.7, False, [1, 2, 3])
        print(t_3) # prints (1, 1, 0, 0, 0)

        t_4 = tuple([3.14, 6, 0])
        t_5 = tuple('hello')
        t_6 = tuple({'x': 1,'y': 2,'z': 3})

        print(t_4) # prints (3.14, 6, 0)
        print(t_5) # prints ('h', 'e', 'l', 'l', 'o')
        print(t_6) # prints ('x', 'y', 'z')

        print(t_1[1]) # prints b
        print(t_3[:2]) # prints (1,1)
        print(t_3[1:3]) # prints (1,0)
        print(t_3[2:]) # prints (0,0,0)
        ```

## Tuple Looping and Step

- Tuples can be looped through with the ```for``` statement because they are iterables

    - Example

        ```python
        t_1 = ('a', 'b', 'c')

        for v in t_1:
          print(v)

        # the above for loop prints the following:
        # a
        # b
        # c

        i = 0

        while i < len(t_1):
          print(t_1[i])
          i += 1

        # the above while loop prints the following:
        # a
        # b
        # c
        ```

- **Tuple Stepping** adjusts the number of items in a tuple slice using square brackets (```[]```) and a double colon syntax (```::```) with ```start:stop:step``` values

    - This stepping syntax also works identically in strings and lists

    - Example

        ```python
        ints = (1,2,3,4,5,6,7,8,9,10)

        print(ints[::3]) # prints (1,4,7,10)
        print(ints[1::2]) # prints (2,4,6,8)
        print(ints[7::-1]) # prints (8,7,6,5,4,3,2,1)
        print(ints[8::-2]) # prints (9,7,5,3,1)
        print(ints[:5:2]) # prints (1,3,5)
        print(ints[1:4:2]) # prints (2,4)
        ```

## Tuple Methods

- Tuples can be arbitrarily nested

    - Example

        ```python
        sample = (('a', 'b'), ('c', 'd'))
        
        print(sample[1]) # prints ('c', 'd')
        print(sample[0][1]) # prints b
        ```

- The ```.count()``` method is a tuple method that returns the number of times a given argument appears in a tuple

    - Example

        ```python
        t_1 = (1,1,1,5,5,0,0,0,0,0,0)
        
        print(t_1.count(1)) # prints 3
        print(t_1.count(5)) # prints 2
        print(t_1.count(0)) # prints 6
        print(t_1.count(9)) # prints 0
        ```

- The ```.index()``` method is a tuple method that returns the number of the first index matching a given argument or an error if a match is not found

    - Example

        ```python
        t_1 = (1,1,1,5,5,0,0,0,0,0,0)
        
        print(t_1.index(1)) # prints 0
        print(t_1.index(5)) # prints 3
        print(t_1.index(0)) # prints 5
        print(t_1.index(9)) # ValueError: tuple.index(x): x not in tuple
        ```