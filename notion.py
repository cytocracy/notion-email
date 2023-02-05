import os
from notion_client import Client

import json
import datetime
# import sync
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("NOTION_DATABASE")
token = os.getenv("NOTION_TOKEN")

notion = Client(auth=token)

TOMORROW = True

def get_message():
    return "Here is the rehearsal call for today!\n\n" + '<font="Courier">' + get_call() + '</font>'





def get_call():
    #get iso 8601 date for tomorrow
    tomorrow = datetime.date.today()
    if TOMORROW:
        tomorrow += datetime.timedelta(days=1)
    

    response = notion.databases.query(
        database_id=database,
        filter={
            "property": "Date",
            "date": {
                "equals": tomorrow.isoformat()
            }
        }
    )
    if len(response["results"]) == 0:
        raise Exception("no call")
    # print (response[0]["properties"]["Name"]["title"][0]["plain_text"])
    for i in response["results"]:

        info = "Rehearsal: "
        name = i['properties']['Name']["title"]
        
        
        if len(name) != 0:
            name = name[0]["plain_text"]
            info += name
        info += '\nDate: '
        

        date = i['properties']['Date']['date']['start']
        date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y')
        info += date + '\nCalled: '
        called = i['properties']['Called']['rich_text']
        if len(called) != 0:
            called = called[0]['plain_text']
            info += called
        info += '\nTime: '

        time = i['properties']['Time']['rich_text']
        if len(time) != 0:
            time = time[0]['plain_text']
            info += time
        info += '\nNotes: '

        notes = i['properties']['Notes']['rich_text']
        if len(notes) != 0:
            notes = notes[0]['plain_text']
            info += notes
        info += '\n'

        return info
        
        
print(get_call())
