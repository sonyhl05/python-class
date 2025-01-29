import json
import sys
import requests
import tarfile

with open("1.json", "r") as fh:
  json_data=json.load(fh)
 # print(json_data)

file_path="/home/ubuntu/behave.tar.gz"
for ele in json_data:
#    print(ele)
#   for key, value in ele.items():
  source_url=ele["Source URL"]
  response = requests.get(source_url)
  #response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
  with open(file_path, 'wb') as file:
      file.write(response.content)
  print("Tar file downloaded successfully.")
  break

file = tarfile.open('/home/ubuntu/behave.tar.gz')
file.extractall('/home/ubuntu')
 # print(ele["Source URL"])
    # print(key)
    # print(value)
#  print("__________________________")
  #sys.exit()
