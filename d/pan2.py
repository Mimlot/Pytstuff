import pandas as pd 

df = pd.read_csv("lmao2.csv")

df2 = df[df['nam2'] > 5]
df2.to_csv("lmao5.csv")