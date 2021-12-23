# first ever program
print('Hello World!!!')

# a list or a tuple
coordinates = [1, 2, 3]

# ❌ product of items w/o destructuring
product1 = coordinates[0] * coordinates[1] * coordinates[2]

# ❌ product of items with destructuring w/o unpacking
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
product2 = a * b * c

# ✅ destructuring using unpacking
x, y, z = coordinates
product3 = x * y * z

print(product1)
print(product2)
print(product3)