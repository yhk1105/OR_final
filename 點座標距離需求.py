import csv

gostation = list()
stationdemand = dict()
with open('gostationTM2.csv', mode='r',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        temp = list()
        temp.append(row[0])
        temp.append(float(row[1]))
        temp.append(float(row[2]))
        with open('gostation/origin/'+ temp[0] +'demand_supply.csv', mode='r',newline='',encoding='utf-8') as f1:
            reader1 = csv.reader(f1)
            d = 0
            next(reader1)
            for i, line in enumerate(reader1, start=1):
                    if i % 48 not in range(1, 17): 
                        d += int(line[0])
            temp.append(d/224) 
            print(d)
        gostation.append(temp)

temp = [0 for _ in range(len(gostation))]
a = list()
with open("點座標.csv", mode='r',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    header1 = next(reader)
    for row in reader:
        minindex = 0
        min = 1000000000000000
        for i in range(len(gostation)):
            if min > pow(float(row[2]) - gostation[i][1],2) + pow(float(row[3]) - gostation[i][2],2):
                min = pow(float(row[2]) - gostation[i][1],2) + pow(float(row[3]) - gostation[i][2],2)
                minindex = i
        temp[minindex]+=1
        a.append([row[2],row[3],minindex])
for i in range(len(a)):
    a[i][2] = gostation[a[i][2]][3]/temp[a[i][2]]


with open('gostation/origin/點需求.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['TM2x', 'TM2y','AVGdemand'])
    for i in range(len(a)):
        writer.writerow(a[i])

