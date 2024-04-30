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

## Indexes and List Slicing Exercises

## Indexes and List Slicing Exercises Solutions

- See solutions in [08-indexes-and-list-slicing.py](./python-projects/08-indexes-and-list-slicing.py)

## del and List Methods

## del and List Methods Exercises

## del and List Methods Exercises Solutions

- See solutions in [08-del-and-list-methods.py](./python-projects/08-del-and-list-methods.py)

## Lists vs Strings

