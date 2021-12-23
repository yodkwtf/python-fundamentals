
## QUESTION
# Get the phone number in digits as an input and print it out as words...
# For eg, if someone enters `123`, print `One Two Three`

## SOLUTION

# -1 create a dictionary
digits = {
  "0": "Zero",
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine",
} 

# -2 get user's number
number = input("Phone: ")

# -3 create an empty variable for output
output = ''

# -4 loop over number
for i in number:
  output += f'{digits[i]} '

# -5 print the output
print(output)
