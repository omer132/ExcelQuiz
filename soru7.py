"""How much higher is the average salary of a C-level person in finance than a mid-level person?"""

import pandas as pd

dataFrame = pd.read_excel("27-SalarySheet.xlsx")

x=dataFrame[dataFrame["Department"]=="Finance"]

avarageaC=x[x["Title"]=="C-level"]["Salary"].mean()
avarageMid=x[x["Title"]=="Mid-Senior"]["Salary"].mean()

salary=avarageaC-avarageMid
print("avarage:",salary)