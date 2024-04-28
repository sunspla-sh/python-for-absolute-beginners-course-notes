# Python Basics

## Variables and Assignment

- **Variables** are named storage of data in computer memory

- **Assignment** is the act of storing data in a variable

- **Initialization** is the act of assignment to a new variable

- Python does NOT have uninitialized variables (also known as variable declarations in other programming languages), i.e. variables that have been created but not yet assigned a value

    - Examples of correct and incorrect variable creation in Python

        ```python
        # Correct variable creation (Initialization)
        my_example_var = 5

        # Incorrect variable creation (Declaration)
        my_second_example_var
        ```
- **Reassignment** is the act of assigning new data to a variable that previously held different data

    - Examples of assignment and reassignment in Python

        ```python
        # Assignment
        test_var = 5

        # Reassignment (because we overwrote the old value of 5)
        test_var = 8
        ```
- Variable Naming Syntax Rules

    - CANNOT start with a number (but later is okay)

        - Example

            ```python
            # NOT ALLOWED
            4ever_variable = 5

            # ALLOWED
            testing4 = 6

            # ALLOWED
            testing4th = 7
            ```

    - CANNOT have a space in the name

        - Example

            ```python
            # NOT ALLOWED
            test variable = 6
            ```

    - CANNOT use special characters

        - Example

            ```python
            # NOT ALLOWED
            $please.avoid!? = 5
            ```
    
    - PROPER variable naming should be camelCase or snake_case format

        - Example

            ```python
            # camelCase
            myFavoriteTestVariable = 5

            # snake_case
            my_second_favorite_test_variable = 6
            ```

## Basic Data Types

    - Floating-Point Number

        - Any number with a decimal point

        - Example

            ```python
            float_1 = 1.2345
            
            float_2 = -1.25

            float_3 = 0.0

            float_4 = 13.0

            float_5 = -0.5
            ```

    - Integer

        - Any number with no decimal

        - Example

            ```python
            int_1 = 7

            int_2 = -52

            int_3 = 0

            int_4 = 900

            int_5 = -749
            ```

    - Boolean

        - True or False

        - Example

            ```python
            bool_1 = True

            bool_2 = False
            ```

## Variables and Assignment Exercise

- Do all of this in a .py file in Pycharm

    1. Create a variable and assign it an integer

    2. Create a second variable and assign it a float

    3. Create a third variable and assign it a Boolean value

    4. Re-assign a different integer to the first variable you created

## Variables and Assignment Exercise Solutions

- See solutions in [02-variables-and-assignment-exercise.py](./python-projects/02-variables-and-assignment-exercise.py)

## Comments and Math Operators

- Comments are characters that are ignored when a program is run

    - To make a comment in python, use the ```#``` character

        ```python
        # This is an example comment
        my_int = 5
        print(my_int) # This prints out 5
        # Note that code in comments is ignored: my_int = 6
        print(my_int) # This still prints out 5
        ```

- Operators

    - Operators are used to transform one or more values into new values

    - Math Operators (non-exhaustive):

        - ```+``` (Addition Operator)

            ```python
            my_addition = 5 + 2
            print(my_addition) # Prints 7
            ```

        - ```-``` (Subtraction Operator)

            ```python
            my_subtraction = 5 - 2
            print(my_subtraction) # Prints 3
            ```

        - ```*``` (Multiplication Operator)

            ```python
            my_multiplication = 5 * 2
            print(my_multiplication) # Prints 10
            ```

        - ```/``` (Division Operator)

            ```python
            my_division = 5 / 2
            print(my_division) # Prints 2.5
            ```

        - ```**``` (Exponentiation Operator)

            ```python
            my_exponentiation = 5 ** 2
            print(my_exponentiation) # Prints 25
            ```

        - ```//``` (Floor-Division Operator)

            ```python
            my_floor_division = 5 // 2
            print(my_floor_division) # Prints 2
            ```

        - ```%``` (Modulo Operator)

            ```python
            my_modulo = 5 % 2
            print(my_modulo) # Prints 1
            ```

    - Assignment Operators (non-exhaustive):

        - ```+=``` (Addition-Assignment Operator)

            ```python
            my_addition = 5
            my_addition += 2
            print(my_addition) # Prints 7
            ```

        - ```-=``` (Subtraction-Assignment Operator)

            ```python
            my_subtraction = 5
            my_subtraction -= 2
            print(my_subtraction) # Prints 3
            ```

        - ```*=``` (Multiplication-Assignment Operator)

            ```python
            my_multiplication = 5
            my_multiplication *= 2
            print(my_multiplication) # Prints 10
            ```

        - ```/``` (Division-Assignment Operator)

            ```python
            my_division = 5
            my_division /= 2
            print(my_division) # Prints 2.5
            ```

        - ```**``` (Exponentiation-Assignment Operator)

            ```python
            my_exponentiation = 5
            my_exponentiation **= 2
            print(my_exponentiation) # Prints 25
            ```

        - ```//``` (Floor-Division-Assignment Operator)

            ```python
            my_floor_division = 5
            my_floor_division //= 2
            print(my_floor_division) # Prints 2
            ```

        - ```%``` (Modulo-Assignment Operator)

            ```python
            my_modulo = 5
            my_modulo %= 2
            print(my_modulo) # Prints 1
            ```

- Order of Operations

    1. ```()```

    2. ```**```

    3. ```%```, ```/```, ```//```, and ```*```

    4. ```+``` and ```-```

    - For any operators with the same level of precedence, the operations occur left to right

## Quiz 1: Comments and Math Operators

- N/A

## Comments and Math Operators Review Exercise

- Do all of this in a .py file in Pycharm

    1. Create a variable and assign it the sum of two integers

    2. Create a variable and assign it the difference of two integers

    3. Create a variable and assign it the result of one integer being divided by another integer

    4. Create a variable and assign it the product of two integers

    5. Create a variable and assign it the result of 3 raised to the 8th power

    6. Create a variable and assign it the result of 10 floor division 3

    7. Create a variable and assign it the integer 2 using the expression 17 modulo integer

## Comments and Math Operators Review Exercise Solution

- See solutions in [02-comments-and-math-operators-review-exercises.py](./python-projects/02-comments-and-math-operators-review-exercises.py)

## print()

- The ```print()``` function will output values to ```stdout```

    ```python
    my_var = 5
    print(my_var) # prints 5
    print(my_var * 5) # prints 25
    print(7) # prints 7
    print(6 - 2) # prints 4
    print(my_var, my_var) # prints 5 5
    print(my_var, 100) # prints 5 100
    ```

## print() Exercises

- Do all of this in a .py file in Pycharm

- Make a comment for each line of code you write.

1. Create a variable, assign it a value of any data type, then use print() to display its assigned value in the output

2. Use print() to print a value of any data type directly

3. Use print() to display the result of an expression that uses at least 2 math operators

## print() Exercises Solutions

- See solutions in [02-print.py](./python-projects/02-print.py)

## More On Floats

- When using floats in Python (and other programming languages), decimal approximation errors can occur

    - Example

        ```python
        print(1.23 + 2.80)
        # prints 4.029999999999999 instead of 4.03
        ```

- These errors occur because the Python language is built on top of the C language, which approximates floats using a fixed number of binary digits

- To get avoid approximation errors, either use integers (by multiply by powers of 10) or the ```round(value-to-round, decimal-places-to-round)``` function

    - Example
    ```python
    print((123 + 280) / 100) # prints 4.03
    print(round(1.23 + 2.80, 2)) # prints 4.03
    ```

## Quiz 2: More On Floats

- N/A

## Programming Challenge: Grocery Store Purpose

- A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:

    1. Penne 16 oz Pack of 12 - $16.68

    2. Arrabiata Pasta Sauce 24 oz - $6.98

    3. Bag of 20 Organic Garlic Cloves - $16.78

    4. Italian Seasoning 1.5 oz Bottle - $15.26

    5. Artisan Baguettes Twin Pack - $3.00

    6. 12 oz Bag of Meatballs - $4.39

- In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression

    - The subtotal is just the sum of all of their prices

- Use print() to display the result of the expression.

## Grocery Store Purchase Solution With Integers

- See solutions in [02-grocery-store-purchase.py](./python-projects/02-grocery-store-purchase.py)

## Grocery Store Purchse Solution With Round

- See solutions in [02-grocery-store-purchase.py](./python-projects/02-grocery-store-purchase.py)