#-*- encoding: utf-8 -*-
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import datetime
'''
1.띄어쓰기->앞뒤로 공백 제거, 조합?
2.지점
3.컴마로 구분되어 있는건 ex.한성양갈비,한성양갈비
4.중단된것 확인 할 열 추가 필요
'''
dt_now = datetime.datetime.now()
year=dt_now.year
month=dt_now.month
day=dt_now.day

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
JSON_PATH=THIS_FOLDER+'/automationproj-327806-6e9bf5c39245.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials=ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH,scope)
gc=gspread.authorize(credentials)

spreadsheet_url='https://docs.google.com/spreadsheets/d/1wNowA_DfSIjEWnw7hgydiQFmPrw8SL_o1RgejqYalOc/edit#gid=1476274737'
doc=gc.open_by_url(spreadsheet_url)

worksheet=doc.worksheet('2019년 월보장')
# print(worksheet)

keyword=worksheet.col_values(3)
company=worksheet.col_values(5)
key_com=dict(zip(keyword,company))
# print(key_com)
    