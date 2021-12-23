# a list
numbers = [1, 1, 2, 3, 4]

# converting list to set -> removes duplicate values
unique = set(numbers)

print(numbers)
print(unique)

# creating a set from scratch
second = {1, 4, 5}

# add an item 
second.add(7)
print(second)

# remove an item
second.remove(4)
print(second)

# check if an item is in set
print(1 in second)
print(2 in second)

# get the length of set
print(len(unique))