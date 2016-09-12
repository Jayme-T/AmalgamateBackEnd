
import json
import requests
from relay import relay
from flask import Flask
from water import water
from turn import turn


app = Flask(__name__)

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

#@app.route('/', methods=['POST'])
#def posts ():
#   relay()
#   return "finished"
@app.route('/water', methods=['POST'])
def watering ():
   water()
   return "finished water"
@app.route('/turn', methods=['POST'])
def turning ():
   turn()
   return "finished turn"
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


