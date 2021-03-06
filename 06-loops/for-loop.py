# print each charcater in string
for i in "Python":
  print(i)

# print items from a list
fruits = ["apple", "banana", "orange", "mango"]

for fruit in fruits:
  print(fruit)

# print a list of numbers
for i in [45,21,63,14]:
  print(i)

## RANGE FUNCTION
# print 10 numbers
for i in range(10):
  print(i)

# print numbers from 13 to 17
for i in range(13, 18):
  print(i)

# print numbers at a step of 2
for i in range(21, 30, 2):
  print(i)


## EXERCISE
# print total cart price of items in cart with given prices for the items

prices = [10, 20, 30]
total_sum = 0

for price in prices:
  total_sum += price

print(f'The total cart price is {total_sum}')