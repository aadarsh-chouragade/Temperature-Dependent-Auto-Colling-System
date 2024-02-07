import Rpi.GPIO as GPIO
from time import sleep
import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)
GPIO.setwarning(False)
GPIO.setup(11,GPIO.OUT)
sensore =Adafruit_DHT.AM2302
print('Gettinf data from sensor')
humidity,temperature =Adafruit_DHT.read_rety(sensor,4)
if temperature>20:
    print('Temp>20')
    GPIO.output(FAN,0);
print('Fan on')
sleep(5)
print('Fan off')
GPIO.output(FAN,1)
else :
GPIO.output(FAN,1)
print("Temp below max value");
