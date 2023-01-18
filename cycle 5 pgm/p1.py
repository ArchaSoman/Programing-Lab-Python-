"""fn=open("file.txt","r")
Lines=fn.readlines()
l1=[line.strip() for line in Lines]
print(l1)
#print([line.strip() for line in open('file.txt','r') ])
l=s.split()
print(l)
fn.close()"""
fn1=open('file.txt','r')
f=fn1.readlines()
for x in range(0,len(f)):
    print(f[x])
fn1.close()    
