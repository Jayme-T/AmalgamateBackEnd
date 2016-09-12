#!/usr/bin/python
from sht1x.Sht1x import Sht1x
data = 24
clock = 23

#print ">>> mysht1x = Sht1x(%d, %d, Sht1x.GPIO_BCM)" % (data,clock)
mysht1x = Sht1x(data, clock, Sht1x.GPIO_BCM)

#print ">>> mysht1x.read_temperature_C()"
temp = mysht1x.read_temperature_C()
rh = mysht1x.read_humidity()
#print "rh =",rh


dewPoint = mysht1x.calculate_dew_point(temp, rh)
#print "dewpoint=", dewPoint

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

#import requests
#r = requests.post('http://192.168.0.4:3000/piData', data = {'temp':temp, 'dewpoint':dewPoint, 'relative_humidity':rh, 'unique_id':getserial()})
#sfrom flask import Flask, jsonify
#app = Flask(__name__)
#@app.route('http://192.168.0.4:3000/piData', methods=['POST'])
#def test():
#	return jsonify({'task': 'hello'}), 201


