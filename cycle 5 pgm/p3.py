import pandas as pd
#df=pd.read_csv("studentsdetails1.csv")
#spc=df[["Name","Address"]]
#print(spc)
# print(df.head())
#print(df.tail())

df=pd.read_csv("studentsdetails1.csv",usecols=["Roll.No","Name","Class"])
print(df)