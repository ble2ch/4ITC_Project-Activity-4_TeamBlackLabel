#*change to webexteam
from webexteam import *
import json
import requests
#Send update for Team L1 and Team L2
def updateNotif(roomnumber,roomnumber2,msg):
    #Auth("MTAyMThlZDYtODU2OS00MGE3LWI3YjEtMjc5ZDc1ZjczZTBmNWMyZDQ3YWQtMTA3_P0A1_9282fec5-949a-498f-b4a3-03239519286e")

    url = 'https://webexapis.com/v1/rooms'
    headers = {
        'Authorization': 'Bearer {}'.format("MjUyNzdlYzYtYmViYy00MDhiLWE2YjItNDRmMmRjYzU4ZTA0YzgyZmJlYmEtNmM4_P0A1_9282fec5-949a-498f-b4a3-03239519286e"),
        'Content-Type': 'application/json'
    }
    params={'max': '100'}
    # Get Rooms
    res = requests.get(url, headers=headers, params=params)

    #* Convert to string
    res2 = json.dumps(res.json(), indent=4)

    #* Convert to dictionary
    rooms = json.loads(res2)

    #* Get Room IDs
    Roomid = rooms['items'][roomnumber]['id']
    print("This is the room ", rooms['items'][roomnumber]['title'])

    Roomid2 = rooms['items'][roomnumber2]['id']
    print("This is the room ", rooms['items'][roomnumber2]['title'])
    # return Roomid

    #L1id = GetRooms(1)

    #print("Room ID:",L1id)

    # SendMsg(L1id,f"{msg} This is an automated message for Team L1")
    # SendMsg(L2id,f"{msg} This is an automated message for Team L2")
    #Auth
    url2 = 'https://webexapis.com/v1/messages'
    headers2 = {
    'Authorization': 'Bearer {}'.format("MjUyNzdlYzYtYmViYy00MDhiLWE2YjItNDRmMmRjYzU4ZTA0YzgyZmJlYmEtNmM4_P0A1_9282fec5-949a-498f-b4a3-03239519286e"),
    'Content-Type': 'application/json'
    }
    params2 = {'roomId': Roomid, 'markdown': msg}
    res3 = requests.post(url2, headers=headers2, json=params2)
    print(res3.json())

    params3 = {'roomId': Roomid2, 'markdown': msg}
    res4 = requests.post(url2, headers=headers2, json=params3)
    print(res4.json())

