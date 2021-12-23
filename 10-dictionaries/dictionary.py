# define a dictionary
customer =  {
  "name": "John Doe",
  "age": 30,
  "isVerified": False
}

# accessing keys
print(customer["name"])

# updating key's value using key
customer["name"] = "Hardy"
print(customer)

# add a new key-value pair
customer["birthday"] = "Aug 4, 2000"
print(customer)

# using get method to avoid the error below
print(customer.get("lastname"))

# get method with a default value
print(customer.get("lastname", "Kumar"))

#! accessing a key that doesn't exist -> throws an error
print(customer["lastname"])
