
## function to print age
def printDetails():
  age = 20
  print(age)

# printDetails()
# printDetails()
# printDetails()

## function with arguments
def printName(name):
  print('My name is ' + name)

# printName('Durgesh')

## if-else inside functions 
def printDetails(name, age):
  if age > 25:
    print('Hello', name, 'Your can take part in elections!!') 
  elif age == 25:
    print('Hello', name, 'Only one year more to go!!')
  else:
    print('Hello', name, "You can't take part in elections!")

# printDetails('SRK', 55)
# printDetails('Durgesh', 20)

## returning from function
def calcAge(DOB, currentYear):
  age = currentYear - DOB
  return age 

myAge = calcAge(2001, 2021)

print('Your are', myAge, 'years old.')