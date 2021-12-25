
## Convert the emoji converter program into a reusable function block

# function that converts emoji
def convert_emoji(msg):
  words = msg.split(' ')
  emojis = {
    ":)": "😊",
    ":(": "🙁"
  }
  output = ""
  for word in words:
    output = output + emojis.get(word, word) + " "

  return output

# get input from user
message = input('> ')

# call func to convert msg to emoji and get returned result
result = convert_emoji(message)
print(result)
