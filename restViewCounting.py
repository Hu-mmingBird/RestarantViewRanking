#-*- encoding: utf-8 -*-
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
JSON_PATH=THIS_FOLDER+'/automationproj-327806-6e9bf5c39245.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials=ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH,scope)
gc=gspread.authorize(credentials)

spreadsheet_url='https://docs.google.com/spreadsheets/d/1p_pr6_6dGvHvpYpYNhax2P-UR_yrNJPQ0-5ht2UxWWg/edit#gid=1476274737'
doc=gc.open_by_url(spreadsheet_url)

worksheet=doc.worksheet('2019년 월보장')
print(worksheet)
row_data=worksheet.row_values(1)
print(row_data)
