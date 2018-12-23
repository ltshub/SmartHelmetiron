from flask import Flask, render_template
#import requests

test = Flask(__name__)

#url = "http://203.250.148.89:7579/Mobius/ironmouse/gps/latest"
#payload = ""
#headers = {
#    'Accept': "application/json",
#    'X-M2M-RI': "12345",
#    'X-M2M-Origin': "SOrigin",
#   'cache-control': "no-cache",
#    'Postman-Token': "5185f594-f384-4e9c-89d4-a249e8ed6b36"
#    }
#response = requests.request("GET", url, data=payload, headers=headers)
#print(response.text)


@test.route('/')
def test_run():
    return render_template('index.html')

if __name__ == '__main__':
    test.run()