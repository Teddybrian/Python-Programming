#if else statements
e = int(input("Enter salary: "))
y = int(input("Enter years of service: "))
if y >= 10:
  Bonus = e*0.1
 
if y>=6 and y<=10:
  Bonus = e*0.08
  
else:
  Bonus = e*0.05
  print(Bonus)

