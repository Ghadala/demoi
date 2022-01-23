# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

data=pd.read_csv("C:/Users/galasaker/Downloads/emp.csv")
df=pd.DataFrame(data)
print(data)
print("----------------------------")
print(data.isnull())
data.fillna(method="bfill")
data.loc[1,'record_id']=123456
print(data)
data.to_csv("tempupdate.csv")
