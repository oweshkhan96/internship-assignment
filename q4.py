import pandas as pd

def average_salary_by_department(df):
    avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
    avg_salary.columns = ['Department', 'Average Salary']
    return avg_salary


data = {
    'Employee': ['John', 'Sarah', 'Alex', 'Jane'],
    'Department': ['HR', 'IT', 'IT', 'HR'],
    'Age': [28, 35, 40, 32],
    'Salary': [50000, 75000, 80000, 55000]
}

df = pd.DataFrame(data)
avg_salary_df = average_salary_by_department(df)
print(avg_salary_df)
