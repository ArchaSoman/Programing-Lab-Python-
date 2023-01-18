import csv
csv_file=open('studentsdetails1.csv','r')
csv_reader=csv.reader(csv_file)
#print(csv_reader)

for line in csv_reader:
    print(line)