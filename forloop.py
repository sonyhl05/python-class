my_list = ["sony", "bangalore", "4", "6"]
my_dict = {
 "Name": "sony",
 "Place": "Sakleshpur",
 "Age": 27
}

if "sony" in my_list:
 print("Element found in the list")
else:
 print("Element not found in the list")

my_list1 = []

if not my_list1:
  print("List is empty")
else:
  print("List is not empty")

if "Name" in my_dict:
 print("key Name is present")
else:
 print("Key name not present")

if "test" in my_dict:
 print("value test is present")
else:
 print("Not present")

if my_dict["Name"] == "sony":
 print("Key contain same value")
else:
 print("Key contain different value")
