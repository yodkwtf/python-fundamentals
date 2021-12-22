# list
names = ['John', 'Peter', 'Susan', 'Josh', 'Brad']
print(names)

#- accessing single items using index
print(names[1])
print(names[-1]) # prints first item from end

#- accessing a range of items
print(names[3:]) # prints all items from index 3 to end
print(names[1:4]) # prints items from first range up to the 2nd

# updating list item using index
names[0] = 'Jon'
print(names)

## EXERCISE
# write a program to find the largest no. in a list

numbers = [1, 9, 2, 76, 4, 7, 45, -55, 3, 6, 8, 5]
largest_num = numbers[0] # assume

for n in numbers:
  if n > largest_num: # if current no. is bigger replace max variable
    largest_num = n
  
print(largest_num)