#!/usr/bin/python

import sys,os
import psycopg2 as psql

from sensors import gettemp as temp
from sensors import getrh as rh
from sensors import getdewPoint as dewPoint
from sensors import getserial

conn = psql.connect("dbname=piData")
cur = conn.cursor()
cur.execute("INSERT into data (temp, rh, dewpoint, serial_id) VALUES(%s, %s, %s, %s)", (temp(), rh(), dewPoint(temp(), rh()), getserial())) 
conn.commit()
conn.close()
