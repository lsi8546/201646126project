# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
조경학과 |201646126 |이승익


## 프로젝트 개요
1.최근 전국 미세먼지 데이터 분석, 시각화

2.피어슨 상관계수를 통한 나무수와 미세먼지와의 상관관계 도출

3.전국의 공원수 데이터 시각화

4.미세먼지 감축을 위해 더많은 공원을 만들어야 한다는 결론 도출

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 코드 삽입
~~~python
import pandas as pd
import matplotlib.pyplot as plt

#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

#1.최근 부산지역 미세먼지 변화량 분석
df = pd.read_csv('온천동(도로변) 측정소 2019년 05월 대기질 정보 일평균자료.CSV')  
print(df)

plt.plot(df['날짜'], df['초미세먼지'], 'bo-')
plt.plot(df['날짜'], df['미세먼지'], 'bo-', c='r')
plt.xlabel('날짜')
plt.ylabel('유해물질')
plt.title('부산지역 5월 유해물질 양 변화')
plt.legend()
plt.show
--------------------------------------------------------------------------------------------------------------------------------------
#2.2018년 한해동안 우리나라 지역별 미세먼지양 분석
df = pd.read_csv('2018년.CSV')  
df = df.groupby('지역')['미세먼지'].mean()
print(df)

df.plot(kind='bar')
plt.xlabel('지역')
plt.ylabel('미세먼지')
plt.title('2018년도 전국 미세먼지 양')
plt.show()
--------------------------------------------------------------------------------------------------------------------------------------
#3.지역별 산림현황
df = pd.read_csv('나무.CSV')  
df = df[['지역', '전체면적(만㎡)']]
df = df.head(17)
print(df)

plt.bar(df['지역'], df['전체면적(만㎡)'])
plt.xlabel('지역')
plt.ylabel('산림면적')
plt.title('지역별 산림면적')
plt.show()
--------------------------------------------------------------------------------------------------------------------------------------
#4.미세먼지양과 나무(산림)간의 상관관계 도출
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
--------------------------------------------------------------------------------------------------------------------------------------
#5. 전국의 지역별 공원의 수 분석
df = pd.read_csv('전국도시공원표준데이터.CSV') 
df = df.groupby('제공기관명')['관리번호'].nunique()
print(df)

df.plot(kind='bar')
plt.xlabel('지역')
plt.ylabel('공원수')
plt.title('지역별 공원수')
plt.show()
~~~

##결론
지난달 5월 부산지역의 미세먼지양 변화를 분석해보니 부산지역에도 미세먼지 기준 나쁨이 넘어가는 날이 종종 있음을 확인하였다.
작년 기준으로 지역별 미세먼지 양과 지역별 나무(산림)과의 상관계수를 보아 다소 반비례하는 것을 알수있었다.
하지만 현재 지역별 도시공원의 수를 분석해 보았을때 수도권지역에 미해 부산지역은 공원의 수가 작은것으로 보인다.
시민들의 건강의 위해 도시 공원이 더 만들어져야 한다는 결론을 도출하였다.
