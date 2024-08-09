"""What is the average salary of a senior person in the software development department compared to a junior person?"""

import pandas as pd

dataFrame = pd.read_excel("27-SalarySheet.xlsx")

yazilim_gelisim_df = dataFrame[dataFrame["Department"] == "Software Development"]

avarage_senior_salary = yazilim_gelisim_df[yazilim_gelisim_df["Title"] == "Senior"]["Salary"].mean()
avarage_junior_salary = yazilim_gelisim_df[yazilim_gelisim_df["Title"] == "Junior"]["Salary"].mean()

salary_difference = avarage_senior_salary - avarage_junior_salary

print(f"Senior pozisyonundaki bir kişinin, Junior pozisyondaki bir kişiye göre ortalama maaşı {salary_difference:.2f} birim daha fazladır.")
