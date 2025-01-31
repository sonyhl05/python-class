import os
for test, dir, files in os.walk("/home/sony/git/Parcel-service"):
  for file in files:
    if file.startswith("LI"):
      print(test,file)
    if file.startswith("NO"):
      print(test,file)
