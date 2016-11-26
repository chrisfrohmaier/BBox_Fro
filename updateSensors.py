#!/usr/bin/python
__author__ = "Chris Frohmaier"
__email__ = "c.frohmaier2soton.ac.uk"
__status__ = "In development"
__date__ = "November 2016"

import RPi.GPIO as GPIO # always needed with RPi.GPIO
from BMP085 import BMP085
from TMP007 import TMP007
import _mysql

db = _mysql.connect(host='localhost', user='pi', passwd='raspberry', db='bbox')

cur.execute("INSERT INTO sensors(irtemp,dietemp,voltage,ambtemp,pressure) VALUES(%s,%s,%s,%s,%s)",(float(tmp.readObjTempC()),float(tmp.readDieTempC()),float(tmp.readVoltage()),float(bmp.read_temperature()),float(bmp.read_pressure()),float(bmp.read_altitude())))
