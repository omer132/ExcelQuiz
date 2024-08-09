"""What is the average salary percentage of a senior person compared to a junior person?"""

import pandas as pd
import numpy as np

dataFrame=pd.read_excel("27-SalarySheet.xlsx")

x=dataFrame[dataFrame["Title"].isin(["Senior","Junior"])]

ortalama=x.groupby("Title")["Salary"].mean()

ortalamasen=ortalama["Senior"]
ortalamamas=ortalama["Junior"]

yüzde=ortalamasen/ortalamamas

print("average percentage",yüzde)