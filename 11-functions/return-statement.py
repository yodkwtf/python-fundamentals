# function to calculate square of a number
def square (number):
  return number * number

# getting and storing the returned value
result = square(6)
print(result)

# printing value directly
print(square(5))

# ! if we remove the `return` keyword from line 3 then line 10 will print `None` since the default return value, i.e., the value returned when there's no return statement in a function is `None`