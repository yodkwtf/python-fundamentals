
## Question
# Print out things based on the commands enter by the user
# `help` - shows a list of possible commands
# `start` and `stop` - to start or stop the car
# `quit` - quits the game and end the program
#  `random commands` -  says "I don't understand the command"

## SOLUTION


help_msg = """
 start - to start the car
 stop - to stop the car
 exit - to exit the program
"""
start_msg = "Car started...Let's go!!!"
stop_msg = "Car stopped."
error_msg = "Sorry, I don't understand..."

while 2 > 1:
  command = input('>').lower()

  if command == 'help':
    print(help_msg)
  elif command == 'start':
    print(start_msg)
  elif command == 'stop':
    print(stop_msg)
  elif command == 'quit':
    break
  else:
    print(error_msg)

