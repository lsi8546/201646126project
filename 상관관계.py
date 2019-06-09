# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:56:00 2019

@author: 이승익
"""

import pandas as pd

df1 = pd.read_csv('나무.CSV')  
df1 = df1[['지역', '전체면적(만㎡)']]
df1 = df1.head(17)

df2 = pd.read_csv('2018년.CSV')
df2 = df2.groupby('지역')['미세먼지'].mean()

df = pd.merge(df1, df2, on="지역") 
df = df[[ '전체면적(만㎡)','미세먼지']]
df = df.head(17)
df = df.corr()
print(df)