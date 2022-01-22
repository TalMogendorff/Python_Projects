import pywhatkit
import requests
import json
import time
import datetime
import schedule


def job():

    now = datetime.datetime.now()

    r = requests.get('https://api.chucknorris.io/jokes/random')
    a = json.loads(r.text)

    pywhatkit.sendwhatmsg("+972543117141",f"Hi This is a Chuck Noris Joke: {a['value']}",now.hour,now.minute+1)

job()
schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

