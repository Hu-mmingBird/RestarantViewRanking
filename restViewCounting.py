#-*- encoding: utf-8 -*-
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
from pandas import Series, DataFrame
import datetime
'''
1. 띄어쓰기->앞뒤로 공백 제거, 조합?
2. 지점
3. 컴마로 구분되어 있는건 ex.한성양갈비,양꼬치 -> 한성양꼬치
4. 중단된것 확인 할 열 추가 필요
5. 나중에 수정하려면 업체명을 직접 써둬야하나
6. 인플이 뭐지->인플루언서
'''
"""
1007 dev note
1. 키워드 C열, 업체명 E열
2. 열번호 AMF 계산 알고리즘
3. dataframe으로 index(1부터)
4. info={today:}
5. key 후보: 날짜, 키워드, 업체명,
6. 업데이트: 해당 날짜에 카운팅:(1,x), 스케줄:순위 ranking

"""
dt_now = datetime.datetime.now()
year=dt_now.year
month=dt_now.month
day=dt_now.day
today=str(month)+'.'+str(day)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
JSON_PATH=THIS_FOLDER+'/automationproj-327806-6e9bf5c39245.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials=ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH,scope)
gc=gspread.authorize(credentials)
gc1=gc.open('에프터마케팅18.10~의 사본').worksheet('2019년 월보장')

index=len(gc1.col_values(1))
print(index)#카운팅스케줄기준
index=[i for i in range(1,index+1)]

keyword=gc1.col_values(3)
company=gc1.col_values(5)
info={'keyword':keyword,'company':company}
info['keyword'].append(keyword[-1])
info['company'].append(company[-1])
df=DataFrame(info,index=index)
# try:
#     df=DataFrame(info,index=index)
#     df.index=df.index+1
# except:
#     info['keyword']+=keyword[-1]
#     info['company']+=company[-1]
#     df=DataFrame(info,index=index)
# print(len(keyword),keyword)#375열인데 마지막 2칸짜리 공백이라 무시돼서 374개까지 나옴
print(df)

#label(index)접근
