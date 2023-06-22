# -*- coding: utf-8 -*-
"""

"""
# from 패키지.모듈 import 함수 
from urllib.request import urlopen # 함수 : 원격서버 url 요청  
from bs4 import BeautifulSoup # 클래스 : html 파싱 



import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=크래프톤",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")
html.select(class="sub_txt", )




# 상영중 영화 사이트 

url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%ED%81%AC%EB%9E%98%ED%94%84%ED%86%A4'

# 1. 원격 서버 url 요청 
req = urlopen(url)  # ulr 요청 
byte_data = req.read() # data 읽기   
print(byte_data)

# 2. html 파싱 
text_data = byte_data.decode("utf-8") # 디코딩 : charset="utf-8" 
print(text_data)
html = BeautifulSoup(text_data, 'html.parser') # html source 파싱
print(html)





# 3. 상영중 영화 주 정보 30개 element 수집(li 태그 30개 수집) 
movie_list = html.select('div[class="lst_wrap"] > ul[class="lst_detail_t1"] > li', limit=30)
print(movie_list) # li 태그 30 
len(movie_list) # 30

movie_list[0]





# //*[@id="content"]/div[1]/div/div[3]/ul/li[1]/dl/dt/a


# 4. url 수집 
urls = [] # url 저장 

base_url = 'https://n.news.naver.com/mnews/article/'
 #https://n.news.naver.com/mnews/article/





# li > div > a
for movie in movie_list : 
    a_tag = movie.select_one('div[class="thumb"] > a')
    urls.append(base_url + a_tag.get('href')) # base_url + url

print(urls)
urls[0] # '/movie/bi/mi/basic.naver?code=215932'
# 'https://movie.naver.com/movie/bi/mi/basic.naver?code=215932'
urls[-1] # https://movie.naver.com/movie/bi/mi/basic.naver?code=217473


# 5. 영화 사이트 이동 : 영화제목과 줄거리 저장  
def crawler(url) : # 자료수집 함수 
    print('url :', url)
    # 1. url 요청 
    req = urlopen(url)  # ulr 요청 
    byte_data = req.read() # data 읽기  
    # 2. 디코딩 
    text_data = byte_data.decode("utf-8")    
    # 3. html 파싱
    html = BeautifulSoup(text_data, 'html.parser')    
    # 4. tag & 내용 수집  
    title = html.select_one('div[class="mv_info"] > h3[class="h_movie"] > a').string   
    summary = html.select_one('div[class="story_area"] > p').text    

    return title, summary 


title = []
summary = [] 

for url in urls :
    t, s = crawler(url)
    title.append(t)
    summary.append(s)

print(title)
print(summary)


# 6. csv file save 
import pandas as pd 

df = pd.DataFrame({'title': title, 'summary': summary},
             columns=['title','summary'])    
# columns : 칼럼 순서 지정 
    
df.info()
'''
RangeIndex: 20 entries, 0 to 19
RangeIndex: 30 entries, 0 to 29
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   title    30 non-null     object
 1   summary  30 non-null     object
'''
  
print(df.head())

# csv file 저장 
path = r"C:\ITWILL\3_TextMining\data"
df.to_csv(path + '/movie_data.csv', index=None)  
# index=None : 행이름 제외    