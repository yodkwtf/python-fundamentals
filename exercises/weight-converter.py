
## Question
# Ask the user their weight
# Ask them if given weight is in pounds or kilos
# Convert the unit from one to another
# Print the full msg  
# - 1KG = 2.20462 LBS 

## SOLUTION

# get the user's weight
weight = float(input("What is your weight? ")) 

# ask the unit from the user
unit = input("Please specify b/w (K)ilograms or (L)bs... ").lower()

# convert and print the weights
if unit == 'k':
  converted_weight = weight * 2.20462
  print(f'Your weight is {converted_weight} lbs.')
elif unit == 'p':
  converted_weight = weight / 2.20462
  print(f'Your weight is {converted_weight} kgs.')
else:
  print("Please enter K for kgs or P for pounds")
