import requests
# IFTTT URL for Logging to Google Sheets
IFTTT_URL_GoogleSheets = 'https://maker.ifttt.com/trigger/hello/with/key/'
# IFTTT Key
IFTTT_KEY = 'XTc0xn_SgM2NwLYRRQWjv'

# Log
requests.post(IFTTT_URL_GoogleSheets + IFTTT_KEY, json = {'value1':'foo', 'value2':'var', 'value3':'parameter3'})
print IFTTT_URL_GoogleSheets + IFTTT_KEY
