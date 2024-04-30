# Strings - Part 2

## String Methods 1

- **Methods** are functions defined within classes/data types that operate on instances of those classes/data types

- The ```.upper()``` method is a string method used to copy and convert any string to uppercase letters

    - Example

        ```python
        word = 'hello'
        print(word.upper()) # prints HELLO
        print(word) # prints hello
        ```

    - Note that the ```.upper()``` method does not change the original string

- The ```.lower()``` method is a string method used to copy and convert any string to lowercase letters

    - Example

        ```python
        word = 'DUDE'
        print(word.lower()) # prints dude
        print(word) # prints DUDE
        ```

    - Note that the ```.lower()``` method does not change the original string

- The ```.isupper()``` method is a string method that returns ```True``` if a string is made of all uppercase letters, excluding special characters (e.g. ```$```, ```!```, etc.), otherwise it returns ```False```

    - Example

        ```python
        upper_word = 'DUDE'
        mixed_word = 'Haha'
        no_letters_empty = ''
        no_letters_special = '!!!'
        print(upper_word.isupper()) # prints True
        print(mixed_word.isupper()) # prints False
        print(no_letters_empty.isupper()) # prints False
        print(no_letters_special.isupper()) # prints False
        ```

- The ```.islower()``` method is a string method that returns ```True``` if a string is made of all lowercase letters, excluding special characters (e.g. ```$```, ```!```, etc.), otherwise it returns ```False```

    - Example

        ```python
        lower_word = 'dude'
        mixed_word = 'Haha'
        no_letters_empty = ''
        no_letters_special = '!!!'
        print(lower_word.islower()) # prints True
        print(mixed_word.islower()) # prints False
        print(no_letters_empty.isupper()) # prints False
        print(no_letters_special.isupper()) # prints False
        ```
- The ```.isalpha()``` method is a string method that returns ```True``` if a string is made of only letters, otherwise it returns ```False```

    - Example

        ```python
        letter_string = 'dude'
        number_string = '1111'
        mixed_string = 'ha1'
        special_string = 'ha!'
        empty_string = ''
        print(letter_string.isalpha()) # prints True
        print(number_string.isalpha()) # prints False
        print(mixed_string.isalpha()) # prints False
        print(special_string.isalpha()) # prints False
        print(empty_string.isalpha()) # prints False
        ```

- The ```.isalnum()``` method is a string method that returns ```True``` if a string is made of only letters and numbers, otherwise it returns ```False```

    - Example

        ```python
        letter_string = 'dude'
        number_string = '1111'
        mixed_string = 'ha1'
        special_string = 'ha!'
        empty_string = ''
        print(letter_string.isalnum()) # prints True
        print(number_string.isalnum()) # prints True
        print(mixed_string.isalnum()) # prints True
        print(special_string.isalnum()) # prints False
        print(empty_string.isalnum()) # prints False
        ```

- The ```.isdecimal()``` method is a string method that returns ```True``` if a string is made of only numbers, otherwise it returns ```False```

    - Example

        ```python
        letter_string = 'dude'
        integer_string = '1111'
        float_string = '1.0'
        mixed_string = 'ha1'
        special_string = '1!'
        empty_string = ''
        print(letter_string.isdecimal()) # prints False
        print(integer_string.isdecimal()) # prints True
        print(float_string.isdecimal()) # prints False
        print(mixed_string.isdecimal()) # prints False
        print(special_string.isdecimal()) # prints False
        print(empty_string.isdecimal()) # prints False
        ```

    - Note that the string representation of floats (e.g. ```1.0```) contains a period (```.```), which is considered to be a special character, so ```.isdecimal()``` returns ```False``` in that case

- The ```.isspace()``` method is a string method that returns ```True``` if a string is made of only **whitespace** characters, otherwise it returns ```False```

    - A character is **whitespace** if in the Unicode character database (see [unicodedata](https://docs.python.org/3/library/unicodedata.html#module-unicodedata)), either its general category is Zs (“Separator, space”), or its bidirectional class is one of WS, B, or S.

    - Example

        ```python
        space_string = '   '
        no_space_string = 'hi'
        tab_string = '\t'
        empty_string = ''
        print(space_string.isspace()) # prints True
        print(no_space_string.isspace()) # prints False
        print(tab_string.isspace()) # prints True
        print(empty_string.isspace()) # prints False
        ```

- The ```.istitle()``` method is a string method that returns ```True``` if a string is made of only title case words (meaning that the first letter of each word is uppercase and the rest are lowercase), otherwise it returns ```False```

    - Example

        ```python
        title_string = 'Hello'
        multi_title_string = 'Hello Bob'
        mixed_string = 'Hello dude'
        title_end_number_string = 'Hello 111'
        title_begin_number_string = '111 Hello'
        special_string = '!!!Hello$$'
        empty_string = ''
        print(title_string.istitle()) # prints True
        print(multi_title_string.istitle()) # prints True
        print(mixed_string.istitle()) # prints False
        print(title_end_number_string.istitle()) # prints True
        print(title_begin_number_string.istitle()) # prints True
        print(special_string.istitle()) # prints True
        print(empty_string.istitle()) # prints False
        ```

- The ```.startswith()``` method is a string method that returns ```True``` if a string starts with a given sequence of characters, otherwise it returns ```False```

    - Example

        ```python
        name = 'bob'
        print(name.startswith('b')) # return True
        print(name.startswith('bo')) # return True
        print(name.startswith('bob')) # return True
        print(name.startswith('bobby')) # return False
        print(name.startswith('B')) # return False
        print(name.startswith('x')) # return False
        ``` 

- The ```.endswith()``` method is a string method that returns ```True``` if a string ends with a given sequence of characters, otherwise it returns ```False```

    - Example

        ```python
        name = 'bob'
        print(name.endswith('b')) # return True
        print(name.endswith('ob')) # return True
        print(name.endswith('bob')) # return True
        print(name.endswith('B')) # return False
        print(name.endswith('x')) # return False
        ``` 

- The ```.join()``` method is a string method that joins a list of strings together using the original string as the separator for the list of strings

    - Example

        ```python
        print(''.join(['one','two','three'])) # prints onetwothree
        print(' '.join(['one','two','three'])) # prints one two three
        print('-'.join(['one','two','three'])) # prints one-two-three
        print('...'.join(['one','two','three'])) # prints one...two...three
        ```

- The ```.split()``` method is a string method that splits a string into a list by space characters as the default separator, although this can be changed using a parameter

    - Example

        ```python
        print('one, two, three'.split()) # prints ['one,', 'two,', 'three']
        print('one, two, three'.split(',')) # prints ['one', ' two', ' three']
        print('one, two, three'.split(', ')) # prints ['one', 'two', 'three']
        print('one-two-three'.split('-')) # prints ['one', 'two', 'three']
        print('one-two-three'.split()) # prints ['one-two-three']
        print('one-two-three'.split('.')) # prints ['one-two-three']
        ```
## String Methods 1 Exercises

- Do all of this in a .py file in Pycharm:

    1. Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"

    2. Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.

    3. Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.

    4. Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.

    5. Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.

    6. Use the .istitle() method to check if mixed_case is title case and print the result.

    7. Create a variable called title_case and assign it the result of .title() being called on mixed_case.

    8. print() title_case

    9. Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.

    10. Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.

    11. Create a variable called words and assign it the result of split() being used on mixed_case.

    12. print() the variable "words"

    13. Use the .join() method to join together all of the items in the list assigned to words as a single string.  Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.

## String Methods 1 Exercises Solutions

- See solutions in [07-string-methods-1.py](./python-projects/07-string-methods-1.py)

## String Methods 2

- The ```.rjust()``` method is a string method that adds space characters (or a different character of your choice) to the left side of a string

    - With one parameter, ```.rjust(length)``` adds additional space characters to the left side of the string so that the total string length equals the ```length``` parameter

    - With two parameters, ```.rjust(length, char)``` adds additional characters of your choice to the left side of the string so that the total string length equals the ```length``` parameter

    - Example

        ```python
        print("hello world".rjust(15)) # prints "    hello world"
        print("hello world".rjust(15, '*')) # prints "****hello world"
        ```

- The ```.ljust()``` method is a string method that adds space characters (or a different character of your choice) to the right side of a string

    - With one parameter, ```.ljust(length)``` adds additional space characters to the right side of the string so that the total string length equals the ```length``` parameter

    - With two parameters, ```.ljust(length, char)``` adds additional characters of your choice to the right side of the string so that the total string length equals the ```length``` parameter

    - Example

        ```python
        print("hello world".ljust(15)) # prints "hello world    "
        print("hello world".ljust(15, '*')) # prints "hello world****"
        ```

- The ```.center()``` method is a string method that adds space characters (or a different character of your choice) to both sides of a string

    - With one parameter, ```.center(length)``` adds additional space characters to both sides of the string so that the total string length equals the ```length``` parameter

    - With two parameters, ```.center(length, char)``` adds additional characters of your choice to both sides of the string so that the total string length equals the ```length``` parameter

    - Example

        ```python
        print("hello world".center(15)) # prints "  hello world  "
        print("hello world".center(15, '*')) # prints "**hello world**"
        print("hello world".center(16, '*')) # prints "**hello world***"
        print("hello world".center(17, '*')) # prints "***hello world***"
        ```

- The ```.strip()``` method is a string method that removes all whitespace characters (or different characters of your choice) from both sides of a string

    - Note that the removal characters will attempt to be removed in any order, one or more times

    - Example

        ```python
        print("  hi  ".strip()) # prints hi
        print("**hi**".strip()) # prints **hi**
        print("**hi**".strip('*')) # prints hi
        print("blueblueyellowblue".strip('blue'))
        print("blueblueyellowblue".strip('lbeu'))
        ```

- The ```.rstrip()``` method is a string method that removes all whitespace characters (or different characters of your choice) from the right side of a string

    - Note that the removal characters will attempt to be removed in any order, one or more times

    - Example

        ```python
        print("  hi  ".rstrip()) # prints   hi  
        print("**hi**".rstrip()) # prints **hi**
        print("**hi**".rstrip('*')) # prints **hi
        print("hello world".rstrip(" world")) # prints he
        print("hello world".rstrip("rw lod")) # prints he
        ```

- The ```.lstrip()``` method is a string method that removes all whitespace characters (or different characters of your choice) from the left side of a string

    - Note that the removal characters will attempt to be removed in any order, one or more times

    - Example

        ```python
        print("  hi  ".lstrip()) # prints hi  
        print("**hi**".lstrip()) # prints **hi**
        print("**hi**".lstrip('*')) # prints hi**
        print("hello world".lstrip("hello ")) # prints world
        print("hello world".lstrip("helo ")) # prints world
        print("hello world".lstrip("lo he")) # prints world
        ```

- The ```.replace()``` method is a string method that will search for and replace a given substring with another string

    - Example

        ```python
        print("hello world".replace("world", "dolly")) # prints hello dolly
        print("hello world".replace("llo", "y")) # prints hey world
        print("hello world".replace("ll", "")) # prints heo world
        ```

## String Methods 2 Exercises

- Do all of this in a .py file:

    1. Create a variable called the_string and assign it the string "North Dakota".

    2. Call .rjust() on the_string with 17 as its argument and print() the result.

    3. Call .ljust() on the_string with the arguments 17 and "*" then print() the result.

    4. Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.

    5. Use print() to display the string assigned to center_plus.

    6. Call .lstrip() on the_string to remove "North" then print() the result.

    7. Call .rstrip() on center_plus with "+" as its argument and print() the result.

    8. Call .strip() on center_plus with "+" as its argument and print() the result.

    9. Call .replace() on the_string and replace "North" with "South".  print() the result.

## String Methods 2 Exercises Solutions

- See solutions in [07-string-methods-2.py](./python-projects/07-string-methods-2.py)

## len()

- The ```len()``` function returns the length of an iterable data type as an integer

    - In the case of a string, the length is the number of characters that the string contains (including all special characters, escape sequences, etc.)

    - Example

        ```python
        print(len(" asdf")) # prints 5
        print(len(" asdf\n")) # prints 6
        print(len(" asdf\n...")) # prints 9
        ```

## Programming Challenge: String Reverser

- For this challenge, you will be writing a program which uses a for loop to reverse a string. 

    1. Start by creating a variable and assigning it a string as user input using input().

    2. Use a for loop to reverse the string.  You will need to use range with all 3 inputs for this.  In addition, you should create a variable before the for loop and assign it an empty string.  The variable will be reassigned multiple times within the for loop and end up holding the new reversed string.

    3. Print the reversed string at the bottom of your program.

## Programming Challenge: String Reverser Solution

- See solutions in [07-string-reverser.py](./python-projects/07-string-reverser.py)

## Programming Challenge: Word Counter

- For this programming challenge, write a function in a .py file which takes 1 string as an argument, finds out the number of words in that string, then returns that number. 

- For example, if the program was used on the string "This is a string.", then the function would return 4. 

- Assumptions:

    - Assume that the string will be assigned to a variable and that it will contain at least 1 word.

    - Assume that there will never be 2 or more consecutive spaces in a row within the string.

    - Contractions and possessive words with an apostrophe like "it's" or "Brian's" count as 1 word.

    - Hyphenated words like "ice-cream" count as 1 word.

    - Numbers in the string such as the "007" in "James Bond is 007." count as words

    - There will be no double quotes "" within in the string.

- Hints for this problem:

    - Use string methods to filter out characters besides numbers, letters, spaces, apostrophes, and hyphens.

    - Count the number of spaces in the filtered string and add 1 to that since the string will always contain at least 1 word.  This will give you the number of words it contains.

- You should test your program with many different strings. 

- However, the strings that the solution code is being used on are the 3 strings below.

    ```python
    str_1 = "James Bond is 007."
    str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
    str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
    saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
    shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
    shrimp burger, shrimp sandwich. That- that's about it."
    ```

- So, for your final solution, copy the above into your .py file and print() 3 calls of your function, once for each of the 3 variables above.

## Programming Challenge: Word Counter Solution

- See solutions in [07-word-counter.py](./python-projects/07-word-counter.py)

## format()

- The ```.format()``` method is a string method for formatting strings using [format string syntax](https://docs.python.org/3/library/string.html#formatstrings)

    - Example

        ```python
        name = input("What is the applicant's name?\n")
        degree = input("What is the applicant's degree?\n")
        job = input("What is the applicant's current job?\n")
        experience = input("How many years has the applicant been working?\n")

        template_string = "{} majored in {}, works as a {}, \
        and has {} years of experience"

        formatted_string = template_string.format(
          name,
          degree,
          job,
          experience
        )
        ```