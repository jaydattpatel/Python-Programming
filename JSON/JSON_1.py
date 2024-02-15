'''
author : Jaydatt


'''

import json

# program to read data from json file
file = open("JsonSample.txt", 'r')
string_data = file.read()
file.close()

res = json.loads(string_data) # convert json string data to list directory
print(type(res))



# program to get tweet author or user and created time
# print("------------Method-1------------")
# res2 = res['statuses']
# for res3 in res2:
#    res4 = res3['user']
#    print(res4['screen_name'], res4['created_at'])

# print("------------Method-2------------")
# for res3 in res['statuses']:
#     print(res3['user']['screen_name'], res3['user']['created_at'])
