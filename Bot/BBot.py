from __future__ import print_function
import httplib2

import datetime
import time
import config
import telepot
import schedule

from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

def job():
    print("I'm working...")
    bot = telepot.Bot(config.TOKEN)

    def main():
        credentials = ServiceAccountCredentials.from_json_keyfile_name(config.client_secret_calendar, 'https://www.googleapis.com/auth/calendar.readonly')
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.datetime.utcnow().isoformat() + '6' # 'Z' indicates UTC time
        now_1day = round(time.time())+86400 #плюс сутки
        now_1day = datetime.datetime.fromtimestamp(now_1day).isoformat() + '6'

        print('Берем 100 событий')
        eventsResult = service.events().list(
            calendarId='271864325465-p7r7btffnam51d47qs035lkoprrv0q7m.apps.googleusercontent.com', timeMin=now, timeMax=now_1day, maxResults=100, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
            print('нет событий на ближайшие сутки')
            bot.sendMessage(683179953, 'нет событий на ближайшие сутки')
        else:
            msg = '<b>События на ближайшие сутки:</b>\n'
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start,' ', event['summary'])
                if not event['description']:
                    print('нет описания')
                    ev_desc = 'нет описания'
                else:
                    print(event['description'])
                    ev_desc = event['description']

                ev_title = event['summary']
                cal_link = '<a href="/%s">Подробнее...</a>'%event['htmlLink']
                ev_start = event['start'].get('dateTime')
                print (cal_link)
                msg = msg+'%s\n%s\n%s\n%s\n\n'%(ev_title, ev_start, ev_desc, cal_link)
                print('===================================================================')
            bot.sendMessage(683179953, msg, parse_mode='HTML')


    if __name__ == '__main__':
        main()

print('Listening ...')
#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("15:29").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
