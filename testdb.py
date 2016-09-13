#!/usr/bin/python

import sys,os
import psycopg2 as psql

#conn = psql.connect("dbname=testdb")
#cur = conn.cursor()
#cur.execute("""SELECT table_name FROM information_schema.tablesss
#       WHERE table_schema = 'public'""")
#for table in cur.fetchall():
#   print(table)
   
def data():
   conn = psql.connect("dbname=piData")
   cur = conn.cursor()
   cur.execute("Select * from data") 
   x=cur.fetchone()
   #conn.commit()
   #conn.close()
   print x
#   return x
