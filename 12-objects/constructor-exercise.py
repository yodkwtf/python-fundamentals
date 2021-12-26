
## Create a class called `Person`that should have a `name` attribute and a `talk` method

# class
class Person:
  def __init__(self, name):
      self.name = name

  def talk (self):
    print(f'{self.name} is talking!')

# object
john = Person('John')
print(john.name)
john.talk()

# creating another instacne
mary = Person("Mary")
mary.talk()