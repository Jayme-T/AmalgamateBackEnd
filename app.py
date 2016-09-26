import sys,os
import psycopg2 as psql
import json
import requests
from relay import relay
from flask import Flask
from water import water
from turn import turn
from flask import jsonify
from sensors import getserial
from flask import request
from mycronfile import schedulingaturn
from mycronfile import schedulingawater
import json

app = Flask(__name__)
from flask.ext.bcrypt import Bcrypt
bcrypt=Bcrypt(app)
@app.route('/test', methods=['GET'])
def index():
    return "test"

@app.route('/')
def test():
    from sht1x.Sht1x import Sht1x
    data = 24
    clock = 23

    #print ">>> mysht1x = Sht1x(%d, %d, Sht1x.GPIO_BCM)" % (data,clock)
    mysht1x = Sht1x(data, clock, Sht1x.GPIO_BCM)

    #print ">>> mysht1x.read_temperature_C()"
    temp = mysht1x.read_temperature_C()
    # print "temp", temp

    rh = mysht1x.read_humidity()
    #print "rh =",rh


    dewPoint = mysht1x.calculate_dew_point(temp, rh)
    #print "dewpoint=", dewPoint


    pidata={"temp": temp, "humidity": rh, "dewPoint":dewPoint}
    conv = [pidata]
    s_data = json.dumps(conv)

    return s_data

@app.route('/water', methods=['POST'])
def watering ():
   water()
   return "finished water"
@app.route('/turn', methods=['POST'])
def turning ():
   turn()
   #return "finished turn"
   #from sht1x.Sht1x import Sht1x
   #data = 24
   #clock = 23

    #print ">>> mysht1x = Sht1x(%d, %d, Sht1x.GPIO_BCM)" % (data,clock)
   #mysht1x = Sht1x(data, clock, Sht1x.GPIO_BCM)

    #print ">>> mysht1x.read_temperature_C()"
   #temp = mysht1x.read_temperature_C()
    # print "temp", temp

   #rh = mysht1x.read_humidity()
    #print "rh =",rh


   #dewPoint = mysht1x.calculate_dew_point(temp, rh)
    #print "dewpoint=", dewPoint


   #pidata={"temp": temp, "humidity": rh, "dewPoint":dewPoint}
   #conv = [pidata]
   #s_data = json.dumps(conv)

   return "finished turn"

@app.route('/data', methods=['GET'])
def data():
   conn = psql.connect("dbname=piData")
   cur = conn.cursor()
   cur.execute("Select * from data")
   #r = [dict((cur.description[i][0], value) \
   #            for i, value in enumerate(row)) for row in cur.fetchall()]
   #conn.close()
   #return jsonify(**r[0])
   x= dict([("data", cur.fetchall())])
   conn.close()
   return jsonify(x)

@app.route('/watersched', methods=['POST'])
def waterschedule():
 
   parsed_json = json.loads(request.data)
   #print "1", request.data
   #print "2", parsed_json['m']
   mins= parsed_json['min']
   hours=parsed_json['hours']
   dom=parsed_json['dom']
   print "dom", dom
   m=parsed_json['m']
   dow=parsed_json['dow']
   #print request.data
   schedulingawater(mins, hours, dom, m, dow);
   return "did it!"
@app.route('/turnsched', methods=['POST'])
def turnschedule():
 
   parsed_json = json.loads(request.data)
   #print "1", request.data
   #print "2", parsed_json['m']
   mins= parsed_json['min']
   hours=parsed_json['hours']
   dom=parsed_json['dom']
   m=parsed_json['m']
   dow=parsed_json['dow']
   #print request.data
   schedulingaturn(mins, hours, dom, m, dow);
   return "did it!"   
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
