import csv
def hash(s):
    alp="абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    d={l: i for i, l in enumerate(alp,1)}
    p=67
    hash=0
    m=10**9+9
    d={l:i for i , l in enumerate(alp,1)}
    for i in range(0,len(s)):

        hash=hash+(d[s[i]] * p**i)%m
    return str(hash)

print(hash("Сербин Геннадий Михаилович"))


reader=[]
with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)[1:]
    for el in answer:
        el[0] = hash(el[1])
with open("studentsnewww.csv", "w", encoding="utf8", newline="") as file:
    w = csv.writer(file)
    w.writerow(["id", "Name", "titleProject_id", "сlass", "score"])
    w.writerows(answer)