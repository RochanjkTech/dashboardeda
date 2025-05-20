import pandas as pd
import numpy as np


df = pd.read_csv('steam-200k.csv', header=None)


df.drop_duplicates(inplace=True)

df.drop(columns=4, inplace=True)


df.dropna(subset=[0, 2], inplace=True)

df.iloc[:, 1] = df.iloc[:, 1].fillna('Unknown Game')

df.iloc[:, 3] = pd.to_numeric(df.iloc[:, 3], errors='coerce')


play_mask = df.iloc[:, 2] == 'play'
purchase_mask = df.iloc[:, 2] == 'purchase'

play_median = df.loc[play_mask, 3].median()
df.loc[play_mask & df[3].isna(), 3] = play_median


df.loc[purchase_mask & df[3].isna(), 3] = 1.0

Q1 = df.loc[play_mask, 3].quantile(0.25)
Q3 = df.loc[play_mask, 3].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


df = df[~(play_mask & ((df[3] < lower_bound) | (df[3] > upper_bound)))]

df.reset_index(drop=True, inplace=True)

print(df.head())

df.to_csv('cleaned_steam_data.csv', header=False, index=False)
