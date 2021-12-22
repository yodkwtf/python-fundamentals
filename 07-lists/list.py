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