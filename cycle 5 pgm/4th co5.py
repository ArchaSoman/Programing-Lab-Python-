import csv
with open('studentdetails - studentdetails.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('newstudentsdetailssss.csv','w')as csv_file1:
        fieldnames1=['Roll No','Student Name','Grade','CO1','CO2','CO3','CO4','CO5']
        csv_writer=csv.DictWriter(csv_file1,fieldnames=fieldnames1)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
        #print(line)