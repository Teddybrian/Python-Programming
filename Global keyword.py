# This function modifies global variable 's'
def f():
  global s
  print (s)
  s = "Look for Geeksforgeeks python section"
  print (s)
  global c
  c = "Teddy"
  print(c)

#Global Scope
s = "Pythom is great"
f()
print(c)
print(s)