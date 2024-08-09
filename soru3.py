"""How does the average salary compare according to departments in this company?"""

import pandas as pd
import numpy as np

dataFrame=pd.read_excel("27-SalarySheet.xlsx")

x=dataFrame.groupby("Department")

v=x["Salary"].mean()

print(v)