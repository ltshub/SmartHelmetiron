import requests
import serial
import time

# ip Address of PC running Mobius server.
mobiusAddress = '203.250.148.89:7579'
port = "/dev/ttyAMA0"

def parseGPS(data):
#    print "raw:", data #prints raw data
    if data[0:6] == "$GPRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print "no satellite data available"
            return
        print "---Parsing GPRMC---",
        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        lat = decode(sdata[3]) #latitude
        dirLat = sdata[4]      #latitude direction N/S
        lon = decode(sdata[5]) #longitute
        dirLon = sdata[6]      #longitude direction E/W
        speed = sdata[7]       #Speed in knots
        trCourse = sdata[8]    #True course
        date = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]#date
        print "time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s, True Course : %s, Date : %s" %  (time,lat,dirLat,lon,dirLon,speed,trCourse,date)
	return (lat+","+lon)

def decode(coord):
    #Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    nanoP = tail[0:4]
    return deg + "." + min + nanoP

def updateStatus(temp):


        head = {'accept': 'application/json', 'X-M2M-RI' : '12345', 'Content-Type' : 'application/vnd.onem2m-res+json; ty=4', 'X-M2M-Origin': 'Ironmouse'}
        url = 'http://' + mobiusAddress + '/Mobius/ironmouse/gps'
        payload = { "m2m:cin": { "con": temp} }
        
        responseCode = requests.post(url, json=payload, headers=head)    
        print(responseCode.status_code)
        

print "Receiving GPS data"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
f= open("GPS_log.txt",'a')
while True:
    k = 0
    time.sleep(1)
    data = ser.readline()
    result=parseGPS(data)
    if (str(result) == "None"):
        continue
    else:
        f.write(str(result) + "\n")
        updateStatus(result)
        k = k+1
    if(k==1000):
        f.close()
        break
    
