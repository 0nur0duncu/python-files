#python standart libraries (json module)
#----------------------------------------

import json as js

user = {"informations":[{"name":"a","surname":"b","idNumber":123456789},{"name":"c","surname":"v","idNumber":222222222}
,{"name":"e","surname":"f","idNumber":111111111}]}

val_json = js.dumps(user,ensure_ascii=False) #or conv_json = js.dumps(user)
print(val_json) #{"informations": [{"name": "a", "surname": "b", "idNumber": 123456789}, {"name": "c", "surname": "v", "idNumber": 222222222}, {"name": "e", "surname": "f", "idNumber": 111111111}]}
user ='{"informations": [{"name": "a", "surname": "b", "idNumber": 123456789}, {"name": "c", "surname": "v", "idNumber": 222222222}, {"name": "e", "surname": "f", "idNumber": 111111111}]}'
conv_json = js.loads(user)
print(conv_json) #{"informations": [{"name": "a", "surname": "b", "idNumber": 123456789}, {"name": "c", "surname": "v", "idNumber": 222222222}, {"name": "e", "surname": "f", "idNumber": 111111111}]}

print(conv_json['informations']) #[{'name': 'a', 'surname': 'b', 'idNumber': 123456789}, {'name': 'c', 'surname': 'v', 'idNumber': 222222222}, {'name': 'e', 'surname': 'f', 'idNumber': 111111111}]

print(conv_json['informations'][0]['name']) #a