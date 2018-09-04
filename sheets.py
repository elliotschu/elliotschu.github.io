"""
Elliot Schumacher, Johns Hopkins University
Created 7/17/18

Helpful troubleshooting links-
https://stackoverflow.com/questions/46274040/append-a-list-in-google-sheet-from-python
https://developers.google.com/sheets/api/quickstart/python
https://stackoverflow.com/questions/36061433/how-to-do-i-locate-a-google-spreadsheet-id
"""
import time
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import socket
def add_score_results(results):
    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('../client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()), cache_discovery=False)
    if results is None:
        row = [["test1", "test2", "test3", "test4", 'test5', "test6"]]
    else:
        server = socket.gethostname()
        row = [[
            results["Timestamp"],
            results["MRR"],
            results["Coverage"],
            results["Top-1"],
            results["JW Top-1"],
            server,
            time.strftime("%Y-%m-%d %H:%M:%S")
        ]]
    resource = {
      "majorDimension": "ROWS",
      "values": row
    }
    spreadsheetId = ""
    range = "Uploaded!A:G"

    service.spreadsheets().values().append(
      spreadsheetId=spreadsheetId,
      range=range,
      body=resource,
      valueInputOption="USER_ENTERED"
    ).execute()

if __name__ == "__main__":
    add_score_results(None)
