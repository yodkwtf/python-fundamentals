'''
matrix in maths
[
  1,2,3,
  4,5,6,
  7,8,9
]
'''
## 2-D List

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
] 

# accessing single list using index
print(matrix[2])

# accessing single item using index
print(matrix[1][2])

# modifying items using indexes
matrix[0][1] = 22
print(matrix)

## nested loops to print every item one by one
# loop over every row in matrix
for row in matrix:
  # loop over every item in that row
  for item in row:
    print(item)