from credentials import liamNum
import requests
import schedule
import time









def send_message():
  resp = requests.post('https://textbelt.com/text', {
    'phone': liamNum,
    'message': 'This reminder was sent from a Python script. Clean your teeth, Lil Dude! Text me if you receive this message.',
    'key': 'textbelt'
  })

  print(resp.json())


schedule.every().day.at("17:00").do(send_message)
# schedule.every(10).seconds.do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)