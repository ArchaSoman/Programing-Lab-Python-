import csv
with open('studentsdetails1.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    with open('newstudentsdetails1.csv','w') as csv_file1:
        csv_writer=csv.writer(csv_file1)
#print(csv_reader)
        for line in csv_reader:
            csv_writer.writerow(line)
    #print(line)