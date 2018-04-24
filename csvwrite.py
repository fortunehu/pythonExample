import csv
#csv 写入
fieldnames = ['name','year']
stu1 = ['marry',26]
stu2 = ['bob',23]
out = open('d:/Stu_csv.csv','w', newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(fieldnames)
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print ("write over")