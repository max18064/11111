import csv
reader=[]
with open("students.csv", encoding="utf8") as file:
    for i in file:
        x=i.split(",")
        if x[-1]!="score\n" and x[-1]!="None\n":
            x[-1]=int(x[-1])
        if x[-1]=="None\n":
            x[-1]=0
        if "10" in x[3]:
            reader.append(x)
print(reader)
for i in range(len(reader)):
    for j in range(len(reader)-1):
        if (reader[j][4])<(reader[j+1][4]):
            reader[j], reader[j + 1] = reader[j + 1], reader[j]
с=0
for i in reader:
    print(i)