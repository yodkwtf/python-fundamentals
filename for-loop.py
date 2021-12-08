# for loop
for x in range(5,10): # starting from 5 up to 10
  print(x) # print x

## printing business days from an array of week days
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

for d in days: # for every day from days
  if d== 'Wed':
    continue # skip tuesday
  elif d=='Sat':
    break # stop loop if we hit saturday
  elif d== 'Sun':
    print('Sunday is fun')
  else:
    print(d)