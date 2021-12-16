
## Question
# Store a secret number in a variable (1-10)
# Ask the user to guess the number in 3 guess.
# Print the message appropriately 

## SOLUTION
secret_num = 7
guess_left = 3

while guess_left > 0:
  # get the num
  guess = int(input("Guess the number? "))

  # check if user won
  if guess == secret_num:
    print('Correct guess!')
    break

  # if user didn't win
  else:
    # reduce guesses left by 1
    guess_left-=1

    # if no chances left, print game over
    if guess_left == 0:
      print('No guesses left!')
      break
    
    # show chances left and re-iterate
    print(f'{guess_left} chances left...')
