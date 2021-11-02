#!/usr/bin/python37all
import cgi
import json
import cgitb
from urllib.request import urlopen 
from urllib.parse import urlencode 
import random, time

cgitb.enable()

data = cgi.FieldStorage() #holds values form HTML

s = data.getvalue("slider1") #input values from html
m = data.getvalue("mode") 

data = {"slider1":s, "mode":m} #dictinary used for data parsing

file = open('angle.txt', 'w+') 


with open('angle.txt', 'w') as f:
  json.dump(data,f)

if m != "Zero Motor":
  api = "2VPFIZ7ZXY6EUC2O" # Enter your API key
  params = {1: int(s),
  "api_key":api}
  params = urlencode(params) # reformat dictionary as a GET string
  url = "https://api.thingspeak.com/update?" + params
  response = urlopen(url)

  time.sleep(15.1) 
elif m == "Zero Motor":
  a = 0
  api = "2VPFIZ7ZXY6EUC2O" # Enter your API key
  params = {1: int(a),
  "api_key":api}
  params = urlencode(params) # reformat dictionary as a GET string
  url = "https://api.thingspeak.com/update?" + params
  response = urlopen(url)

  time.sleep(15.1)


#This part of the code is meant to make a dynamic website
print("Content-type: text/html\n\n")
print('<html>')
print('<head>')
print('<title> LAB 4 - LED SWITCH </title>')
print('</head>')
print('<body>')
print('<div style="width:600px;background:#FFFFFF;border:1px;text-align:center"> <br>')

print('<form action="/cgi-bin/steppercgi3.py" method="POST">')

print('Angle:<br>')
print('<input type="range" name="slider1" min ="0" max="360" value ="0"/><br>')
print('Range is from 0 to 360<br>')
print('<br>')
print('<input type="submit" name = "mode" value="Submit Angle">')
print('<input type="submit" name = "mode" value="Zero Motor"> <br>')
print('<br>')
print('Motor Angle<br>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550380/widgets/372919"></iframe> <br>')
print('<br>')
print('Motor Angle vs. Time<br>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550380/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>')
print('</body>')
print('</form>')
print('</div>')
print('</html>')