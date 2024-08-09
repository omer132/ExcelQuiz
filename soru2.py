"""How much salary does this company pay?"""

import pandas as pd
import numpy as np

dataFrame=pd.read_excel("27-SalarySheet.xlsx")

ortalama=dataFrame["Salary"].mean()
print(ortalama)