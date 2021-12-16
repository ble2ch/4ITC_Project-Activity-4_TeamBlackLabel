import requests
from cred import *
import json

def getRoom(num):
    url = 'https://webexapis.com/v1/rooms'
    headers = {
        'Authorization': 'Bearer {}'.format("MjUyNzdlYzYtYmViYy00MDhiLWE2YjItNDRmMmRjYzU4ZTA0YzgyZmJlYmEtNmM4_P0A1_9282fec5-949a-498f-b4a3-03239519286e"),
        'Content-Type': 'application/json'
    }
    params={'max': '100'}
    #* Get Rooms
    res = requests.get(url, headers=headers, params=params)

    #* Convert to string
    res2 = json.dumps(res.json(), indent=4)

    #* Convert to dictionary
    rooms = json.loads(res2)

    #* Get Room IDs
    Roomid = rooms['items'][num]['id']
    print("This is the room ", rooms['items'][num]['title'])
    return Roomid