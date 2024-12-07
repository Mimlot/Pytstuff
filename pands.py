import pandas as pd

lst = [[1, 2], [3, 4], [5, 6]]
df = pd.DataFrame(lst, columns=['nam1', 'nam2'])  
print(df.loc[df['nam1'] > 1, 'nam1'])
