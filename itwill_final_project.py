# 아이티윌 파이널 프로젝트 (coding: UTF-8)

#라이브러리

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import urllib.parse
import numpy as np
from tqdm import tqdm
###############################################################################

# csv 파일 읽기

# 경로 지정(본인 경로에 맞게 수정 요망)
path = r"C:\Users\itwill\Desktop\git_test"

# 파일 불러오기
df_Base = pd.read_csv(f'{path}/Base_Data.csv')
df_Base.info()

'''
#   Column           Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   일자            10478 non-null  object 
 1   구분1           10478 non-null  object 
 2   발전소코드      10478 non-null  object 
 3   발전소용량(KW)  10478 non-null  float64
 4   0:00            10478 non-null  float64
 5   1:00            10478 non-null  float64
 6   2:00            10478 non-null  object 
 7   3:00            10478 non-null  object 
 8   4:00            10478 non-null  object 
 9   5:00            10478 non-null  float64
 10  6:00            10478 non-null  float64
 11  7:00            10478 non-null  float64
 12  8:00            10478 non-null  float64
 13  9:00            10478 non-null  float64
 14  10:00           10478 non-null  float64
 15  11:00           10478 non-null  float64
 16  12:00           10478 non-null  float64
 17  13:00           10478 non-null  float64
 18  14:00           10478 non-null  float64
 19  15:00           10478 non-null  float64
 20  16:00           10478 non-null  float64
 21  17:00           10478 non-null  float64
 22  18:00           10478 non-null  float64
 23  19:00           10478 non-null  float64
 24  20:00           10478 non-null  object 
 25  21:00           10478 non-null  object 
 26  22:00           10478 non-null  object 
 27  23:00           10478 non-null  object 
 28  합계            10478 non-null  float64
'''

###############################################################################

#실측값과 예측값으로 자료 구조 나누기 후 저장

import pandas as pd

# 경로 지정(본인 경로에 맞게 수정 요망)
path = r"C:\Users\itwill\Desktop\git_test"

df_Base = pd.read_csv(f'{path}/Base_Data.csv')

# "구분1" 칼럼 값에 따라 실측과 예측으로 데이터프레임 분리

df_actual = df_Base[df_Base['구분1'] == '실측']
df_prediction = df_Base[df_Base['구분1'] == '예측']

# 분리된 데이터프레임을 각각 CSV 파일로 저장

df_actual.to_csv(f'{path}/실측.csv', index=False)
df_prediction.to_csv(f'{path}/예측.csv', index=False)

#실측과 예측 데이터 프레임 확인

df_actual.info()
'''
Int64Index: 5239 entries, 0 to 10270
Data columns (total 29 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   일자         5239 non-null   object 
 1   구분1        5239 non-null   object 
 2   발전소코드      5239 non-null   object 
 3   발전소용량(KW)  5239 non-null   float64
 4   0:00       5239 non-null   float64
 5   1:00       5239 non-null   float64
 6   2:00       5239 non-null   object 
 7   3:00       5239 non-null   object 
 8   4:00       5239 non-null   object 
 9   5:00       5239 non-null   float64
 10  6:00       5239 non-null   float64
 11  7:00       5239 non-null   float64
 12  8:00       5239 non-null   float64
 13  9:00       5239 non-null   float64
 14  10:00      5239 non-null   float64
 15  11:00      5239 non-null   float64
 16  12:00      5239 non-null   float64
 17  13:00      5239 non-null   float64
 18  14:00      5239 non-null   float64
 19  15:00      5239 non-null   float64
 20  16:00      5239 non-null   float64
 21  17:00      5239 non-null   float64
 22  18:00      5239 non-null   float64
 23  19:00      5239 non-null   float64
 24  20:00      5239 non-null   object 
 25  21:00      5239 non-null   object 
 26  22:00      5239 non-null   object 
 27  23:00      5239 non-null   object 
 28  합계         5239 non-null   float64
'''

df_prediction.info()
'''
Int64Index: 5239 entries, 1 to 10477
Data columns (total 29 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   일자         5239 non-null   object 
 1   구분1        5239 non-null   object 
 2   발전소코드      5239 non-null   object 
 3   발전소용량(KW)  5239 non-null   float64
 4   0:00       5239 non-null   float64
 5   1:00       5239 non-null   float64
 6   2:00       5239 non-null   object 
 7   3:00       5239 non-null   object 
 8   4:00       5239 non-null   object 
 9   5:00       5239 non-null   float64
 10  6:00       5239 non-null   float64
 11  7:00       5239 non-null   float64
 12  8:00       5239 non-null   float64
 13  9:00       5239 non-null   float64
 14  10:00      5239 non-null   float64
 15  11:00      5239 non-null   float64
 16  12:00      5239 non-null   float64
 17  13:00      5239 non-null   float64
 18  14:00      5239 non-null   float64
 19  15:00      5239 non-null   float64
 20  16:00      5239 non-null   float64
 21  17:00      5239 non-null   float64
 22  18:00      5239 non-null   float64
 23  19:00      5239 non-null   float64
 24  20:00      5239 non-null   object 
 25  21:00      5239 non-null   object 
 26  22:00      5239 non-null   object 
 27  23:00      5239 non-null   object 
 28  합계         5239 non-null   float64
'''
###############################################################################

#발전소 코드별로 데이터 프레임 정리하기 후 저장

import pandas as pd

path = r"C:\Users\itwill\Desktop\git_test"

# 실측 데이터프레임 정렬
df_actual_sorted = df_actual.groupby('발전소코드').apply(lambda x: x.sort_values('일자'))

# 예측 데이터프레임 정렬
df_prediction_sorted = df_prediction.groupby('발전소코드').apply(lambda x: x.sort_values('일자'))

# 정렬된 데이터프레임을 CSV 파일로 저장
df_actual_sorted.to_csv(f'{path}/실측발전소코드별정렬.csv', index=False)
df_prediction_sorted.to_csv(f'{path}/예측발전소코드별정렬.csv', index=False)

df_actual_sorted.info()
'''
Data columns (total 29 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   일자         5239 non-null   object 
 1   구분1        5239 non-null   object 
 2   발전소코드      5239 non-null   object 
 3   발전소용량(KW)  5239 non-null   float64
 4   0:00       5239 non-null   float64
 5   1:00       5239 non-null   float64
 6   2:00       5239 non-null   object 
 7   3:00       5239 non-null   object 
 8   4:00       5239 non-null   object 
 9   5:00       5239 non-null   float64
 10  6:00       5239 non-null   float64
 11  7:00       5239 non-null   float64
 12  8:00       5239 non-null   float64
 13  9:00       5239 non-null   float64
 14  10:00      5239 non-null   float64
 15  11:00      5239 non-null   float64
 16  12:00      5239 non-null   float64
 17  13:00      5239 non-null   float64
 18  14:00      5239 non-null   float64
 19  15:00      5239 non-null   float64
 20  16:00      5239 non-null   float64
 21  17:00      5239 non-null   float64
 22  18:00      5239 non-null   float64
 23  19:00      5239 non-null   float64
 24  20:00      5239 non-null   object 
 25  21:00      5239 non-null   object 
 26  22:00      5239 non-null   object 
 27  23:00      5239 non-null   object 
 28  합계         5239 non-null   float64
'''

df_prediction_sorted.info()
'''
Data columns (total 29 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   일자         5239 non-null   object 
 1   구분1        5239 non-null   object 
 2   발전소코드      5239 non-null   object 
 3   발전소용량(KW)  5239 non-null   float64
 4   0:00       5239 non-null   float64
 5   1:00       5239 non-null   float64
 6   2:00       5239 non-null   object 
 7   3:00       5239 non-null   object 
 8   4:00       5239 non-null   object 
 9   5:00       5239 non-null   float64
 10  6:00       5239 non-null   float64
 11  7:00       5239 non-null   float64
 12  8:00       5239 non-null   float64
 13  9:00       5239 non-null   float64
 14  10:00      5239 non-null   float64
 15  11:00      5239 non-null   float64
 16  12:00      5239 non-null   float64
 17  13:00      5239 non-null   float64
 18  14:00      5239 non-null   float64
 19  15:00      5239 non-null   float64
 20  16:00      5239 non-null   float64
 21  17:00      5239 non-null   float64
 22  18:00      5239 non-null   float64
 23  19:00      5239 non-null   float64
 24  20:00      5239 non-null   object 
 25  21:00      5239 non-null   object 
 26  22:00      5239 non-null   object 
 27  23:00      5239 non-null   object 
 28  합계         5239 non-null   float64
'''
###############################################################################




