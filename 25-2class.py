def display_content(filename):
    with open(filename, "r") as fh:
       print(fh.read())
    return filename, ab, num

file_name = "1.txt"
var, var1, var2 = display_content(file_name)
