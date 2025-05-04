# what is a for loop?

for x in range(5):
    print(x)

print("---------------------------------------------")

values = [23, 52, 59, 37, 48]
sum = 0
length = 0

for value in values:
  sum += value
  length += 1

print("total sum: " + str(sum) + " - average: " + str(sum/length))

print("---------------------------------------------")

# more for loop examples

product = 1
for n in range(1,10):
   product = product * n 

print( product)

print("---------------------------------------------")

def to_celsius(x):
   return (x-32) * 5/9

for x in range(0, 101,25):
   print(x, to_celsius(x))

print("---------------------------------------------")

# R: a closer look at the range() function

for n in range(10, 0, -2):
   print(x)

print("---------------------------------------------")

for number in range(2,7+1):
    print(number*3)

print("---------------------------------------------")

# nested for loops

for left in range(7):
   for right in range(left, 7):
      print("[" + str(left) + "|" + str(right) + "]", end=" ")

print("---------------------------------------------")

teams = ['dragons', 'wolves', 'pandas', 'unicorns']
for home_team in teams:
   for away_team in teams:
      if home_team != away_team:
         print(home_team + " vs " + away_team)

print("---------------------------------------------")

# common errors in for loops

for x in [25]:
   print(x)

print("---------------------------------------------")

def greet_friends(friends):
   for friend in friends:
      print("Hi " + friend)

greet_friends(['tylor', 'luisa', 'jamaal', 'eli'])

print("---------------------------------------------")







  