import random
print("DICE ROLLER \n ")
while True:
  print("To roll the dice type r")
  a=(input())
  if a=='r':
      droll=random.randint(1,6)
      print("You got ",droll)
  else:
    break
        
