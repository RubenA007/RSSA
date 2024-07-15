from fastapi import FastAPI
import os
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from random import randrange

import creds

app = FastAPI()

def getnice():
    print(sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1", "Лист2"]).execute())

def get_values():
    values = [[randrange(0,5)]]
    # values = [[randrange(10, 99) for _ in range(0, 6)]]
    # values = [[randrange(10, 99)] for _ in range(0, 3)]
    # values = [[randrange(10, 99) for _ in range(0, 3)] for _ in range(0, 3)]
    return values

table_value = 0
def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/creds/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)
service = get_service_sacc()
sheet = service.spreadsheets()
sheet_id = "1HYHpniPx60_yzt224M_S_ybWOta--9AsYRYAKhF_MHI"

@app.post("/increment")
async def increment_value():
    getgood()
    return {"complete"}

@app.get("/value")
async def read_value():
    getnice()
    return {"good"}


# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update
def getgood():
    sheet.values().update(
    spreadsheetId=sheet_id,
    range="Лист1!A1",
    valueInputOption="RAW",
    body={'values' : get_values() }).execute()
 



# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
# resp = sheet.values().append(
#     spreadsheetId=sheet_id,
#     range="Лист2!A1",
#     valueInputOption="RAW",
#     # insertDataOption="INSERT_ROWS",
#     body={'values' : get_values() }).execute()

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
# body = {
#     'valueInputOption' : 'RAW',
#     'data' : [
#         {'range' : 'Лист2!D2', 'values' : get_values()},
#         {'range' : 'Лист2!H4', 'values' : get_values()}
#     ]
# }

# resp = sheet.values().batchUpdate(spreadsheetId=sheet_id, body=body).execute()


