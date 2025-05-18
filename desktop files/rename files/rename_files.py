import os

os.chdir('/Users/username/Desktop/docs')

# List of files
# print(os.listdir())

# Print list of files
for file in os.listdir():
    print(file)

    filename, ext = os.path.splitext(file)
    splitted = filename.split("_")
    new_filename = f"{splitted[1]}_{splitted[0]}"
    print(splitted)
    print(new_filename)



