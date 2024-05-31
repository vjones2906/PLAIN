import board
import busio
import digitalio
import adafruit_mpu6050
import pwmio
from adafruit_motor import motor
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull
from time import sleep, monotonic

led = digitalio.DigitalInOut(board.GP1)                #telling the pico that there is something on pin 0
led.direction = digitalio.Direction.OUTPUT             #declaring  led as an output in pin 0

ledBoard = digitalio.DigitalInOut(board.LED)        
ledBoard.direction = digitalio.Direction.OUTPUT        #declaring onboard led

sda_pin = board.GP14                                   #defining sda pin
scl_pin = board.GP15                                   #defining the scl pin
i2c = busio.I2C(scl_pin, sda_pin)                      #creating the i2c from the pins
mpu = adafruit_mpu6050.MPU6050(i2c)

ll = digitalio.DigitalInOut(board.GP2)
ll.direction = digitalio.Direction.INPUT
ll.pull = digitalio.Pull.UP 

lr = digitalio.DigitalInOut(board.GP3)
lr.direction = digitalio.Direction.INPUT
lr.pull = digitalio.Pull.UP     

ld = digitalio.DigitalInOut(board.GP4)
ld.direction = digitalio.Direction.INPUT
ld.pull = digitalio.Pull.UP 

lu = digitalio.DigitalInOut(board.GP5)
lu.direction = digitalio.Direction.INPUT
lu.pull = digitalio.Pull.UP

rl = digitalio.DigitalInOut(board.GP7)
rl.direction = digitalio.Direction.INPUT
rl.pull = digitalio.Pull.UP 

rr = digitalio.DigitalInOut(board.GP6)
rr.direction = digitalio.Direction.INPUT
rr.pull = digitalio.Pull.UP 

ru = digitalio.DigitalInOut(board.GP8)
ru.direction = digitalio.Direction.INPUT
ru.pull = digitalio.Pull.UP

rd = digitalio.DigitalInOut(board.GP9)
rd.direction = digitalio.Direction.INPUT
rd.pull = digitalio.Pull.UP 

pwm_servo = pwmio.PWMOut(board.GP10, duty_cycle=2 ** 15, frequency=50)      #tells pin 20 it will control a servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

pwm_servo = pwmio.PWMOut(board.GP11, duty_cycle=2 ** 15, frequency=50)      #tells pin 20 it will control a servo
servo2 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

motPWM = pwmio.PWMOut(board.GP12)
motPWM.duty_cycle = 2 ** 15 

sleep(1)

tilt=0
val=50
lval=0
rval=0
count = 0
start=0 

with open("/data.csv", "w") as datalog:                #write to this file
#while True:
    while True:                       
        if start==1:
            
            count+=1
            print(count)
            if count == 10:
                datalog.write(f"{monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]},{tilt},{val}\n")  #writing acceleration data
                datalog.flush()
                count = 0
                print('wrote')
                print(f"{monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]}\n")
        if rr.value == False:
            start = 1
        if rl.value == False:
            start = 0
        if ll.value == False: 
            if val < 99:
                print(val, 'increase')
                val += 1
                sleep(.05)
                dval = int(val)*65535/100
                motPWM.duty_cycle = int(dval)   
            else: sleep(0.05)
        elif lr.value == False:
            if val > 50:
                val = val - .75
                print(val, 'decrease')
                sleep(.05)
                dval = int(val)*65535/100
                motPWM.duty_cycle = int(dval)
            else: sleep(0.05)
        elif ld.value == False:
            print('reset')
            val=50
            dval = int(val)*65535/100
            motPWM.duty_cycle = int(dval)
            sleep(.05)                
        else:
            sleep(.05)
