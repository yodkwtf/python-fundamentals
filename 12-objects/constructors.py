
#- defining a class
class Point:
  # defining a constructor function
  def __init__(self, x, y): # x and y are constructor parameters
    # setting up pre defined attributes
    self.x = x # self is ref to the current instance of the class
    self.y = y

  def move(self):
    print('move')

  def draw(self):
    print('draw')

#- creating a new object
point = Point(10, 20)
print(point.x)

# attribute values can also be updated later
point.x = 15
print(point.x)