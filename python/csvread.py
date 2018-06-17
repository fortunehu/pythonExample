import csv
#csv 读取
csvin = open('d:/Stu_csv.csv','r',)
csv_read = csv.reader(csvin,dialect='excel')
for stu in csv_read:
    # 行号从1开始
    print(stu)