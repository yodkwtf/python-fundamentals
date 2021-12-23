numbers = (1, 2, 1, 3, 4)

first = set(numbers)
second = {1, 5}

# union of 2 set
print(first | second)

# intersection of 2 set
print(first & second)

# difference b/w 2 sets
print(first - second)
print(second - first)

# symmetric difference -> returns `union - intersection`
print(first ^ second)