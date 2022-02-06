#Comparing heights of students
Student1=(input("Enter student Name: "))
H1=(input("Enter student Height: "))
Student2=(input("Enter student Name: "))
H2=(input("Enter student Height: "))
Student3=(input("Enter student Name: "))
H3=(input("Enter student Height: "))

print(Student1,":", H1)
print(Student2,":", H2)
print(Student3,":", H3)

if H1>H2 and H1>H3:
  print (Student1, "is the tallest")
if H2>H1 and H2>H3:
  print (Student2, "is the tallest")
else:
  print(Student3, "is the tallest")
  