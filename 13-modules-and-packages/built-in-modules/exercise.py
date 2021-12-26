
## Question
# Create a class called `Dice` that has a method `roll()` which rolls 2 dice and returns a tuple with 2 random results 

## Solution

import random

class Dice:
  def roll(self):
    return (random.randint(1, 6), random.randint(1, 6))

die = Dice()
die_outcome = die.roll()
print(die_outcome)