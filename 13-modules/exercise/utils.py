# module for a bunch of utility functions

# Function to find the largets num from a list
def find_max(list):
  max = list[0]

  for item in list:
    if item > max:
      max = item

  return max