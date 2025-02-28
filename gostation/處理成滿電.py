import datetime
import csv

with open('新竹市站點.csv',mode='r',newline='',encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        maxbattery = int(row[5])
        minbattery = int(row[6])
        earliest = datetime.datetime.strptime(row[7], '%Y/%m/%d %H:%M:%S')
        latest = datetime.datetime.strptime(row[8], '%Y/%m/%d %H:%M:%S')
        diffsec = (latest - earliest).total_seconds()
        with open(row[0]+'.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        temp = content.split(' ')
        ls = list()
        maximumy =0
        minimumy =100000
        for i in range(int(len(temp)/3)):
            templs =list()
            templs.append(float(temp[3*i+1]))
            templs.append(float(temp[3*i+2]))
            if templs[1] > maximumy:
                maximumy = templs[1]
            if templs[1] < minimumy:
                minimumy = templs[1]
            ls.append(templs)
        mintime = ls[0][0]
        maxtime = ls[len(ls) - 1][0]
        for i in range(len(ls)):
            ls[i][0] = earliest + datetime.timedelta(seconds=(int((ls[i][0] - mintime) * diffsec / (maxtime - mintime))))
            ls[i][1] = maxbattery - round((ls[i][1] - minimumy) * (maxbattery - minbattery) / (maximumy - minimumy) + minbattery)
        print(ls)
        earliestneed = datetime.datetime(2024,5,20,0,0,0)
        latestneed = datetime.datetime(2024,5,27,0,0,0)
        demand = [ 0 for _ in range(336)]
        supply = [ 0 for _ in range(336)]

        for i in range(len(ls)):
            if ls[i][0] >= earliestneed and ls[i][0] < latestneed:
                s = int((ls[i][0] - earliestneed).total_seconds() // 1800)
                if supply[s] == 0:
                    supply[s] = ls[i][1]
                    if ls[i][1] - ls[i-1][1] < 0:
                        demand[s] += ls[i-1][1] - ls[i][1]
                else:
                    if ls[i][1] - ls[i-1][1] > 0:
                        supply[s] += ls[i][1] - ls[i-1][1]
                    elif ls[i][1] - ls[i-1][1] < 0:
                        demand[s] += ls[i-1][1] - ls[i][1]
        for i in range(len(supply)):
            if i-1>=0 and i+1<len(supply) and supply[i-1]!=0 and supply[i+1]!=0 and supply[i]==0:
                supply[i] = supply[i-1]
        print(demand)
        print(supply)
        output_file = 'origin/'+row[0]+'demand_supply.csv'

        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Demand', 'Supply'])
            for d, s in zip(demand, supply):
                writer.writerow([d, s])
