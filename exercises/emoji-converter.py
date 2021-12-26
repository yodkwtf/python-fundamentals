
## Question
# Get a greeting msg from user and print it by replacing the text emojis with actual emojis
# For eg, `Good morning :)` -> `Good morning 😊`

## SOLUTION

# get input from the user
greeting = input("> ")

# split greeting into single words
words = greeting.split(' ')

# dictionary of emojis
emojis = {
  ":)": "😊",
  ":(": "🙁"
} 

# create an empty output variable
output = ''

# loop over words and check if any word matches emoji
for word in words:
  output = output + emojis.get(word, word) + ' ' # for every word, get emoji associated with that word or key & if there isn't, then get the word itself

# print the output
print(output)