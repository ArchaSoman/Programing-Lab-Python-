import csv
cars=[{'No':1,'Company':'Ferrari','Model':'488GTB'},{'No':2,'Company':'Audi','Model':'64589H'}]
csvfile=open('Name.csv','w')
field_names=list(cars[0].keys())

writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()

csv_file=open('Name.csv','r')