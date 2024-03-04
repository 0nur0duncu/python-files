children = ["a",  "b",  "c"]
children_pets = {
  "a":"cat",
  "b":"dog",
  "c":"bird"
  }

# Good usages
for i in children:
  print(i,end=" ")
  
print()

if "a" in children_pets:
  print("yes")
  
# Bad usages
print()

for i in range(len(children)):
  print(children[i],end= ' ')


if children_pets["a"] != "dog":
  print("no")