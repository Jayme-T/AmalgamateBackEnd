#!/usr/bin/python
# -*- coding: utf-8 -*-


import psycopg2 as psql
import sys,os
# import is not currently working
from sensors import getserial;
from sensors import temp;
from sensors import rh;
from sensors import dewPoint;

conn = psql.connect("dbname=piData")
cur = conn.cursor()
cur.execute("INSERT into data (temp, rh, dewpoint, date, serial_id, time) values (%s,%s, %s, now(), %s, CURRENT_TIME)", (temp, rh, dewPoint, getserial()))

conn.commit()

    
conn.close()
