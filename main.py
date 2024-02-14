import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}

    for id, name, titleProject_id, clas, score in answer:
        if "Меднова Наталья" in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")

        count_class[clas] = count_class.get(clas, 0) + 1
        sum_class[clas] = sum_class.get(clas, 0) + (int(score) if score != "None" else 0)

    for el in answer:
        if el[-1] == "None":
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open("studentsnew.csv", "w", encoding="utf8", newline="") as file:
    w = csv.writer(file)
    w.writerow(["id", "Name", "titleProject_id", "сlass", "score"])
    w.writerows(answer)
