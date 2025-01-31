import re

email_data="sonyhl97 <sonyhennaly123@gmail.com>, teja <teja@gmail.com>"

result= re.search(r"so", email_data)
print(result)


result= re.findall(r"so", email_data)
print(result)

result= re.search(r"so[o,n]", email_data)
print(result)

result= re.search(r"so[a-z]{2}", email_data)
print(result)

result= re.findall(r"so[a-z]+", email_data)
print(result)

result= re.findall(r"so[a-z,A-Z,0-9]+", email_data)
print(result)

# to search email-ID
result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)


result= re.search(r"so[a-zA-Z0-9@.]+", email_data)
print(result[0])

result= re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
