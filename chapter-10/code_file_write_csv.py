import csv

with open(file="test_csv_write.csv", mode="a", encoding="utf-8") as f:
    cf = csv.writer(f)
    cf.writerows([['name', 'subject', 'score'], ['lee', 'c', 99]])
