import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'whoAmI_robot'] = True
data.loc[data['whoAmI'] == 'human', 'whoAmI_robot'] = False
data.loc[data['whoAmI'] == 'human', 'whoAmI_human'] = True
data.loc[data['whoAmI'] == 'robot', 'whoAmI_human'] = False
print(data.head())