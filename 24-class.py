import os
for test, dir, files in os.walk("/opt"):
  for file in files:
    if file.endswith(".txt"):
      print(test,file)
