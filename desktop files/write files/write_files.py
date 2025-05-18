# Import file
import csv

# Field names
scores = [["Name", "Score"],
        ["student a", 80],
        ["student b", 90],
        ["student c", 10]]

# Csv file link
file_link = "/Users/Username/Desktop/scores.csv"

try:
    # Write to existing csv file
    with open(file_link, "w") as file:
        # Create a csv writer object
        writer = csv.writer(file)
        for row in scores:
            # Write to data rows
            writer.writerow(row)
        print(f"csv file {file_link} created")
except FileExistsError:
    print("Error, file exists!")