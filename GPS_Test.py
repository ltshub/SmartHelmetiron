#import requests
import time

mobiusAddress = '203.250.148.89:7579'

def updateStatus(temp):


        head = {'accept': 'application/json', 'X-M2M-RI' : '12345', 'Content-Type' : 'application/vnd.onem2m-res+json; ty=4', 'X-M2M-Origin': 'Ironmouse'}
        url = 'http://' + mobiusAddress + '/Mobius/ironmouse/gps'
        payload = { "m2m:cin": { "con": temp} }
        
        responseCode = requests.post(url, json=payload, headers=head)    
        print(responseCode.status_code)
        

print ("Receiving GPS data")
#ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
f= open("C:\\Users\\USER\\Desktop\\오픈소스 3-2\\realsex\\jujak.txt",'r')
str1 = []	
while True:
	line = f.readline()
	if not line: break
	str1.append(line)
f.close()
str2 = []
for i in range(0,149):
	str2.append(str1[i].split(','))
for i in range(0,149):
	str2[i][1] = str2[i][1][0:10]
txtdata = []
for i in range(0,149):
	txtdata.append(','.join(str2[i]))
i = 0
while True:
	#updateStatus(textdata[i%160])
	print(txtdata[i%149])
	i = i+1
	#time.sleep(1)
