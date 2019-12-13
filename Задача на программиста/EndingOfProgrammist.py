n=int(input())
mod10 = n % 10
mod100 = n % 100

if mod10 == 1 and mod100 != 11:
  print(str(n), 'программист')
elif (mod10 == 2 or mod10 == 3 or mod10 == 4) and mod100 != 12 and mod100 != 13 and mod100 != 14:
  print(str(n), 'программиста')
else:
  print(str(n), 'программистов')