import os
import csv

movies = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]


with open(os.path.join("C:\\","Users","ABHIJEET","OneDrive","Desktop","Programming","assignment.csv"),"w") as a:
    write = csv.writer(a,delimiter=",")
    for i in movies:
        write.writerow(i)

        
