import json

ruta_json = '/home/devasc/Documents/myfile.json'

with open('/home/devasc/Documents/myfile.json', 'r') as file:
    ourjson = json.load(file)

print(ourjson)

  






