john_age = 18
voting_age = 18

# if-else statement
# if john_age > voting_age:
#   print('John can vote')
# else:
#   print('John cannot vote')

# if-else with elif statement
if john_age > voting_age:
  print('John can vote')
elif john_age == voting_age:
  print('Depends on the govt.')
else:
  print('John cannot vote')

## CHALLENGE
# A house is for $1M. If customer has good credit, downpayment is only 10%, else it is 20%
is_goodCredit = False

if is_goodCredit:
  print(f'Down payment is ${0.1*1000000}')
else:
  print(f'Down payment is ${0.2*1000000}')
