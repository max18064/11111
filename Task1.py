import csv
with open("students.csv",encoding="utf8") as file:
    reader=csv.reader(file,delimitr=",")
    answer=list(reader)[1:]
    count_class = {}
    sum_class = {}