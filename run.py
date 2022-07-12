import  gspread
from google.oauth2.service_account  import Credentials

SCOPE = [
    "http://www.googleapis.com/auth/spreadsheets",
    "http://www.googleapis.com/auth/drive.file",
    "http://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)
