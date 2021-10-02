#-*- encoding: utf-8 -*-
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH=THIS_FOLDER+'/automationproj-327806-6e9bf5c39245.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
sheet="에프터마케팅18.10~의 사본"
worksheet="2019 월보장"
sheet=sheet.encode('utf-8')
worksheet=worksheet.encode('utf-8')

credentials=ServiceAccountCredentials.from_json_keyfile_name(PATH,scope)
gc=gspread.authorize(credentials)

gc1=gc.open(sheet).worksheet(worksheet)
gc2=gc1.get_all_values()
print(gc2)
