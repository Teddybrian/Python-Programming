#voting

age=int(input("enter your age:"))
citizenship=str(input("enter your citizenship:"))
if age>= 18 and citizenship=="Kenyan" or "kenyan":
  print ("viable to vote")
else:
  print("cannot vote")