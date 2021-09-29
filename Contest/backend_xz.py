import csv
from datetime import datetime
tmp=[]
_type1=["KGT","COLD","OTHER"]
with open('/home/andrey/Рабочий стол/yandex_cup/input.txt', newline='') as File: 
reader = csv.reader(File)
for row in reader:
# print(row)
if row[2]=='NULL':
for i in _type1:
tmp.append([f'{row[0]}',f'{row[1]}',f'{i}'])
else:tmp.append(row)
 
tmp.sort(key=lambda x: [x[0],_type1.index(x[2]),x[1]])
 
for i in tmp:
print(i)
print("\n")
result=tmp[:]
for i in range(len(tmp)):
 
date1=datetime.strptime(tmp[i][1].split(" ")[0],"%Y-%m-%d")
date2=datetime.strptime(tmp[i][1].split(" ")[1],"%Y-%m-%d")
for j in range(i+1,len(tmp)):
date3=datetime.strptime(tmp[j][1].split(" ")[0],"%Y-%m-%d")
date4=datetime.strptime(tmp[j][1].split(" ")[1],"%Y-%m-%d")
if date1<=date3 and date2>=date4 and tmp[i][0]==tmp[j][0] and tmp[i][2]==tmp[j][2]:
result.remove(tmp[j])
 
myFile = open('output.txt', 'w')
with myFile:
writer = csv.writer(myFile)
writer.writerows(result)