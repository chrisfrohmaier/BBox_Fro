#!/usr/bin/python
__author__ = "Chris Frohmaier"
__email__ = "c.frohmaier2soton.ac.uk"
__status__ = "In development"
__date__ = "November 2016"

import RPi.GPIO as GPIO # always needed with RPi.GPIO
from BMP085 import BMP085
from TMP007 import TMP007
import MySQLdb
tmp=TMP007()
bmp=BMP085()
db = MySQLdb.connect(host='localhost', user='pi', passwd='raspberry', db='bbox')
conn=db.cursor()

print 'IR Temp: ', tmp.readObjTempC()
print 'Die Temp: ', tmp.readDieTempC()
print 'Voltage: ', tmp.readVoltage()
print 'Amb Temp: ', bmp.read_temperature()
print 'Pressure: ', bmp.read_pressure()

conn.execute("INSERT INTO sensors(irtemp,dietemp,voltage,ambtemp,pressure) VALUES(%s,%s,%s,%s,%s)",(float(tmp.readObjTempC()),float(tmp.readDieTempC()),float(tmp.readVoltage()),float(bmp.read_temperature()),float(bmp.read_pressure()),float(bmp.read_altitude())))
