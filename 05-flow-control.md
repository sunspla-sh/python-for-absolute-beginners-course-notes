# Flow Control

## Intro To Flow Control

- Comparison Operators

    - ```>``` (Greater Than Operator)

        - Example

            ```python
            print(5 > 2) # prints True
            print(2 > 5) # prints False
            print(7 > 7) # prints False
            ```

    - ```<``` (Less Than Operator)

        - Example

            ```python
            print(5 < 2) # prints False
            print(2 < 5) # prints True
            print(7 < 7) # prints False
            ```

    - ```>=``` (Greater Than Or Equal To Operator)

        - Example

            ```python
            print(5 >= 2) # prints True
            print(2 >= 5) # prints False
            print(7 >= 7) # prints True
            print(7.0 >= 7) # prints True
            ```

    - ```<=``` (Less Than Or Equal To Operator)

        - Example

            ```python
            print(5 <= 2) # prints False
            print(2 <= 5) # prints True
            print(7 <= 7) # prints True
            print(7.0 <= 7) # prints True
            ```

    - ```!=``` (Not Equal To Operator)

        - Example

            ```python
            print(5 != 2) # prints True
            print(2 != 2) # prints False
            print('hi' != 'hi') # prints False
            print('Hi' != 'hi') # prints True
            print('yo' != 'hi') # prints True
            print(5.0 != 5) # prints False
            ```

    - ```==``` (Equal To Operator)

        - Example

            ```python
            print(5 == 2) # prints False
            print(2 == 2) # prints True
            print('hi' == 'hi') # prints True
            print('Hi' == 'hi') # prints False
            print('yo' == 'hi') # prints False
            print(5.0 == 5) # prints True
            ```

- Boolean Operators

    - ```and``` (And Operator)

        - Example

            ```python
            print(True and True) # prints True
            print(True and False) # prints False
            print(False and True) # prints False
            print(False and False) # prints False
            ```

    - ```or``` (Or Operator)

        - Example

            ```python
            print(True and True) # prints True
            print(True and False) # prints True
            print(False and True) # prints True
            print(False and False) # prints False
            ```

    - ```not``` (Not Operator)

        - Example

            ```python
            print(not True) # prints False
            print(not False) # prints True
            ```

## Quiz 4: Comparison Operators

- N/A

## Quiz 5: Boolean Operators

- N/A

## If Statements

- The ```if``` statement is a flow control statement used to execute a block of code when a given condition evaluates to ```True```

    - Example

        ```python
        if 5 > 1:
          print("Five is greater than one")

        if 5 < 1:
          print("Five is less than one")

        # Only "Five is greater than one" will print, because the condition 5 > 1 evaluates to True, while the condition 5 < 1 evaluates to False
        ```

## Else Statements

- The ```else``` statement is a flow control statement used to execute a block of code when an associated ```if``` statement condition evaluates to ```False```

    - Example

        ```python
        if 5 > 1:
          print("Five is greater than one")
        else:
          print("Five is less than one")

        if 5 < 1:
          print("Five is definitely less than one")
        else:
          print("Five is definitely greater than one")

        # "Five is greater than one" will print, because the condition 5 > 1 evaluates to True, then "Five is definitely greater than one" will print, because the condition 5 < 1 evaluates to False
        ```

## Nested If and Else Statements

- ```if``` and ```else``` statements can be nested to arbitrary levels

    - Example

        ```python
        fruit = 'pear'

        if fruit == 'apple' or fruit == 'pear':
          print('You picked a tasty fruit!')
          if fruit == 'apple':
            print('*crunch*')
          else:
            print('*squish*')
        else:
          print('Ick!')
        ```

## Programming Challenge: Grade Determiner

- Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams. You work as a teacher's assistant and due to her busy schedule she has requested that you write a program which will determine the grades of the class's students.

    - Her grading scale is as follows:

        - A score of 90 or above is an A

        - A score of 80 or above is a B

        - A score of 70 or above is a C

        - A score of 60 or above is a D

        - A score any lower is an F

1. For this exercise, start by creating a variable and assigning that variable a student's score as an integer using input().

2. Then, using nested if and else statements and the following set of rules, determine and then display the student's grade along with their score using print(). 

    - If the student's score is greater than or equal to 90, then the student will receive an A grade.

    - Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.

    - Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.

    - Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.

    - Otherwise, the student will receive an F grade.

- Make sure to run your program multiple times and test it with values for each 5 of the different grades to make sure that the correct output is displayed for any value entered as a student's score.

## Programming Challenge: Grade Determiner Solution

- See solution in [05-grade-determinor.py](./python-projects/05-grade-determinor.py)

## Elif Statements

- The ```elif``` statement allows for additional conditions to be evaluated in an ```if``` statement

    - Example

        ```python
        user_num = int(input("Enter an integer:\n"))
        
        if user_num < 0:
          print("The number you entered was less than 0.")
        elif user_num == 0:
          print("The number you entered was exactly 0.")
        else:
          print("The number you entered was greater than 0.")
        ```

## Programming Challenge: Roman Numeral Equivalent

- For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

    - Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.

    - For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.

## Programming Challenge: Roman Numeral Equivalent Solution

- See solution in [05-roman-numeral-equivalent.py](./python-projects/05-roman-numeral-equivalent.py)

## Truthy and Falsy Values

- Truthy values are values other than ```True```, which act as ```True``` when used in a conditional statement

    - List of Truthy Values

        - ```"asdf"``` (Non-Empty String)

        - ```1``` (Integer Non-Zero)

        - ```1.0``` (Float Non-Zero)

        - ```1j``` (Complex Non-Zero)

        - ```Decimal(1)``` (Decimal Non-Zero)

        - ```Fraction(1,1)``` (Fraction Non-Zero)

        - ```(1)``` (Non-Empty Tuple)

        - ```[1]``` (Non-Empty List)

        - ```{name: 'bob'}``` (Non-Empty Dictionary)

        - ```set(1)``` (Non-Empty Set)

        - ```range(1)``` (Non-Empty Range)

- Falsy values are values other than ```False```, which act as ```False``` when used in a conditional statement

    - List of Falsy Values

        - ```""``` (Empty String)

        - ```0``` (Integer Zero)

        - ```0.0``` (Float Zero)

        - ```0j``` (Complex Zero)

        - ```Decimal(0)``` (Decimal Zero)

        - ```Fraction(0,1)``` (Fraction Zero)

        - ```()``` (Empty Tuple)

        - ```[]``` (Empty List)

        - ```{}``` (Empty Dictionary)

        - ```set()``` (Empty Set)

        - ```range(0)``` (Empty Range)

        - ```None``` (None)

        - ```False``` (False)

- The ```bool()``` function will evaluate the Boolean value of any data that you pass into the function as a parameter

    - Example

        ```python
        print(bool('asdf')) # prints True
        print(bool(1)) # prints True
        print(bool(1.0)) # prints True
        print(bool(5)) # prints True
        print(bool(5.123)) # prints True
        print(bool(1j)) # prints True
        print(bool(Decimal(1))) # prints True
        print(bool(Fraction(1,1))) # prints True
        print(bool((1))) # prints True
        print(bool([1])) # prints True
        print(bool({name: 'bob'})) # prints True
        print(bool(set(1))) # prints True
        print(bool(range(1))) # prints True

        print(bool('')) # prints False
        print(bool(0)) # prints False
        print(bool(0.0)) # prints False
        print(bool(0j)) # prints False
        print(bool(Decimal(0))) # prints False
        print(bool(Fraction(0,1))) # prints False
        print(bool(())) # prints False
        print(bool([])) # prints False
        print(bool({})) # prints False
        print(bool(set())) # prints False
        print(bool(range(0))) # prints False
        print(bool(None)) # prints False
        print(bool(False)) # prints False
        ```

