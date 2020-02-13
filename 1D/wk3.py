# Code copied from 
# https://github.com/MarkHershey/DW2020/blob/master/W3/mini1D/wk3_template.py 
# with permission from MarkHershey

# Annotations by me
# You are free to use this however you like, unless for malicious intents

# Further Readings
# https://www.raspberrypi.org/documentation/usage/gpio/

# <------------------------ Code Begins Here -------------------------->
# Import Raspberry Pi GPIO python library for controlling GPIO pins
import RPi.GPIO as GPIO

# Import time python library
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Store the pin number of the GPIO pins connected to the LEDs in a list
led = [23, 24]

# Store the pin number of the GPIO pin connected to the switch in this
# variable (pins 18)
switch = 18

# Set up the GPIO pins defined in line 8 (23 and 24) as output pins
GPIO.setup(led, GPIO.OUT)

# Set the GPIO18 as input with a pull-down resistor 
# This prevents the processor from being destroyed by high current
# due to a short circuit
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)


# This function takes in two input: gpio_number and duration. The
# gpio_number specifies the GPIO number which the LED (to be blinked)
# is connected to. The duration is the blink interval in seconds.
def blink(gpio_number, duration):       
    
    # Sets the GPIO pin with pin number "gpio_number" to
    # HIGH state (outputs +3.3V)
    GPIO.output(gpio_number, GPIO.HIGH)

    # Stops execution of code for "duration" number of seconds
    sleep(duration)

    # Sets the GPIO pin with pin number "gpio_number" to
    # LOW state (outputs 0V)
    GPIO.output(gpio_number, GPIO.LOW)
    
    # Stops execution of code for "duration" number of seconds
    sleep(duration)

    # This has the effect of blinking by turning the LED on , waiting
    # for the duration, turning the LED off and waiting for the duration
    # again before looping

    return                              

# Check whether the switch is closed or opened. When the switch is closed,
# turn off the LED at GPIO24 and blink the LED at GPIO23. When the switch
# is opened, turn off the LED at GPIO23 and blink the LED at GPIO24. The
# blink interval should be 1 second.
while True:

    # Check if there is a signal received on the GPIO pin defined by 
    # "switch", HIGH is +3.3V, LOW is no signal
    if GPIO.input(switch) == GPIO.HIGH:

        # If true, turn off LED on GPIO 23,
        GPIO.output(led[1], GPIO.LOW)

        # and blink LED on GPIO 24
        blink(led[0], 1)
    else:

        # If false, turn off LED on GPIO 24,
        GPIO.output(led[0], GPIO.LOW)

        # and blink LED on GPIO 23
        blink(led[1], 1)