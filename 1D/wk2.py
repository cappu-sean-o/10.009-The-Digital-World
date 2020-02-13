#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celcius):
    # Read temperature in celcius from the sensor and print it
    print('The temperature in celcius is', round(t_celcius,2))

    # Read temperature in celcius from the sensor, convert to fahrenheit and print it
    print('The temperature in fahrenheit is', round((t_celcius*(9/5)+32),2))
    pass

def forward(speed, duration):
    #Accelerating to given speed in 1 second in 4 steps
    aspeed = speed/4
    robot.wheels(aspeed,aspeed)
    robot.sleep(0.25)
    aspeed += speed/4
    robot.wheels(aspeed,aspeed)
    robot.sleep(0.25)
    aspeed += speed/4
    robot.wheels(aspeed,aspeed)
    robot.sleep(0.25)
    aspeed += speed/4
    robot.wheels(aspeed,aspeed)
    robot.sleep(0.25)
    aspeed += speed/4
    robot.wheels(aspeed,aspeed)
    robot.sleep(duration-1)
    robot.wheels(0,0)
    pass

robot = ThymioReal() # create an object

############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement
spd = int(input('How fast to go?(Enter a number between 0 and 500)'))
dur = float(input('For how long?(in seconds)'))
print('OK')
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('GOOOOOO')

# Move according to the specified speed and duration
forward(spd,dur)

# Read temperature Sensor and print temperature in celcius and fahrenheit
print_temp(robot.read_temperature())

########################## end ############################## 

robot.quit() # disconnect the communication

