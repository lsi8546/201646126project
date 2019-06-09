# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:52:40 2019

@author: 이승익
"""
import pandas as pd
import matplotlib.pyplot as plt

#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df = pd.read_csv('나무.CSV')  
df = df[['지역', '전체면적(만㎡)']]
df = df.head(17)
print(df)

plt.bar(df['지역'], df['전체면적(만㎡)'])
plt.xlabel('지역')
plt.ylabel('산림면적')
plt.title('지역별 산림면적')
plt.show()
