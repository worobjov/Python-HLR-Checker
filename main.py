# Python HLR CHECKER Script
# worobjov

# Using TELEGRAM CLIENT API AND SMSC.RU API

from telethon import TelegramClient, events
import time
import requests
import json

api_id = 000000 # TELEGRAM API_ID
api_hash = '0a0a0a00a0a0a0a0a0a0a' # TELEGRAM API_HASH

async def message(rs):
  await client.send_message('<username>', rs.text) # TELEGRAM USERNAME WITHOUT @ TO SEND NOTIFICATION
  return

client = TelegramClient('console', api_id, api_hash) # <console> - NAME OF TELEGRAM CLIENT
client.start()

while True:
  r = requests.get('https://smsc.ru/sys/send.php?login=<USERNAME>&psw=<PASSWORD>&phones=<PHONE>&hlr=1&err=1&fmt=3&status=1')
  j = json.loads(r.text)
  time.sleep(10)
  rs = requests.get(f'https://smsc.ru/sys/status.php?login=<USERNAME>&psw=<PASSWORD>&phone=<PHONE>&id={j["id"]}')
  print(rs.text)
  client.loop.run_until_complete(message(rs))
  time.sleep(900) # SECONDS 
