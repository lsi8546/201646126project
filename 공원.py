# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:52:10 2019

@author: 이승익
"""
import pandas as pd
import matplotlib.pyplot as plt

#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df = pd.read_csv('전국도시공원표준데이터.CSV') 
df = df.groupby('제공기관명')['관리번호'].nunique()
print(df)

df.plot(kind='bar')
plt.xlabel('지역')
plt.ylabel('공원수')
plt.title('지역별 공원수')
plt.show()

