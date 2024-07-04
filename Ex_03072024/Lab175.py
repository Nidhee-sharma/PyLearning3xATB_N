import csv
with open("Td.csv") as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],col[1], sep=" | ")
