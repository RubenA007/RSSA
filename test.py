from fastapi import FastAPI
import os
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds

app = FastAPI()

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
    global table_value
    table_value += 1
    return ("complete")

@app.get("/value")
async def read_value():
    return{sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1", "Лист2"]).execute()}

# resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A1:A999").execute()