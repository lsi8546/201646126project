# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:05:58 2019

@author: 이승익
"""

import pandas as pd
df = pd.read_csv('온천동(도로변) 측정소 2019년 05월 대기질 정보 일평균자료.CSV')  
df = df[[ '미세먼지','초미세먼지']]
df = df.corr()
print(df)