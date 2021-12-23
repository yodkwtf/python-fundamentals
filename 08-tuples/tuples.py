# defined using `()`
numbers = (1, 2, 3, 4, 1)

## tuple methods
# count no. of instances
print(numbers.count(1))

# find index of an item
print(numbers.index(2))

## index based
print(numbers[3]) 

#! tuples can't be mutated 
numbers[2] = 10 # will throw an error
