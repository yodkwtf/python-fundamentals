'''
`>` check if one is greater than the other
`<` check if one is lesser than the other
`==` check if both the values are equal
`>=` checks for greater than or equal to
`<=` checks for lesser than or equal to
'''

## Question
# Get someone's name and based on length of name, show msgs like name is too short or too long 

name = input('Enter your name... ') 

name_length = len(name)

if name_length < 3:
  print("Name can't be less than 3 char")
elif name_length >= 10:
  print("Name can't be greater than or equal to 10 char")
else:
  print(name)