import csv

gostation = list()
stationdemand = dict()
with open('gostationTM2.csv', mode='r',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        temp = list()
        temp.append(row[0])
        temp2 = list()
        with open('gostation/origin/'+ temp[0] +'demand_supply.csv', mode='r',newline='',encoding='utf-8') as f1:
            reader1 = csv.reader(f1)
            d = 0
            next(reader1)
            last = 0
            for i, line in enumerate(reader1, start=1):
                if i % 48 not in range(1, 17): 
                    temp2.append(int(line[1]))
            for i in range(len(temp2)):
                if temp2[i]==0 and temp2[i-1]>0 and i-1>=0 and i+1< len(temp2) and temp2[i+1]>0:
                    d+= temp2[i-1]
                else:
                    d+= temp2[i]
            temp.append(d/224) 
            print(d)
        gostation.append(temp)

with open('gostation/origin/站供給.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['站名', 'AVGSupply'])
    for i in range(len(gostation)):
        writer.writerow(gostation[i])