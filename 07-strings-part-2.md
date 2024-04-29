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

- The ```.rjust()``` method

- The ```.ljust()``` method

- The ```.center()``` method

- The ```.strip()``` method

- The ```.rstrip()``` method

- The ```.lstrip()``` method

- The ```.replace()``` method

## String Methods 2 Exercises

## String Methods 2 Exercises Solutions

- See solutions in [07-string-methods-2.py](./python-projects/07-string-methods-2.py)

## len()

- The ```.len()``` method

## Programming Challenge: String Reverser

## Programming Challenge: String Reverser Solution

- See solutions in [07-string-reverser.py](./python-projects/07-string-reverser.py)

## Programming Challenge: Word Counter

## Programming Challenge: Word Counter Solution

- See solutions in [07-word-counter.py](./python-projects/07-word-counter.py)

## format()

- The ```.format()``` method