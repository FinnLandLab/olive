import scipy.stats as ss
import pandas as pd
import numpy as np

square_prob_array = ss.bernoulli.rvs(0.1, size=135)
print square_prob_array

for i in range(len(square_prob_array) - 1, -1, -1):
    if square_prob_array[i]:
        print i

df1 = pd.read_csv('participant_1.csv')
df = pd.Series(np.nan, index=df1.columns.values)

# result = df1.append(df, ignore_index=True)
result = df1.ix[:2]
result = result.append(df, ignore_index=True)
result = result.append(df1.ix[3:], ignore_index=True)

# result = df1

print result

# print df
# concat([df.ix[:2], line, df.ix[3:]]).reset_index(drop=True)
