import urllib3
import os
import json
 
def sendReminder(url, daysUnread):
    http = urllib3.PoolManager()
    requestHeader = {"Accept": "text/plain"}
    requestParam = { 'daysUnread':daysUnread}
    response = http.request('POST', url, headers=requestHeader, fields=requestParam)
    print(daysUnread, response.status, response.geturl())
    print(response.data)
   
def sendUnreadReminders(event, context):
    url = os.environ['url']
    firstReminder = os.environ['firstReminder']
    secondReminder = os.environ['secondReminder']
   
    sendReminder(url, firstReminder)
    sendReminder(url, secondReminder)
   
    print( url, firstReminder, secondReminder)
    return {
        'statusCode': 200,
        'body': json.dumps(event['firstReminder'])
    }
 