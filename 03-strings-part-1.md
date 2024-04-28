# Strings - Part 1

## Strings

- **Strings** are sequences of characters

    - These sequences can be any combination of numbers, spaces, uppercase letters, lowercase letters, underscores, or symbols such as periods, exclamation points, etc.

    - To create a string, you can use either single quotes (```''```) or double quotes (```""```) around any sequence of characters

        - Example

            ```python
            my_string_single = 'hello'
            my_string_double = "world!"
            print(my_string_single) # prints hello
            print(my_string_double) # prints world!
            ```

- Each character in a string has an **index**, which is a number (starting from zero) that represents the character's position in the string

    - Example

        ```python
        my_string = 'hello'
        # the index of h is 0
        # the index of e is 1
        # the index of l is 2
        # the index of l is 3
        # the index of o is 4
        ```

    - The index of a character in a string can be used retrieve that character with square bracket syntax (```[]```)

        - Example

            ```python
            my_string = 'hi'
            print(my_string[0]) # prints h
            print(my_string[1]) # prints i
            print("asdf"[2]) # prints d

            # Note that accessing a character by index does not change the original string
            my_short_string = my_string[0]
            print(my_short_string) # prints h
            print(my_string) # prints hi
            ```

- **String Slicing** allows retrieving one or more characters from a string simultaneously with square bracket syntax (```[]```) and a colon (```:```)

    - Example

        ```python
        my_string = 'apple'
        print(my_string[:2]) # prints ap
        print(my_string[1:3]) # prints pp
        print(my_string[3:]) # prints le

        # Note that slicing does not change the original string
        my_short_string = my_string[3:]
        print(my_short_string) # prints le
        print(my_string) # prints apple
        ```

**Concatentation** is the act of combining two or more strings together, which is done using the addition operator (```+```)

    - Example

        ```python
        print('hello' + ' ' 'world') #prints hello world
        my_string_one = 'r2-'
        my_string_two = 'd2'
        my_droid = my_string_one + my_string_two
        print(my_droid) # prints r2-d2
        ```

## Strings Exercises

- Do all of this in a .py file in Pycharm

  1. Create a variable and assign it the string "Just do it!"

  2. Access the "!" from the variable by index and print() it

  3. Print the slice "do" from the variable

  4. Get and print the slice "it!" from the variable

  5. Print the slice "Just" from the variable

  6. Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

## Strings Exercises Solutions

- See solutions in [03-strings.py](./python-projects/03-strings.py)

## type() and str()

- The ```type()``` function allows you to determine the type of a piece of data

    - Example

        ```python
        ex_1 = False
        ex_2 = 29
        ex_3 = 4.1253
        print(type(ex_1)) # prints <class 'bool'>
        print(type(ex_2)) # prints <class 'int'>
        print(type(ex_3)) # prints <class 'float'>
        ```

- The ```str()``` function converts any data type to a string

    - Example

        ```python
        ex_4 = str(True)
        ex_5 = str(5)
        ex_6 = str(3.21)
        print(type(ex_4)) # prints <class 'str'>
        print(type(ex_5)) # prints <class 'str'>
        print(type(ex_6)) # prints <class 'str'>
        ```

## Escape Sequences

- **Escape Sequences** are special characters starting with a backslash (```\```) that can be inserted into strings to manipulate their presentation when printed

    - ```\t``` (Tab Character)

        - Creates a horizontal space or indent in a string

        - Example
            
            ```python
            print('This\tis\ta\tlot\tof\tspace!')
            # The above string prints:
            # This  is  a lot of  space!
            ```

    - ```\n``` (Newline Character)

        - Creates a new line in a string

        - Example

            ```python
            print('line one\nline two')
            # The above string prints:
            # line one
            # line two
            ```

    - ```\'``` (Single Quote Character)

        - Adds a single quote to the string

            ```python
            print('Here\'s a single quote: \'')
            ```

    - ```\"``` (Double Quote Character)

        - Adds a double quote to the string

            ```python
            print("Here's a double quote: \"")
            ```

    - ```\\``` (Backslash Character)

        - Adds a backslash to the string

        - Example

            ```python
            print("Here's a backslash: \\")
            ```

    - Note that this list is non-exhaustive and that there are many more escape sequences...

## type(), str(), and Escape Sequences Exercises

- Do all of this in a .py file in Pycharm.

    1. Create a variable and assign it a float

    2. Use print() and type() to print the data type of the variable in the output

    3. Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result

    4. print() the string "Hello, I'm Bob, it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)

## type(), str(), and Escape Sequences Exercises Solutions

- See solutions in [03-type-str-escape-sequences.py](./python-projects/03-type-str-escape-sequences.py)

## Programming Challenge: Asterisk Triangle

- Using your knowledge of escape sequences, create a single print() statement with single string inside of it that displays this when the program is run:

        *******
         *****
          ***
           *

## Asterisk Triangle Solution

- See solution in [03-asterisk-triangle.py](./python-projects/03-asterisk-triangle.py)

## input()

- The ```input()``` function gets input strings from a user of our programs

    - Example

        ```python
        name = input("What is your name?")
        # Assume that the user inputted bob
        print("Your name is: " + name + ".")
        # The previous line prints Your name is: bob.
        print(type(name))
        # The previous line prints <class 'str'>
        ```

    - Note that the user input is always converted to a string, even if the user types a number

## Programming Challenge: Monty Python

- In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.

    1. What is your name?

    2. What is your quest?

    3. What is your favorite color?

- Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

## Monty Python Solution

- See solution in [03-monty-python.py](./python-projects/03-monty-python.py)

## int() and float()

- The ```int()``` function turns a string into an integer

    - Example

        ```python
        user_int = int(input("Please enter an integer.\n"))
        # Assume that the user inputted 7
        print(user_int) # prints 7
        print(type(user_int)) # prints <class 'int'>
        ```

    - Note that using the ```int()``` function on a float will truncate the float

- The ```float()``` function turns a string into a float

    - Example

        ```python
        user_float = float(input("Please enter a float.\n"))
        # Assume that the user inputted 5.5
        print(user_float) # prints 5.5
        print(type(user_float)) # prints <class 'float'>
        ```

## int() Exercise

- In a Python file, use input() to ask the user to enter an integer that 10 will be added to.  Assign what they type to a variable.

- print() the sum of the integer they entered and 10.

## int() Exercise Solution

- See solution in [03-int.py](./python-projects/03-int.py)