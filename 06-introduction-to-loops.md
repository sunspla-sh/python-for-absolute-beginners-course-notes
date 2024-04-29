# Introduction To Loops

## While Loops

- The ```while``` statement is used to repeatedly execute a block of code until a given condition evaluates to ```False```

    - Example

        ```python
        counter = 1
        while counter < 5:
          print("The counter is currently " + str(counter))
          counter += 1

        # This example prints the following:
        # The counter is currently 1
        # The counter is currently 2
        # The counter is currently 3
        # The counter is currently 4
        ```

## While Loops Exercise

- For this exercise, you will print 10 descending integers starting from 10 and ending at 1 with each integer being 1 less than the last and each integer printed on a new line.

    - Create a variable and assign it the integer 10.

    - Then, print
        ```
        10

        9

        8

        7

        6

        5

        4

        3

        2

        1
        ```

    - in the output by using a while loop to print numbers while the variable does not equal 0.  Use the -= operator to reassign descending values to the variable.

## While Loops Exercise Solution

- See solution in [06-while-loops.py](./python-projects/06-while-loops.py)

## Programming Challenge: Sum Of Numbers From A Positive Integer

- Write a program which gets a positive integer from a user using input() and assigns it to a variable.

- The program should then use a while loop to get the sum of all of the integers from the integer that was entered by the user down to 1.  For example, if the integer entered by the user was 6, the while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.

- At the bottom of your program create two print statements.  One will display the user entered integer and the other will display the sum found by the while loop.

## Programming Challenge: Sum Of Numbers From A Positive Integer Solution

- See solution in [06-sum-of-numbers-from-a-positive-integer.py](./python-projects/06-sum-of-numbers-from-a-positive-integer.py)

## For Loops

- The ```for``` statement is used to repeatedly execute a block of code for a pre-determined number of iterations that are set when the ```for``` statement is declared

    - Example

        ```python
        int_10 = range(1, 5)

        for x in int_10:
          print("The value x is currently " + str(x))

        # This example prints the following:
        # The value x is currently 1
        # The value x is currently 2
        # The value x is currently 3
        # The value x is currently 4
        ```

        ```python
        word = 'house'

        for letter in word:
          print(letter)

        # This example prints the following:
        # h
        # o
        # u
        # s
        # e
        ```

## For Loops Exercise

- Use a for loop to print each letter from the string "hello world".

## For Loops Exercise Solution

- See solution in [06-for-loops.py](./python-projects/06-for-loops.py)

## Programming Challenge: Find The Number Of Characters In A String

- In a .py file, write a program which calculates the number of characters in a string.

- The string should be entered using input() and assigned to a variable. 

- Use print() twice at the end of your program.  The first print() will print the string that the user entered and the second print() will display the number of characters in the string.  For example, if the user entered the string "hello world", the number of characters would be 11.

## Programming Challenge: Find The Number Of Characters In A String Solution

- See solution in [06-find-the-number-of-characters-in-a-string.py](./python-projects/06-find-the-number-of-characters-in-a-string.py)

## range()

- The ```range()``` function is used to generate a sequence of numbers, typically so that you can iterate over them with a ```for``` statement

    - Range can be used with one, two, or three parameters

        - ```range(stop)```

            - ```stop```

                - The stopping value of the range, exclusive

            - Note that in this case, the starting value is assumed to be ```0``` and the step value is assumed to be ```1```

        - ```range(start, stop, step)``` has three parameters

            - ```start```

                - The starting value of the range, inclusive

            - ```stop```

                - The stopping value of the range, exclusive

            - Note that in this case, the step value is assumed to be ```1```

        - ```range(start, stop, step)```

            - ```start```

                - The starting value of the range, inclusive

            - ```stop```

                - The stopping value of the range, exclusive

            - ```step```

                - The step value of the range

    - Example

        ```python
        my_range = range(5)

        for x in my_range:
          print(x)

        # This example prints the following:
        # 0
        # 1
        # 2
        # 3
        # 4
        ```

        ```python
        my_range = range(1,6)

        for x in my_range:
          print(x)

        # This example prints the following:
        # 1
        # 2
        # 3
        # 4
        # 5
        ```

        ```python
        my_range = range(1,10,2)

        for x in my_range:
          print(x)

        # This example prints the following:
        # 1
        # 3
        # 5
        # 7
        # 9
        ```

## Quiz 6: range()

- N/A

## Programming Challenge: Fizz Buzz

- Write a program that iterates over the integers 1 through 50 using a loop.

- However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.  For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".  For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.

- All of the integers which are not multiples of 3 or 5 should just be printed as themselves.

## Programming Challenge: Fizz Buzz Solution

- See solution in [06-fizz-buzz.py](./python-projects/06-fizz-buzz.py)

## Programming Challenge: Factorial

- Create a function which takes one positive integer as its input and returns its factorial.

- To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

## Programming Challenge: Factorial Solution

- See solution in [06-factorial.py](./python-projects/06-factorial.py)