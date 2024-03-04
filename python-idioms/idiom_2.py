state = True
n_child = 3
c_names = ["a", "b", "c"]
c_pets = {"a":"cat","b":"dog","c":"bird"}

# best usage
if state and n_child and c_names and c_pets:
  print("GOOD")

# bad usage
if state == True and n_child >0 and len(c_names)>0 and c_pets != {}:
  print("BAD")
  
