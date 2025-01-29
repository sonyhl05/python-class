import json
import requests
import zipfile
import os

# Load the JSON data
with open("1.json", "r") as fh:
    json_data = json.load(fh)

# Define the file path for saving the zip file
file_path = "/home/ubuntu/v1.2.6.zip"

# Loop through the JSON data to download and extract zip files
for ele in json_data:
    source_url = ele["Git Source Url"]
    
    try:
        # Download the zip file
        response = requests.get(source_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Zip file downloaded successfully from {source_url}.")
        
        # Extract the contents of the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall('/home/ubuntu')
        print(f"Zip file extracted to /home/ubuntu.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file from {source_url}: {e}")
    except zipfile.BadZipFile as e:
        print(f"Error extracting the zip file {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
