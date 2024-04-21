import pandas as pd
import numpy as np

df = pd.read_csv('drinks.csv')
print(df)
print(df.shape)
print(df.dtypes)
print("")

df_C2 = df.groupby('continent').beer_servings.mean()
print(df_C2)
print("")


df_c3 = df.groupby('continent').wine_servings.describe()
print(df_c3)
print("")

df_c4 = df.groupby('continent').wine_servings.mean(),df.groupby('continent').beer_servings.mean()
print("wine_servings.mean  beer_servings.mean")
print(df_c4)
print("")

df_c5 = df.groupby('continent').wine_servings.median(),df.groupby('continent').beer_servings.median()
print(df_c5)
print("")

df_c6 = df.groupby('continent').spirit_servings.agg(['mean','max','min'])
print(df_c6)
print("")

df_c7 = df['beer_servings'].sort_values()
print(df_c7)
print("")

df_c7_max = df['beer_servings'].max()
print(df_c7_max)
