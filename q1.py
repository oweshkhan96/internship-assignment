import pandas as pd

def find_subject_wise_toppers(df):
    toppers = {}
    for subject in df.columns[1:]:
        topper_index = df[subject].idxmax()
        topper_name = df['Student'][topper_index]
        toppers[subject] = topper_name
    toppers_df = pd.DataFrame(list(toppers.items()), columns=['Subject', 'Topper'])
    return toppers_df

data = {
    'Student': ['Akhil', 'Ravi', 'Neha', 'Priya', 'Bhanu'],
    'Maths': [70, 88, 92, 60, 95],
    'Science': [85, 76, 90, 75, 90],
    'Social': [80, 89, 85, 70, 75]
}

df = pd.DataFrame(data)
toppers_df = find_subject_wise_toppers(df)
print(toppers_df)
