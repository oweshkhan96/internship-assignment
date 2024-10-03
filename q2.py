import pandas as pd

def fill_missing_grades_with_average(df):
    for subject in df.columns[1:]:
        subject_mean = df[subject].mean()
        df[subject].fillna(subject_mean, inplace=True)

    return df

data = {
    'Student': ['Akhil', 'Bhanu', 'Clara'],
    'Math': [85, 70, None],
    'Science': [None, 88, 90],
    'English': [78, None, 85],
    'History': [90, 75, None]
}

df = pd.DataFrame(data)
filled_df = fill_missing_grades_with_average(df)
print(filled_df)
