# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:43:08 2019

@author: 이승익
"""

import pandas as pd
import matplotlib.pyplot as plt

#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df = pd.read_csv('2018년.CSV')  
df = df.groupby('지역')['미세먼지'].mean()
print(df)

df.plot(kind='bar')
plt.xlabel('지역')
plt.ylabel('미세먼지')
plt.title('2018년도 전국 미세먼지 양')
plt.show()
