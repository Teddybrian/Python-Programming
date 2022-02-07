#if elif statements
s1=int(input("Enter maths score: "))
s2=int(input("Enter english score: "))
s3=int(input("Enter computer score: "))
s4=int(input("Enter chemistry score: "))
s5=int(input("Enter geography score: "))

score = (s1+s2+s3+s4+s5)/5
print("\nScore:",score)

if score>=70 and score<=100:
  print("Grade A")
elif score>=60 and score<70:
  print("Grade B")
elif score>=50 and score<60:
  print("Grade C")
elif score>=40 and score<50:
  print("Grade D")
elif score>=0 and score<40:
  print("Fail")
else:
  print("Invalid score")

