import requests

mobiusAddress = '203.250.148.89:7579'

payload = {"m2m:cin": { "con": 'Action'}}

url = 'http://' + mobiusAddress + '/Mobius/ironmouse/gyro'

head = {
    'Accept': "application/json",
    'X-M2M-RI': "12345",
    'Content-Type': "application/vnd.onem2m-res+json; ty=4",
    'X-M2M-Origin': "{{aei}}"
    }
#'cache-control': "no-cache"
#'Postman-Token': "ea98743a-3483-4789-8e68-a78e47c01a87"
responseCode = requests.post(url, json=payload, headers=head)
print(responseCode.status_code)
