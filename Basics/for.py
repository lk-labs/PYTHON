"""break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#continue  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  

#range
for x in range(6):
  print(x)
#range(2,6)
for x in range(2, 6):
  print(x) 
#difference
for x in range(2, 30, 3):
  print(x)
#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")   

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  
"""
#to print square 
for i in range(1,5):
    i=i*i*i
    print(i)