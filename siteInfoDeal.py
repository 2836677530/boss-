import pandas as pd
data = pd.read_csv('newjava.csv')
data_1=data['site'].value_counts()
data_1.to_csv('countsite.csv')
print(data_1)