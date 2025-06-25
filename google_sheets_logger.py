import gspread                                                        # python library to read/write google sheets
from oauth2client.service_account import ServiceAccountCredentials    # used to log in to google sheets using a service account (via JSON credentials)
import pandas as pd


# this will be used to open and access the specific sheet
def connect_to_sheet(credentials_path, sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet


# this will save the trade log in the tabs of google sheet ( it will also clear old content and upload new content )
def write_trade_log(sheet, df, tab_name="Trade_Log"):
    try:
        df = df.replace([float('inf'), float('-inf')], None)
        df = df.fillna('') 

        try:
            worksheet = sheet.worksheet(tab_name)
        except:
            worksheet = sheet.add_worksheet(title=tab_name, rows="1000", cols="20")

        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print(f"✅ Trade log written to tab '{tab_name}'")

    except Exception as e:
        print(f"❌ Error writing trade log to Google Sheet: {e}")


# this will write the profit & loss in the tabs of google sheet 
def write_summary(sheet, summary_data, tab_name="P&L Summary"):
    try:
        try:
            worksheet = sheet.worksheet(tab_name)
        except:
            worksheet = sheet.add_worksheet(title=tab_name, rows="100", cols="10")

        worksheet.clear()
        print(f"✅ Writing summary to '{tab_name}':")
        for idx, (k, v) in enumerate(summary_data.items(), start=1):
            safe_value = "" if pd.isna(v) or v in [float("inf"), float("-inf")] else v
            worksheet.update_cell(idx, 1, k)
            worksheet.update_cell(idx, 2, safe_value)
            print(f"  • {k}: {safe_value}")

    except Exception as e:
        print(f"❌ Error writing summary to Google Sheet: {e}")


# this will write the win ratio in the tabs of google sheet 
def write_win_ratio(sheet, ratio, tab_name="Win Ratio"):
    try:
        try:
            worksheet = sheet.worksheet(tab_name)
        except:
            worksheet = sheet.add_worksheet(title=tab_name, rows="10", cols="10")

        worksheet.clear()
        safe_ratio = "" if pd.isna(ratio) or ratio in [float("inf"), float("-inf")] else ratio
        worksheet.update_cell(1, 1, "Win Ratio")
        worksheet.update_cell(1, 2, safe_ratio)
        print(f"✅ Win ratio written to tab '{tab_name}': {safe_ratio}")

    except Exception as e:
        print(f"❌ Error writing win ratio to Google Sheet: {e}")
