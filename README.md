# Python Fundamentals

A playground to learn basics of python with small programs and my personal docs based on those programmes.

## Why learn Python?

- One of the most popular
- Been around a while, hence reliable
- Beginner friendly and easy to learn
- Can do all sorts of things like AI & ML, game or web dev, data science, automation, etc.
- Fundamentals are useful for all other languages too

## Getting Python

- Go to [www.python.org](https://www.python.org/)
- Click the download btn and choose the best option for your system
- Install python and check the `python path` checkbox during the process
- Installed! 🚀

> To check if you have python, open a terminal like cmd and type `python --version`. If you have python in your system it will show the version or else you don't have it

## Python Environment

- Open python from start menu in the default command line app
- Write your first `hello world` program
- Use `exit()` function to exit and close the program

#### Notepad

- We can also use notepad and other text editors for writing python code
- Simple open notepad and write some python code
- Save the file with `.py` extension which stands for python
- Open terminal and type `python <saved file's full path>`
- Code will be executed!

#### IDEs

- Get an IDE like [VS Code](https://code.visualstudio.com/) for your system
- Open vscode and configure it to look pretty
- Get the [python extension by microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Select the python intrepreter using command palette and set it as downloaded python version
- Open the python file and run it using play btn
- Code will be executed!

> We can use any one of the several IDE's available online to run python code like PyCharm, Jupyter Notebook, etc.

# Notes

Print your first ever python program

```bash
# first ever program
print('Hello World!!!')
```

## 1. Python Basics

#### Comments

- Used to explain code as python ignores it
- Use `#` symbol for single line comment
- For multi-line comments wrap it inside `''' comment '''`
- Can be put above or right next to any code
- Can be used for line by line debugging
- Refer to [comments.py](./01-basics/comments.py)

#### Variables

- Used to assign and store values
- Can be used to store different data types
- Should only contain letters, numbers, and underscores
- Shouldn't start w number
- Case sensitive and can't be python keywords
- Can be reset later after defining
- Refer to [variables.py](./01-basics/variables.py)

#### Input Function

- Used to get input from the user in terminal
- Used as `input(<'Input details or question'>)`
- Input can pe stored in a variable
- Input function always returns a string even if user enters a number
- Refer to [input.py](./01-basics/input.py)

#### Math Functions

- Several functions/methods to handle calculations
- A few built in functions like `round(n)` and `abs(n)`
- Import the `math` module and use its methods for complex stuff
- Math module has methods like `math.ceil(n)` and `math.floor(n)`
- Google _python <version> math modules_ to learn more methods
- Refer to [math-functions.py](./01-basics/math-functions.py)

## 2. Data Types in Python

#### Data Types

- There are multiple data types in python
- `str` represents strings - any text or characters
- `int` is for integers like 4, 7, 27328
- `float` is for numbers with decimals like 3.2, 7839.83
- `bool` is for True/False (case sensitive)
- `type(name)` - used to find the data type of a variable
- Refer to [data-types.py](./02-data-types/data-types.py)

#### Type Conversion

- One data type can be converted into another
- Built-in functions like `str()`, `int()` can be used for this
- `int('birthday')` - converts the string into integer
- Refer to [type-conversion.py](./02-data-types/type-conversion.py)

## 3. Strings and String Methods

#### Basics of Strings

- Wrap text b/w single or double quotes - `print("Hello")`
- Numbers can also be used as strings `print('5')`
- Use quotes carefully and when required `print("Give me John's number")`
- For multiline strings use the quotes 3 times
- Use [formatted strings](./03-strings/formatted-strings.py) for easy string concatenation
- Refer to [strings.py](./03-strings/strings.py)

#### String Methods

- Used to handle and do more things with strings
- `len(name)` used to find the length of a string
- `name.upper()` - to convert string to uppercase
- `name.lower()` - to convert string to lowercase
- `name.find()` - to find the index of characters
- `name.replace()` - to replace one char to another
- `'...' in name` - to check existence of a char in variable
- Refer to [string-methods.py](./03-strings/string-methods.py)

## 4. Operators and Types of Operators

#### Arithmetic Operators

- Adding(+), subtract(-), multiple(\*), divide (/)
- White spaces are ignored
- Follows default mathematical BODMAS rule `2+2*5 = 12`
- Don't use commas in bw numbers
- `x*=5 => x = x * 5` - called **augmented assignment operator**
- Refer to [arithmetic-operators.py](./04-operators/arithmetic-operators.py)

#### Logical Operators

- Used to combine multiple conditions
- Used for with if-else statements a lot
- `and` - both condition is true
- `or` - any one condition is true
- `not` - reverts the boolean value next to it
- Refer to [logical-operators.py](./04-operators/logical-operators.py)

#### Comparison Operators

- Used to compare 2 values (a variable with a value)
- Operators are almost like math
- `>`, `<`, `==`- used to compare which value is **greater**, **lesser**, or **equal**
- `>=` and `<=` - checks the condition **greater than or equal to** and **less than or equal to**
- Refer to [comparison-operators.py](./04-operators/comparison-operators.py)

## 5. If-Else Statements

- Used to run programs based on conditions
- Used a lot with comparison operators and boolean values
- If a condition is met, the program runs and discards the rest of the conditions
- Starts with `if (condition)` and continues till the last `else` statement
- `elif` statements are used to created [nested if-else](./05-conditionals/nested-if-else.py) conditions
- Refer to [if-else.py](./05-conditionals/if-else.py)

## 6. Loops in Python

#### While Loops

- Used to execute a block of code multiple times
- Code block keep reiterating as long as the condition given is true
- Can use used to create patterns and small games
- `else` can be used with while loops
- Refer to [while-loops.py](./06-loops/while-loop.py)

#### For Loops

- Used to iterate over a collection - For eg, each character of a string
- In each iteration, loop variable holds one character value at a time
- `for i in 'Python'` - Here `i` is the loop variable and `Python` is iterable string
- Built-in `range()` func is used to loop over a range of numbers
- `range()` func can take arguments in multiple ways
- Refer to [for-loops.py](./06-loops/for-loop.py)

#### Nested Loops

- One loop can be nested inside another loop
- Used to create complex programs like getting graph coordinates
- Can be used to create various patterns or complex programs
- Use [break and continue statements](./06-loops/continue-break-statements.py) for further control of loops
  - `break` - stop and exit the loop
  - `continue` - skip over current iteration
- Refer to [nested-loops.py](./06-loops/nested-loops.py)

## 7. Lists and List Methods

#### Basics of Lists

- Used to store a collection of values of different data types
- Items are put inside the square brackets `['John', 'Peter', 'Josh']`
- Single items can be accessed using their index
- We can also get a range of items using index - `names[2:4]`
- Range doesn't modify the list, they return a new list
- List items can also be updated using their index
- Refer to [lists.py](./07-lists/list.py)

#### 2-D Lists

- Used to create a maths like matrix by nesting multiple lists inside a parent list
- Used a lot in data science and ML
- Each child list represents one row of the parent matrix
- Individual items can be referenced using 2 brackets indexes
- Items can also be modified using the same way `items[2][1]`
- Refer to [2D-lists.py](./07-lists/2D-lists.py)

#### List Methods

- Built-in functions/operations for lists
- `sort()` - to sort the list in ascending order
- `reverse()` - to reverse direction of the list
- `append(n)` - to add n to the end of the list
- `remove(n)` - to remove n from the list
- `list.copy()` - to create a copy of the list that doesn't get affected when the original list is manipulated
- Refer to [list-methods.py](./07-lists/list-methods.py) for more

## 8. Tuples in Python

- Used to store a collection of items just like lists
- Defined using _parenthesis_ - `('John', 'Peter', 'Josh')`
- Immutable - items can't be added or removed
- Single items can be accessed using indexes
- Since they're immutable, there aren't a lot of methods for tuples unlike lists
- `count()` and `index()` can be used to get count and index of the specified item
- Refer to [tuples.py](./08-tuples/tuples.py)

## Bonus - Unpacking in Python

- Used to destructure list/tuple items into separate individual variables
- Makes it easy to access single items when they are being repeated many times

```bash
# a list or a tuple
coordinates = [1, 2, 3]

# ❌ product of items w/o destructuring
product1 = coordinates[0] * coordinates[1] * coordinates[2]

# ❌ product of items with destructuring w/o unpacking
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
product2 = a * b * c

# ✅ destructuring using unpacking
x, y, z = coordinates
product3 = x * y * z

# All 3 products will return the same value but it can easily be observed that the 3rd way makes things much more simple than the other two.

```

## 9. Sets in Python

#### Basics of Sets

- Set is a collection of items with no duplicates
- Defined by curly braces - `{1, 2, 3}`
- A list can be converted into set using **set** function
- Sets are unordered so items cannot be accessed using indexes
- Has several built-in methods like `add()`, `remove()`, `len()`, etc.
- Refer to [sets.py](./09-sets/sets.py)

#### Mathematical Operations on Sets

- Sets support powerful mathematical operations
- `set1 | set2` - returns union of 2 sets
- `set1 & set2` - returns intersection of 2 sets
- `set1 - set2` - returns difference b/w 2 sets
- `set1 ^ set2` - returns symmetric difference b/w 2 sets
- Refer to [mathematical-operations.py](./09-sets/mathematical-operations.py)

## 10. Dictionaries in Python

- Used to store a collection of key-value pairs
- Every key must be unique
- Values can be accessed using the `[]` brackets to target specific keys
- Items can also be modified the same way
- New key value pairs can also be added later using `[]` brackets
- Refer to [dictionary.py](./10-dictionaries/dictionary.py)

## 11. Functions in Python

#### Basics of Functions

- Block of code that performs a specific task when called and executed
- Makes code more reusable and well designed
- Can be built-in like `print()` or can be manually created
- Created by using the **def** keyword followed by function name and parenthesis
- Cannot be called before defining it
- Can be called as many as required
- Refer to [functions.py](./11-functions/functions.py)

#### Parameters and Arguments

- **Parameters** act as placeholders for info passed to the functions
- **Arguments** are actual information passed into the function when called
- Make functions more dynamic
- We can also have multiple parameters for a single function
- Order/Position of the argument matters
- Refer to [parameters-arguments.py](./11-functions/parameters.py)

#### Keyword Arguments

- Order of the arguments doesn't matter when using keyword argument
- Are used to improve the readability of the code
- Used by writing parameter name followed by the argument value when calling a function
- Must come after the positional arguments if we have both
- Refer to [keyword-arguments.py](./11-functions/keyword-arguments.py)

#### Return Statement

- Functions can also return values using return statement
- Useful when performing calculations inside functions
- By default, all functions return the value **None**
- Refer to [return-statement.py](./11-functions/return-statement.py)

## Bonus - Try and Except

- Used to handle errors in python programs
- Main code is written under try block and except block customizes the results based on the type of the error

```bash
# normal code
try:
  age = int(input('Age: '))
  print(age)
# code when there's a value error
except ValueError:
  print('Please provide a number...')
```

- We can have multiple exceptions (except blocks) to handle different kinds of errors

# Exercises

1. [Weight Converter Program](./exercises/weight-converter.py)
2. [Guessing Game](./exercises/guessing-game.py)
3. [Car Game](./exercises/car-game.py)
4. [Emoji Converter](./exercises/emoji-converter.py)
