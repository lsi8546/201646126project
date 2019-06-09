# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:49:53 2019

@author: 이승익
"""

import pandas as pd
import matplotlib.pyplot as plt

#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df = pd.read_csv('온천동(도로변) 측정소 2019년 05월 대기질 정보 일평균자료.CSV')  
print(df)

plt.plot(df['날짜'], df['초미세먼지'], 'bo-')
plt.plot(df['날짜'], df['미세먼지'], 'bo-', c='r')
plt.xlabel('날짜')
plt.ylabel('유해물질')
plt.title('부산지역 5월 유해물질 양 변화')
plt.legend()
plt.show
