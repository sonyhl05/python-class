with open("assignment.py", "r") as fh:
  content = fh.read()
  print(f"{content}")
  fh.close()

with open("1.txt", "w") as fh:
   fh.write("Hi Welcome to devops class")
with open("1.txt", "r") as fh:
  print(fh.read())
print("_______________________")
with open("1.txt", "a") as fh:
   fh.write("\n Hi sony")
with open("1.txt", "r") as fh:
  print(fh.read())
