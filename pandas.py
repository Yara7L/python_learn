import pandas as pd
import numpy as np
 
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7],
    index=["C", "D", "E", "F", "G", "A", "B"])
 
# for i in series1.index:
#     print("series1[{}] = {} \n".format(i,series1[i]))
# print("series1.E = {} \n".format(series1.E))

df1 = pd.DataFrame({"note" : ["C", "D", "E", "F", "G", "A", "B"],
    "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    index=['1', '2', '3', '4', '5', '6', '7'])
# print("df1.loc['2']:\n{}\n".format(df1.loc['2']))
# print("series1.loc['E':'A']=\n{}\n".format(series1.loc['E':'A']))
# print("df1.iloc[2:4]=\n{}\n".format(df1.iloc[2:4]))

# print("series1.at['E']={}\n".format(series1.at['E']))
# print("df1.iloc[4,1]={}\n".format(df1.iloc[4,1]))



multiIndex = pd.MultiIndex(levels=[['Epple', 'Geagle', 'Macrosoft'], ['S1', 'S2', 'S3', 'S4']],
           labels=[[1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]],
           names=['Company', 'Turnover'])
df = pd.DataFrame(data=np.random.randint(0, 1000, 36).reshape(-1, 12),
                  index=[2016, 2017, 2018],
                  columns=multiIndex)
# print("df = \n{}\n".format(df)) 

df1 = pd.DataFrame({'Note': ['C', 'D'],
                    'Weekday': ['Mon', 'Tue']},
                    index=[1, 2])
df2 = pd.DataFrame({'Note': ['E', 'F'],
                    'Weekday': ['Wed', 'Thu']},
                    index=[3, 4])
df3 = pd.DataFrame({'Note': ['G', 'A', 'B'],
                    'Weekday': ['Fri', 'Sat', 'Sun']},
                    index=[5, 6, 7])
df_concat = pd.concat([df1, df2, df3], keys=['df1', 'df2', 'df3'])
# print("df_concat=\n{}\n".format(df_concat))

df_concat_column = pd.concat([df1, df2, df3], axis=1)
# print("df_concat_column=\n{}\n".format(df_concat_column))

df_append = df1.append([df2, df3])
# print("df_append=\n{}\n".format(df_append))

df1 = pd.DataFrame({'key': ['K1', 'K2', 'K3', 'K4'],
                    'A': ['A1', 'A2', 'A3', 'A8'],
                    'B': ['B1', 'B2', 'B3', 'B8']})
 
df2 = pd.DataFrame({'key': ['K3', 'K4', 'K5', 'K6'],
                    'A': ['A3', 'A4', 'A5', 'A6'],
                    'B': ['B3', 'B4', 'B5', 'B6']})
 
# print("df1=n{}n".format(df1))
# print("df2=n{}n".format(df2))
 
merge_df = pd.merge(df1, df2)
merge_inner = pd.merge(df1, df2, how='inner', on=['key'])
merge_left = pd.merge(df1, df2, how='left')
merge_left_on_key = pd.merge(df1, df2, how='left', on=['key'])
merge_right_on_key = pd.merge(df1, df2, how='right', on=['key'])
merge_outer = pd.merge(df1, df2, how='outer', on=['key'])
 
# print("merge_df=\n{}\n".format(merge_df))
# print("merge_inner=\n{}\n".format(merge_inner))
# print("merge_left=\n{}\n".format(merge_left))
# print("merge_left_on_key=\n{}\n".format(merge_left_on_key))
# print("merge_right_on_key=\n{}\n".format(merge_right_on_key))
# print("merge_outer=\n{}\n".format(merge_outer))

df3 = pd.DataFrame({'key': ['K1', 'K2', 'K3', 'K4'],
                    'A': ['A1', 'A2', 'A3', 'A8'],
                    'B': ['B1', 'B2', 'B3', 'B8']},
                    index=[0, 1, 2, 3])
 
df4 = pd.DataFrame({'key': ['K3', 'K4', 'K5', 'K6'],
                    'C': ['A3', 'A4', 'A5', 'A6'],
                    'D': ['B3', 'B4', 'B5', 'B6']},
                    index=[1, 2, 3, 4])
 
# print("df3=\n{}\n".format(df3))
# print("df4=\n{}\n".format(df4))
 
join_df = df3.join(df4, lsuffix='_self', rsuffix='_other')
join_left = df3.join(df4, how='left', lsuffix='_self', rsuffix='_other')
join_right = df1.join(df4, how='outer', lsuffix='_self', rsuffix='_other')
 
# print("join_df=\n{}\n".format(join_df))
# print("join_left=\n{}\n".format(join_left))
# print("join_right=\n{}\n".format(join_right))



df = pd.DataFrame({
    'Name': ['A','A','A','B','B','B','C','C','C'],
    'Data': np.random.randint(0, 100, 9)})
# print('df=\n{}\n'.format(df))
 
groupby = df.groupby('Name')
 
# print("Print GroupBy:")
# for name, group in groupby:
#     print("Name: {}\nGroup:\n{}\n".format(name, group))

def sort(df):
    return df.sort_values(by='Data', ascending=False)
# print("Sort Group: \n{}\n".format(groupby.apply(sort)))



import datetime as dt 
now = dt.datetime.now()
print("Now is {}".format(now))
 
yesterday = now - dt.timedelta(1)
# print("Yesterday is {}\n".format(yesterday.strftime('%Y-%m-%d')))


this_year = pd.date_range(dt.datetime(2018, 1, 1),dt.datetime(2018, 12, 31), freq='5D')
# print("Selected days in 2018: \n{}\n".format(this_year))

df = pd.DataFrame(np.random.randint(0, 100, this_year.size), index=this_year)
# print("Jan: \n{}\n".format(df['2018-01']))



import matplotlib.pyplot as plt

# data = pd.read_csv("data/housing.csv")
# data.hist(bins=50, figsize=(15, 12))
# plt.show()