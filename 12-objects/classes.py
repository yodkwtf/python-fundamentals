# defining a class
class Point:
  def move(self):
    print('move')

  def draw(self):
    print('draw')

# creating an instance of the class -> an Object
point1 = Point()

# accessing methods on the object
point1.move()

# setting new attributes to the object
point1.x = 10
point1.y = 20
print(point1.x)
