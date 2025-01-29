my_list = [10, 25, 3, 85, 5, 54, 11]
print("List the Elements of my_list")
print(my_list)
print("\n")
ascending_order = sorted(my_list)
print("List the elements of my_list in ascending order")
print(ascending_order)
print("\n")
descending_order = sorted(my_list, reverse=True)
print("List the elements of my_list in descending order")
print(descending_order)
print("\n")

sum = sum(my_list)
print("Sum of elements in my_list is")
print(sum)
print("\n")

even_number = []
for n in my_list:
 if n % 2 == 0:
  even_number.append(n)
if even_number:
  print("FOllowing are the even numbers in my_list")
  print(even_number)
else:
  print("No even number in my_list")

