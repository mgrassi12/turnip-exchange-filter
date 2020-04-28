import json
import re

islands_json = 'C:/Users/Mic/Workspaces/TurnipExchangeSorter/islands.json'
minTurnipPrice = 400
maxTurnipPrice = 650
maxPeopleQueued = 20

# Don't touch this unless you know what you're doing. 
with open(islands_json, encoding="utf8") as json_file:
    data = json.load(json_file)
    print('')
    print('============================================================================================================')
    print('============================================================================================================')
    print('============================================================================================================')
    print('========================================T U R N I P   T I M E===============================================')
    print('============================================================================================================')
    print('============================================================================================================')
    print('============================================================================================================')
    print('ISLANDS WITH TURNIP PRICE GREATER THAN ' +  str(minTurnipPrice) + ' BELLS AND LESS THAN ' + str(maxPeopleQueued) + ' PEOPLE WAITING:')
    print('')
    for island in data['JSON']['islands']:
        if (island['turnipPrice'] >= minTurnipPrice) & (island['turnipPrice'] <= maxTurnipPrice):
            queued = re.split("/", island['queued'], 1)[0]
            if int(queued) <= maxPeopleQueued:
                print('Name: ' + str(island['name']))
                print('Turnip Price: ' + str(island['turnipPrice']))
                print('Queued Players: ' + str(island['queued']))
                print('Description: ' + str(island['description']))
                print('Queue Here: ' + 'https://turnip.exchange/island/' + str(island['turnipCode']))
                print('')
                print('')