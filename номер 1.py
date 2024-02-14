import csv
with open("students.csv",encoding="utf8") as file:
    reader=csv.reader(file,delimiter=",")
    answer=list(reader)[1:]

    sumclass={}
    countclass={}

    for id, Name , titleProject_id,clas,score in answer:
        if "Меднова Наталья " in Name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
        sumclass[clas] = sumclass.get(clas, 0) + int(score if score != "None" else 0)
        countclass[clas] = countclass.get(clas, 0) + 1
    for el in  answer:
        if el[-1] =="None":
            el[-1]=round(sumclass[el[-2]]/countclass[el[-2]],3)

    with open("studentsnew2222222.csv","w",encoding="utf8",newline="") as  file:
        w=csv.writer(file)
        w.writerow(["id","Name","titleProject_id","class","score"])
        w.writerows(answer)


