import csv
file = open("CommaSeparate.csv",'r')
content = csv.reader(file,delimiter=",")
for item in content:
    print(item)

file.close()