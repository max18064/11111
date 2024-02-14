import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}
id1=input()
while id1 !="СТОП":
    for id, name, titleProject_id, clas, score in answer:
        if id1 == titleProject_id:
            a,b,c=name.split(" ")
    print(f'Проект N {id1} делал {a,b}')
    id1 = input()

