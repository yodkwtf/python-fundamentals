# parent class
class Mammal:
  def walk(self):
    print("walk")

# child classes
class Cat(Mammal):
  pass # so our class isn't empty; doesn't do anything

class Dog(Mammal):
  def bark(self):
    print('bark')

# creating objects from child classes
cat = Cat()
cat.walk()

dog = Dog()
dog.walk()
dog.bark()