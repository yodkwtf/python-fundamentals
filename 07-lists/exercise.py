
## Write a program to remove the duplicates in a list

numbers = [2,5,78,23,2,53,2,78, 2, 23]

# loop over all items
for n in numbers:
  # if item is more than ones
  if numbers.count(n) > 1:
    # remove that one instance of item
    numbers.remove(n)

print(numbers)

# ! There are other ways to do it too.