birthYear = input("Enter birth year ")
# even though we'll enter a number we get a string so we need to convert it into a number

print(type(birthYear))

# 2021 - birthyear => 2021 - '2001'
# 2021 - int(birthyear) => 2021 - 2001
age = 2021 - int(birthYear)

print(age)