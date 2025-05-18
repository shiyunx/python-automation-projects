# Read txt file
file_link = "/Users/Username/Desktop/text.txt"

try:
    with open(file_link, "r") as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print("Error, file not found!")