# coding: utf-8

import json

### Amaozn Connectの戻り値
event = {'Details': {'ContactData': {'Attributes': {}, 'Channel': 'VOICE', 'ContactId': '1f111111-11f1-1111-1a1c-1c1c1f111111', 'CustomerEndpoint': {'Address': '+815012345678', 'Type': 'TELEPHONE_NUMBER'}, 'InitialContactId': '1f111111-11f1-1111-1a1c-1c1c1f111111', 'InitiationMethod': 'INBOUND', 'InstanceARN': 'arn:aws:connect:ap-northeast-1:12345678910:instance/1111a111-11f1-1fb1-1c11-1a11a1111111', 'MediaStreams': {'Customer': {'Audio': None}}, 'PreviousContactId': '1f111111-11f1-1111-1a1c-1c1c1f111111', 'Queue': None, 'SystemEndpoint': {'Address': '+815012345678', 'Type': 'TELEPHONE_NUMBER'}}, 'Parameters': {}}, 'Name': 'ContactFlowEvent'}

def main():
    #f = open('output.json', 'w')
    #json.dump(event, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    print(event.keys)
    for i in event.keys():
        print(i)
    
    print('===')
    for j in event['Details']['ContactData']['CustomerEndpoint']['Address']:
        print(j)

    data = event['Details']['ContactData']['CustomerEndpoint']['Address']
    print(data)
        

if __name__ == '__main__': main()
