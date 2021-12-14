'''
and - both conditions are true
or - any one condition is true
not - revert the boolean value of condition
'''

## ELIGIBLE FOR LOAN OR NOT
has_goodCredit = True
has_criminalRecord = True
has_security = False 

# and
if has_goodCredit and has_security:
  print('Eligible')
# not
elif has_goodCredit and not has_criminalRecord:
  print('Eligible because good person')
# or
elif has_goodCredit or has_security:
  print('Has one thing right')
else:
  print('Will discuss')
