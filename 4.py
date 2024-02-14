import csv
import random
reader=[]
with open("students.csv", encoding="utf8") as file:
    for i in file :
        if not( "id" in i):

            x=i.split(",")

            y=x[1].split(" ")

            z=y[0]+"_" + y[1][0] +y[2][0]
            x.append(z)
            print(z)
            p=""
            for i in range(8):
                t=random.randint(0,255)
                t1=chr(t)
                p=p+t1
            x.append(p)
            print(x)