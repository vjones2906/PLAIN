import board
import busio
import digitalio
import adafruit_mpu6050
import pwmio
from adafruit_motor import motor
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull
from time import sleep, monotonic                      #importing libraries

led = digitalio.DigitalInOut(board.GP1)                #telling the pico that there is something on pin 0
led.direction = digitalio.Direction.OUTPUT             #declaring  led as an output in pin 0

ledBoard = digitalio.DigitalInOut(board.LED)        
ledBoard.direction = digitalio.Direction.OUTPUT        #declaring onboard led

sda_pin = board.GP14                                   #defining sda pin
scl_pin = board.GP15                                   #defining the scl pin
i2c = busio.I2C(scl_pin, sda_pin)                      #creating the i2c from the pins
mpu = adafruit_mpu6050.MPU6050(i2c)

ll = digitalio.DigitalInOut(board.GP2)                 #mapping controller buttons to inputs
ll.direction = digitalio.Direction.INPUT
ll.pull = digitalio.Pull.UP 

lr = digitalio.DigitalInOut(board.GP3)
lr.direction = digitalio.Direction.INPUT
lr.pull = digitalio.Pull.UP     

ld = digitalio.DigitalInOut(board.GP4)
ld.direction = digitalio.Direction.INPUT
ld.pull = digitalio.Pull.UP 

rl = digitalio.DigitalInOut(board.GP7)
rl.direction = digitalio.Direction.INPUT
rl.pull = digitalio.Pull.UP 

rr = digitalio.DigitalInOut(board.GP6)
rr.direction = digitalio.Direction.INPUT
rr.pull = digitalio.Pull.UP 

motPWM = pwmio.PWMOut(board.GP12)                      #telling pico there will be a motor output on pin 12 
motPWM.duty_cycle = 2 ** 15 

sleep(1)

val=50
count = 0
start=0                                                #setting up variables 

with open("/data.csv", "w") as datalog:                #write to this file
#while True:
    while True:                       
        if start==1:                                   #if start is activated, start recording data
            count+=1
            print(count)
            if count == 10:
                datalog.write(f"{monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]},{val}\n")  #writing acceleration data
                datalog.flush()
                count = 0
                print('wrote')
                print(f"{monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]}\n")
        if rr.value == False:                          #activate start
            start = 1
        if rl.value == False:                          #deactivate start
            start = 0
        if ll.value == False:                          #increase throttle
            if val < 99:
                print(val, 'increase')
                val += 1
                sleep(.05)
                dval = int(val)*65535/100
                motPWM.duty_cycle = int(dval)   
            else: sleep(0.05)
        elif lr.value == False:                        #decrease throttle
            if val > 50:
                val = val - .75
                print(val, 'decrease')
                sleep(.05)
                dval = int(val)*65535/100
                motPWM.duty_cycle = int(dval)
            else: sleep(0.05)
        elif ld.value == False:                        #kill switch 
            print('reset')
            val=50
            dval = int(val)*65535/100
            motPWM.duty_cycle = int(dval)
            sleep(.05)                
        else:
            sleep(.05)
