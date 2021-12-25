# function
def greet_user (first_name, last_name):
  print(f'Hi {first_name} {last_name}')
  print('Welcome to the new world!')

# calling with `keyword-arguments`
greet_user(last_name = "Doe", first_name = "John")

## example where keyword arguments would suit best - 
# calc_cost(total_cost = 50, items = 10, discount = 0.1)

# ! In the above example keyword arguments make it very easy to determine what are all these arguments, otherwise it would've been difficult to figure out the diff b/w them