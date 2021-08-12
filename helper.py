import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
#from cfg import NADIA_SPREAD_SHEET_KEY

ITEM_SHEET = 'items'
CLIENT_SHEET = 'clients'
SPREAD_SHEET = '1JMPyBfHDdRINucDzuTViS6p-E7u3t-jHZRmsFXwFoO0'
CREDS_JSON = '/media/isaiascruz/KINGSTON/curses/telegram_bot/access_key.json'

class gsheet_helper: 
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_JSON,scope)

        # autoriza una conexion hacia la google sheet 
        self.client = gspread.authorize(creds)
        self.gsheet = self.client.open_by_key(SPREAD_SHEET)

    def get_items(self):
        items = self.get_sheet(ITEM_SHEET)
        return items

    def get_sheet(self, sheet_name):
        sheet = self.gsheet.worksheet(sheet_name)
        items = pd.DataFrame(sheet.get_all_records())
        return items

    def store_user(self, user_dic):
        sheet = self.gsheet.worksheet(CLIENT_SHEET)
        clients = pd.DataFrame(self.get_sheet(CLIENT_SHEET))

        cond = clients[clients["id"] == user_dic["id"]].empty

        
        # si no existe guardar
        if cond:
            sheet.add_rows(1)
            sheet.append_row([element for element in user_dic.values()])
        else:
            print("El vato ya existe")





if __name__ == "__main__":
    print(gsheet_helper().get_items())
