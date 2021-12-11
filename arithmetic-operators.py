# add
print(2+5)

# subtract
print(10-6)

# multiply
print(2*4)

# divide
print(10/3) # returns float
print(10//3) # returns integer

# modulus or remainder
print(12%5)

# exponent or power
print(2**5)

# augmented assignment operator
x = 5
x += 7 # x+= 7 => x = x + 7
print(x)

y = 2
y *= 3 # y *= 3 => y = y * 3
print(y)

# follows precedence rule (BODMAS rule)
z = 12 + 4 * 3 ** (2 + 1) 
# z = 12 + 4 * 3 ** 3
# z = 12 + 4 * 27
# z = 12 + 108
# z = 120
print(z)