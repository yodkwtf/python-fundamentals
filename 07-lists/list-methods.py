numbers = [2,4,5,9,7]

# add a new item to the end of the list
numbers.append(11)
print(numbers)

# add an item in b/w other items using index
numbers.insert(1,33) 
print(numbers)

# remove an item
numbers.remove(9)
print(numbers)

# remove an item from end
numbers.pop()
print(numbers)

# find if an item is in the list -> returns the index where the item first appeared and error if it isn't there
print(numbers.index(4)) 

# check if an item is in the list -> true/false
print(8 in numbers)
print(4 in numbers)

# count the frequency of an item in the list
print(numbers.count(33))

# sort the list
numbers.sort()
print(numbers)

# reverse the list direction
numbers.reverse()
print(numbers)

# create a copy of the the list
numbers2 = numbers.copy()
# ! if we change anything in the first list it doesn't affect the second copy
numbers.append(545)
print(f'Original - {numbers}')
print(f'Copy - {numbers2}')

# remove all items from list
numbers.clear()
print(numbers)
