"""How does the average salary compare according to title (senior - junior) performance in this company?"""

import pandas as pd


dataFrame=pd.read_excel("27-SalarySheet.xlsx")

x=dataFrame[dataFrame["Title"].isin(["Senior","Junior"])]

ortalama=x.groupby("Title")["Salary"].mean()

ortalamasen=ortalama["Senior"]
ortalamamas=ortalama["Junior"]
print("senior:",ortalamasen)
print("Junior:",ortalamamas)