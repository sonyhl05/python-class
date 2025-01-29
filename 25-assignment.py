import os

output_file = "1.txt"

with open(output_file, "w") as f:
    f.write("")

for root, dirs, files in os.walk("/home/ubuntu/"):
    for file in files:
        if file.startswith("LICENSE"):
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")

            with open(file_path, "r") as fh:
                content = fh.read()

                print(f"Content of {file_path}:\n{content}\n")

                with open(output_file, "a") as output:
                    output.write(f"--- {file_path} ---\n")
                    output.write(content)

print(f"All LICENSE files have been aggregated into {output_file}.")


