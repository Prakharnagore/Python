# CSV - Comma Separated Values
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 100])
    writer.writerow([1001, 2, 200])
    writer.writerow([1002, 3, 300])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader)) - [['transaction_id', 'product_id', 'price'], [1000, 1, 100], [1001, 2, 200], [1002, 3, 300]]
    for row in reader:
        print(row)
