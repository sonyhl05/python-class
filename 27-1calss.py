class example:
   def __init__(self, str1, str2):
       self.name1=str1
       self.name2=str2
       self.name3="devops"
#   def __init__(self, str1, str2):
#       self.name=str1
   def print_value(self):
      print(self.name1, self.name2, self.name3)
   def display_value(self,str2):
      print(self.name1, str2)

var = example("Hello", "welcome")
var.print_value()
var.display_value("cloud")
var1 = example("sony", "sonyhl")
var1.print_value()
var.print_value()
