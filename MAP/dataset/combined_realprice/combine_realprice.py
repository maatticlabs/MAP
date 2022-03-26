# -*- coding: utf-8 -*- 
import pandas as pd

data = pd.read_excel(f'/Users/ryuchangmin/Desktop/DA/dataset/realprice/2012_1.xlsx')
columns = data.iloc[15]

raw = pd.DataFrame()
for i in range(2012,2022):
    for j in range(1,4):
        name = str(i)+'_'+str(j)+'.xlsx'
        data = pd.read_excel(f'/Users/ryuchangmin/Desktop/DA/dataset/realprice/{name}')
        print(name)
        # columns = data.iloc[15]
        # print(columns)
        df = pd.DataFrame(data.iloc[16:])
        raw = pd.concat([raw, df])

raw.reset_index(inplace=True)
# raw.columns = columns
raw.to_csv('price.csv')
