# Sets

## Introduction To Sets

- **Sets** are collections of unordered, unique (non-duplicative) items of any data type that are created with curly bracket syntax (```{}```) or the ```set()``` function (which accepts an iterable as an argument)

    - Unlike dictionaries, sets do not contain key-value pairs

    - Unlike lists, sets cannot have duplicate values or be accessed by index number

    - The ```in``` and ```not in``` operators work with sets in the same way that they do with lists

    - The ```is``` operator returns true if two variables reference the same set in memory

    - The ```len()``` function can be used to return the number of items in a set

    - Sets are frequently used to de-duplicate lists

    - Example

        ```python
        set_1 = { 1, 5, 9 }
        set_2 = { 'a', 'b', 'c' }
        set_3 = { 4, 'a', False }
        set_4 = { 2, 2, 2 }
        set_5 = set([1,2,3])
        set_6 = set([9,9,9])

        print(set_1) # prints {1, 5, 9}
        print(set_2) # prints {'c', 'a', 'b'}
        print(set_3) # prints {'a', False, 4}
        print(set_4) # prints {2}
        print(set_5) # prints {1, 2, 3}
        print(set_6) # prints {9}

        # Note that order was not guaranteed when the sets were printed and that it differed from the order in which the items were placed when the sets were created

        for s in set_3:
          print(s)

        # The above for loop prints the following (also note that order was not guaranteed):

        # False
        # 4
        # a

        print(5 in set_1) # prints True
        print(9 not in set_1) # prints False

        print(len(set_1)) # prints 3
        ```

## Set Methods

- The ```.add()``` method is a set method that adds a new item to a set, assuming that the item is unique

    - Example

        ```python
        scifi = {'star trek', 'star wars', 'halo'}
        scifi.add('mass effect')

        print(scifi) # prints {'star trek', 'star wars', 'halo', 'mass effect'}

        scifi.add('halo') # No effect because halo already in set

        print(scifi) # prints {'star trek', 'star wars', 'halo', 'mass effect'}
        ```

- The ```.remove()``` method is a set method that deletes an item from a set or throws a KeyError if the item is not in the set

    - Example

        ```python
        scifi = {'star trek', 'star wars', 'halo'}
        scifi.remove('star wars')

        print(scifi) # prints {'star trek', 'halo'}

        scifi.remove('mass effect') # KeyError: 'mass effect'
        ```

- The ```.discard()``` method is a set method that deletes an item from a set or does nothing if the item is not in the set

    - Example

        ```python
        scifi = {'star trek', 'star wars', 'halo'}
        scifi.discard('star wars')

        print(scifi) # prints {'star trek', 'halo'}

        scifi.discard('mass effect') # No effect because 'mass effect' is not in set

        print(scifi) # prints {'star trek', 'halo'}
        ```

- The ```.clear()``` method is a set method that removes all items from a set

    - Example

        ```python
        scifi = {'star trek', 'star wars', 'halo'}
        scifi.clear()

        print(scifi) # prints set()
        ```

- The ```.copy()``` method is a set method that creates a new copy of a set with its own reference in memory

    - Example

        ```python
        mountains = {'everest', 'kilimanjaro', 'fuji'}

        mtn = mountains

        mountains.discard('fuji')

        print(mtn) # prints {'everest', 'kilimanjaro'}
        print(mountains) # prints {'everest', 'kilimanjaro'}

        mtn_copy = mountains.copy()

        print(mtn_copy is mountains) # prints False

        mountains.discard('everest')

        print(mtn) # prints {'kilimanjaro'}
        print(mountains) # prints {'kilimanjaro'}
        print(mtn_copy) # prints {'everest', 'kilimanjaro'}

        print(mtn is mountains) # prints True
        print(mtn is mtn_copy) # prints False
        ```

- The ```.union()``` method is a set method that combines all items from two sets into a single new set

    - Alternatively, the union operator, represented by the pipe (```|```) character can be use instead of the ```.union()``` method

    - Example

        ```python
        set_1 = {1,2,3}
        set_2 = {2,3,4,5}

        union_set = set_1.union(set_2)

        union_pipe_set = set_1 | set_2

        print(set_1) # prints {1,2,3}
        print(set_2) # prints {2,3,4,5}
        print(union_set) # prints {1,2,3,4,5}
        print(union_pipe_set) # prints {1,2,3,4,5}
        ```

- The ```.intersection()``` method is a set method that combines two sets into a single new set with only the items they have in common

    - Alternatively, the intersection operator, represented by the ampersand (```&```) character can be use instead of the ```.intersection()``` method

    - Example

        ```python
        set_1 = {1,2,3}
        set_2 = {2,3,4,5}

        intersection_set = set_1.intersection(set_2)

        intersection_ampersand_set = set_1 & set_2

        print(set_1) # prints {1,2,3}
        print(set_2) # prints {2,3,4,5}
        print(intersection_set) # prints {2,3}
        print(intersection_ampersand_set) # prints {2,3}
        ```

- The ```.difference()``` method is a set method that removes items from a first set if they are in a second set that is being subtracted from them

    - Alternatively, the difference operator, represented by the minus (```-```) character can be use instead of the ```.difference()``` method

    - Example

        ```python
        set_1 = {1,2,3}
        set_2 = {2,3,4,5}

        diff_set_1 = set_1.difference(set_2)
        diff_set_2 = set_2.difference(set_1)        

        diff_minus_set_1 = set_1 - set_2
        diff_minus_set_2 = set_2 - set_1

        print(diff_set_1) # prints {1}
        print(diff_set_2) # prints {4,5}

        print(diff_minus_set_1) # prints {1}
        print(diff_minus_set_2) # prints {4,5}
        ```

## Set Comprehensions

- **Set Comprehension** is a syntax for creating sets using a ```for``` statement with an interable data type and an action performed on each item within the iterable (which can be a method invocation, math operation, etc.)

    - Example

        ```python
        comp_1 = {even for even in range(2, 11, 2)}
        comp_2 = {even+1 for even in range(2, 11, 2)}
        comp_3 = {str(even) + '!' for even in range(2, 11, 2)}

        print(comp_1) # prints {2, 4, 6, 8, 10}
        print(comp_2) # prints {3, 5, 7, 9, 11}
        print(comp_3) # prints {'4!', '2!', '6!', '10!', '8!'}

        # Remember that order is not guaranteed in sets, so the print order may be different from the order in which items were added to a set
        ```