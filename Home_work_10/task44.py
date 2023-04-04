import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame(columns=["robot", "human"])

for index, row in data.iterrows():
    if row['whoAmI'] == 'robot':
        one_hot.loc[index] = [1, 0]
    else:
        one_hot.loc[index] = [0, 1]

one_hot.index = data.index

print("Original DataFrame:")
print(data)

print("\nOne-Hot Encoded DataFrame:")
print(one_hot)