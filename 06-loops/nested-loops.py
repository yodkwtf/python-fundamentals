# print coordinates
for x in range(4): # runs 4 times (0-3)
  for y in range(3): # runs 3 times (0-2) in each iteration of x
    print(f'({x},{y})')

## EXERCISE
# print an F pattern using x's and nested loops

numbers = [6, 2, 5, 2, 2]

#- using one loop
# for n in numbers:
#   print(n * 'x')

#- using nested loop
for digit in numbers: # run this 5 times (for each num list)
  line = '' # initialize an empty var

  for x in range(digit): # run this as many times as digit
    line += 'x' # add an x to var each iteration

  print(line) # print the output var for each iteration


## PRINTING AN 'L' THE SAME WAY

items = [1, 1, 1, 1, 6]

for i in items: # iterates 5 times
  line = ''
  for x in range(i): # iterates 1,1,1,1,6 times resp. for each i
    line += '*'
  print(line)