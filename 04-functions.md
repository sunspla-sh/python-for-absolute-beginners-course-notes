# Functions

## Functions

- A **function** is a block of organized, reusable code that is used to perform a single task

    - Example

        ```python
        def print_four():
          print('this')
          print('is')
          print('an')
          print('example')

        print_four()
        print_four()
        # The result of calling this function twice will print:
        # this
        # is
        # an
        # example
        # this
        # is
        # an
        # example
        ```

- The act of creating a function is also referred to as **defining a function**

    - The syntax for defining a function is the following:

        ```python
        def some_function_name():
          # your code goes here
          print('hello')
          # your other code goes here

        some_function_name() # prints hello
        ```

        - Note that ```def``` starts a function

        - The function name follows the same rules as variables

        - The function name is followed by parenthesis (```()```) and a colon (```:```)

        - The code within the function must be indented

- The act of using a function is known as **calling a function** or **invoking a function**

    - To call a function, type its name followed by parenthesis (```()```)

        - Example

            ```python
            def some_test_func():
              # your code goes here
              print('stuff')
              # your other code goes here


            some_test_func() # prints stuff
            ```

        - The best practice after defining a function in python is to leave two empty lines for readability

- Functions can have **parameters**, which are placeholder variables for data that will be used within the function

    - Example

        ```python
        def hello_name(name):
          print('hello ' + name)


        hello_name('tim') # prints hello tim
        ```

    - Parameter naming follows the same rules as variables

    - Functions can have as many parameters as you want

        - Example

            ```python
            first_str = 'The number'

            def some_func(p1, p2, p3):
              print(p1 + str(p2) + p3)

            
            some_func(first_str, 5, 'is an integer.') # prints The number 5 is an integer.
            ```

    - Parameters can have default values

        - Example

            ```python
            def test_default_values(num1=7, num2=8):
              print(num1 * num2)

            
            test_default_values() # prints 56
            test_default_values(1) # prints 8
            test_default_values(2,2) # prints 4
            ```

- The **return** of a function is a value that will be passed out of the function for later usage

    - Example

        ```python
        def test_return(param):
          return param + 5

        
        val_one = test_return(2) # val_one is 7
        val_two = val_one + 3 # val_two is 10
        print(val_two) # prints 10
        ```

## Function With No Parameters Exercise

- Do all of this in a .py file in Pycharm.

    1. Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"

    2. Call the function hello_world_printer()

## Function With No Parameters Exercise Solution

- See solution in [04-function-with-no-parameters.py](./python-projects/04-function-with-no-parameters.py)

## Function With One Parameter Exercise

- Do all of this in a .py file in Pycharm

    1. Create a function called name_printer which takes 1 parameter and prints it

    2. Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.

    3. Call name_printer() with the variable "name" as its argument.

## Function With One Parameter Exercise Solution

- See solution in [04-function-with-one-parameter.py](./python-projects/04-function-with-one-parameter.py)

## Programming Challenge: Volume Of A Rectangular Prism

- Do all of this in a .py file in Pycharm.

- For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.

    1. First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().

    2. Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism calculated using those 3 parameters.

    3. Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

## Programming Challenge: Volume Of A Rectangular Prism Solution

- See solution in [04-volume-of-a-rectangular-prism.py](./python-projects/04-volume-of-a-rectangular-prism.py)

## Programming Challenge: Celcius To Fahrenheit

- The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:

    - F = 1.8 * C + 32

    - Where F is the Fahrenheit temperature and C is the Celsius temperature.

- In a .py file, create a variable and assign it an integer representing a celsius temperature that is entered as user input().  input()'s message should prompt the user to enter an integer value.

- For this programming challenge, you will then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.

- At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:  "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".

- To make sure that the function works, run your program multiple times and call the function on different user entered integer values both negative and positive.

## Programming Challenge: Celcius To Fahrenheit With Integers Solution

- See solution in [04-celcius-to-fahrenheit.py](./python-projects/04-celcius-to-fahrenheit.py)

## Programming Challenge: Celcius To Fahrenheit With round() Solution

- See solution in [04-celcius-to-fahrenheit.py](./python-projects/04-celcius-to-fahrenheit.py)

## Importing Modules

- **Modules** are sets of functions created and shared by other people so that we don't need to re-create functions for common tasks from scratch each time we need them

    - There are three different ways to import functions from modules

        - Generic Imports

            - Importing the entire module by name

            - Example

                ```python
                import random
                
                print(random.randint(1,10))
                ```

        - Function Imports

            - Importing individual functions from a module

            - Example

                ```python
                from random import randint

                print(randint(1,10))
                ```

        - Universal Imports

            - Importing all functions from a module

            - Example

                ```python
                from random import *

                print(randint(1,10))
                ```

## Programming Challenge: Miles Per Gallon

- For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.

    1. In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400

        - The first variable represents the number of gallons of gas that the car's fuel tank holds
        
        - The second variable represents the miles that the car can travel on a full tank before needing a refuel

    2. Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate the car's MPG and display it in the output using print()

        - Use floor division instead of regular division for this calculation to get an integer instead of a float
        
            - This will give a realistic approximation of miles per gallon even though floats such as 19.8 round down a large amount when using floor division since sometimes, car manufacturers sometimes exaggerate miles per gallon
    
    3. In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank and miles it can travel on a full tank with two different print statements.

## Programming Challenge: Miles Per Gallon Solution

- See solution in [04-miles-per-gallon.py](./python-projects/04-miles-per-gallon.py)

## Variable Scope

- Scope is the section of a program in which a given variable is accessible

- There are four different types of scope in Python

    - Local Scope

        - Applies to variables within a function

        - Example

            ```python
            def test_scope():
              name = 'bob'
              print(name)

            test_scope() # prints bob
            print(name) # causes an error because bob is not accesible outside of test_scope function
            ```

    - Enclosing Scope

        - Applies to variables within nested functions

        - Example

            ```python
            def test_scope():
              name = 'bob'
              print('outer: ' + name) # prints outer: bob

              def second_scope():
                message = 'hi'
                print('inner: ' + message) # prints inner: hi 
                print('inner: ' + name) # prints inner: bob


              second_scope()
              print('outer: ' + message) # causes an error


            test_scope()
            ```

    - Global Scope

        - Applies to variables declared outside of any function

        - Example

            ```python

            global_var = 'yo'

            def test_scope():
              name = 'bob'
              print('outer: ' + name) # prints outer: bob
              print('outer: ' + global_var) # prints outer: yo

              def second_scope():
                message = 'hi'
                print('inner: ' + message) # prints inner: hi 
                print('inner: ' + name) # prints inner: bob
                print('inner: ' + global_var) # prints inner: yo 


              second_scope()
              print('outer: ' + message) # causes an error


            print(global_var) # prints yo
            test_scope()
            ```

        - Global variables are hoisted, meaning that they are created first when a program is run, before any functions are defined, even if they are declared at the end of the program instead of at the beginning

            - However, global variables must still be declared before any functions calls/invocations that use the global variables

            - Hoisting Example

                ```python
                # This example runs fine
                def print_yo():
                  print(test_yo)


                test_yo = 'yo'
                print_yo()
                ```

            - Error Example

                ```python
                # This example results in an error
                def print_yo():
                  print(test_yo)


                print_yo()
                test_yo = 'yo'
                ```

        

    - Built-In Scope

        - Applies to all reserved keywords of Python (e.g. ```return```, ```def```, etc.)

        - These reserved keywords can be used anywhere inside or outside of functions

- Using the reserved keyword ```global``` will change a local variable to a global variable

    - Example

        ```python
        fruit = 'banana'
        def print_fruit():
          global fruit
          fruit = 'pear'
          print(fruit)


        print_fruit() # prints pear
        print(fruit) # also prints pear

## Quiz 3: Variable Scope

- N/A