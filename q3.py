import pandas as pd

def add_population_density(df):
    df['Population Density'] = df['Population'] / df['Area (sq km)']
    return df

data = {
    'City': ['CityA', 'CityB', 'CityC'],
    'Population': [500000, 1200000, 300000],
    'Area (sq km)': [300, 500, 150]
}

df = pd.DataFrame(data)
df_with_density = add_population_density(df)
print(df_with_density)
