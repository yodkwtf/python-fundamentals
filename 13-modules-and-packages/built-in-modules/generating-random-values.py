# importing the `random` built-in module
import random

# generate a random value b/w 0-1
print(random.random())

# print 3 random values
for i in range(3):
  print(random.random())

# random value b/w 10-20
for i in range(3):
  print(random.randint(10, 20))

# randomly print an item from a list
kids = ["John", "Mary", "Bob", "Mark"]
leader = random.choice(kids)
print(f'{leader} should be the leader of the group!')