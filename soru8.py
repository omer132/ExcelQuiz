"""How many times are there C-level employees in the software development department than in the marketing department?"""

import pandas as pd

dataFrame = pd.read_excel("27-SalarySheet.xlsx")

x=dataFrame[(dataFrame["Department"]=="Software Development")]
y=dataFrame[(dataFrame["Department"]=="Marketing")]

xx=x[x["Title"]=="C-level"]
yy=y[y["Title"]=="C-level"]

software=xx.shape[0]
market=yy.shape[0]

if software>market:
    print("software more than market:",software-market)

elif market>software:
    print("market more than software:",market-software)

else:
    print(f"equal,software {software}\n marketing {market}")

