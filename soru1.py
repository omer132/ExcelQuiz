"""How many lines are there in total?"""

import pandas as pd
import numpy as np

dataFrame=pd.read_excel("27-SalarySheet.xlsx")
x=len(dataFrame)
print(f"number of lines {x}")