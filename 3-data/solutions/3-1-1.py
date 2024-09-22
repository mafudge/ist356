import pandas as pd
import numpy as np

s1 = pd.Series(data = [1, 2, 3, 4], index=['a', 'b', 'c', 'd'], name='s1')
s2 = pd.Series(data = [2.2, np.nan, 3.0, 1.5], index=['a', 'b', 'c', 'd'], name='s3')
s3 = pd.Series(data = ['q', 'q', 'z', 'z'], index=['a', 'b', 'c', 'd'], name='s3')

df = pd.DataFrame({'s1':s1,'s2':s2,'s3':s3})
print(df)

print(df.loc['a':'b', 's1':'s2'])