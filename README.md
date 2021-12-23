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

- Get an IDE like VS Code for your system
- Open vscode and configure it to look pretty
- Get the `python` extension by microsoft
- Select the python intrepreter using command palette and set it as downloaded python version
- Open the python file and run it using play btn
- Code will be executed!

## Python Notes

Print your first ever python program

```bash
# first ever program
print('Hello World!!!')
```

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

#### Math Functions

- Several functions/methods to handle calculations
- A few built in functions like `round(n)` and `abs(n)`
- Import the `math` module and use its methods for complex stuff
- Math module has methods like `math.ceil(n)` and `math.floor(n)`
- Google _python <version> math modules_ to learn more methods
- Refer to [math-functions.py](./01-basics/math-functions.py)

#### Input

- Used to get input from the user in terminal
- Used as `input(<'Input details or question'>)`
- Input can pe stored in a variable
- Input function always returns a string even if user enters a number
- Refer to [input.py](./01-basics/input.py)

#### Data Types

- There are multiple data types in python
- `str` represents strings - any text or characters
- `int` is for integers like 4, 7, 27328
- `float` is for numbers with decimals like 3.2, 7839.83
- `bool` is for True/False (case sensitive)
- 'type(name)` - used to find the data type of a variable
- One type can be converted to another via [type conversion](./02-data-types/type-conversion.py)
- Refer to [data-types.py](./02-data-types/data-types.py)

#### Strings

- Wrap text bw single or double quotes `print("Hello")`
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

#### If-Else Statements

- Used to run programs based on conditions
- Used a lot with comparison operators and boolean values
- If a condition is met, the program runs and discards the rest of the conditions
- Starts with `if (condition)` and continues till the last `else` statement
- `elif` statements are used to created [nested if-else](./05-conditionals/nested-if-else.py) conditions
- Refer to [if-else.py](./05-conditionals/if-else.py)

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

#### Lists

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

#### Tuples

- Used to store a collection of items just like lists
- Defined using _parenthesis_ - `('John', 'Peter', 'Josh')`
- Immutable - items can't be added or removed
- Single items can be accessed using indexes
- Since they're immutable, there aren't a lot of methods for tuples unlike lists
- `count()` and `index()` can be used to get count and index of the specified item

#### Functions

- Block of code with a name that can be executed when called
- Makes code more reusable
- Can be built-in `print()` or can be created by us
- Created by using the **def** keyword followed by function name and parenthesis
- Cannot be called before defining it
- Can take arguments as function parameters
- If-else statements can be used inside functions
- Values can also be returned from function after executions
- Refer to [functions.py](./functions.py)

#### Importing Libraries and Modules

- Can be imported to built stuff on top of pre existing code
- Use `import` keyword followed by the library name
- Use the methods on the imported library or however the respective module works
- Refer to [libraries.py](./libraries.py)

## Exercises

1. [Weight Converter Program](./exercises/weight-converter.py)
2. [Guessing Game](./exercises/guessing-game.py)
3. [Car Game](./exercises/car-game.py)
