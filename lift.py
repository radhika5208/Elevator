#import Adafruit_BBIO.GPIO as g
import sys
import time as t
dp=0
max1=5

def upward(dp,tp):
   for i in range(tp+1):
      pin="P9_"+str(11+dp+i)
      print "Floor No: "+str(dp+i)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.HIGH)
      t.sleep(1)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.LOW)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.HIGH)
   print "Reached To Floor"
   t.sleep(3)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.LOW)
def downword(dp,tp):
   for i in range(tp+1):
      pin="P9_"+str(11+dp-i)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.HIGH)
      print "Floor No: "+str(dp-i)
      t.sleep(1)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.LOW)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.HIGH)
   print "Reached To Floor"
   t.sleep(3)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.LOW)

