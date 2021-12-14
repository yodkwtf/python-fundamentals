# any text or character
text = "Hello World"

# when use single quotes
a = "This is John's number"

# double quotes when?
b = 'I like the movie "Batman"'

# multi line strings
msg = '''
Hello

This is your email msg
'''

# get character at certain index
print(text[2]) # will return `l` from `Hello World`

# get charcaters starting from one index to another
print(text[0:5]) # up to the last one (not including) 

# using above method and the default values of indices to create a new variable
new_var = text[6:] # starting from W till end
print(new_var)

# guess the answer
name = 'Elephant'
print(name[1:-1]) # should return `lephan`


