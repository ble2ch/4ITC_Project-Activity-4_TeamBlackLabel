import requests
import json

#Authenticate User Token
def Auth():
    user = []
    url = 'https://webexapis.com/v1/people/me'
    headers = {
        'Authorization': 'Bearer {}'.format("MjUyNzdlYzYtYmViYy00MDhiLWE2YjItNDRmMmRjYzU4ZTA0YzgyZmJlYmEtNmM4_P0A1_9282fec5-949a-498f-b4a3-03239519286e")
    }
    #* Get User Info
    res = requests.get(url, headers=headers)
    #* Convert to string
    res2 = json.dumps(res.json(), indent=4)
    #* Convert to dictionary
    data = json.loads(res2)

    print("Hello User!")

#Get Rooms
# def GetRooms(number):
#     url = 'https://webexapis.com/v1/rooms'
#     headers = {
#         'Authorization': 'Bearer {}'.format("MTAyMThlZDYtODU2OS00MGE3LWI3YjEtMjc5ZDc1ZjczZTBmNWMyZDQ3YWQtMTA3_P0A1_9282fec5-949a-498f-b4a3-03239519286e"),
#         'Content-Type': 'application/json'
#     }
#     params={'max': '100'}
#     #* Get Rooms
#     res = requests.get(url, headers=headers, params=params)

#     #* Convert to string
#     res2 = json.dumps(res.json(), indent=4)

#     #* Convert to dictionary
#     rooms = json.loads(res2)

#     #* Get Room IDs
#     Roomid = rooms['items'][number]['id']
#     print("This is the room ", rooms['items'][number]['title'])
#     return Roomid

#Send Message to Teams
def SendMsg(room_id,message):
    url = 'https://webexapis.com/v1/messages'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

def GetRooms():
    url = 'https://webexapis.com/v1/rooms'
    headers = {
        'Authorization': 'Bearer {}'.format("MjUyNzdlYzYtYmViYy00MDhiLWE2YjItNDRmMmRjYzU4ZTA0YzgyZmJlYmEtNmM4_P0A1_9282fec5-949a-498f-b4a3-03239519286e"),
        'Content-Type': 'application/json'
    }
    params={'max': '100'}
    #* Get Rooms
    res = requests.get(url, headers=headers, params=params)
    print(res.json())