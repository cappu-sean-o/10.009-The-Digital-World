# Code copied from https://github.com/MarkHershey/DW2020/blob/master/W3/mini1D/wk3_template.py with permission from MarkHershey
# Annotations by me
# You are free to use this however you like, unless for malicious intents

# Further Readings
# https://www.raspberrypi.org/documentation/usage/gpio/
# https://www.raspberrypi.org/documentation/hardware/raspberrypi/gpio/README.md

# <----------------------------------------------------- Code Begins Here ----------------------------------------------------------->
import RPi.GPIO as GPIO                 # Import Raspberry Pi GPIO python library for controlling GPIO pins

from time import sleep                  # Import time python library

GPIO.setmode(GPIO.BCM)                  # Use the BCM GPIO numbers as the numbering scheme

led = [23, 24]                          # Store the pin number of the GPIO pins connected to the LEDs in a list (pins 23 and 24)

switch = 18                             # Store the pin number of the GPIO pin connected to the switch in this variable (pins 18)

GPIO.setup(led, GPIO.OUT)               # Set up the GPIO pins defined in line 8 (23 and 24) as output pins

GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)  # Set the GPIO18 as input with a pull-down resistor 
                                            # This prevents the processor from being destroyed by high current due to a short circuit


def blink(gpio_number, duration):       # This function takes in two input: gpio_number and duration. The
                                        # gpio_number specifies the GPIO number which the LED (to be blinked) is
                                        #connected to. The duration is the blink interval in seconds.
    
    GPIO.output(gpio_number, GPIO.HIGH) # Sets the GPIO pin with pin number "gpio_number" to HIGH state (outputs +3.3V)

    sleep(duration)                     # Stops execution of code for "duration" number of seconds

    GPIO.output(gpio_number, GPIO.LOW)  # Sets the GPIO pin with pin number "gpio_number" to LOW state (outputs 0V)
    
    sleep(duration)                     # Stops execution of code for "duration" number of seconds
                                        # This has the effect of blinking by turning the LED on , waiting for the duration,
    return                              # turning the LED off and waiting for the duration again before looping


while True:                             # Check whether the switch is closed or opened. When the switch is closed,
                                        # turn off the LED at GPIO24 and blink the LED at GPIO23. When the switch
                                        # is opened, turn off the LED at GPIO23 and blink the LED at GPIO24. The
                                        # blink interval should be 1 second.

    if GPIO.input(switch) == GPIO.HIGH: # Check if there is a signal received on the GPIO pin defined by "switch", HIGH is +3.3V, LOW is no signal

        GPIO.output(led[1], GPIO.LOW)   # If true, turn off LED on GPIO 23,

        blink(led[0], 1)                # and blink LED on GPIO 24
    else:

        GPIO.output(led[0], GPIO.LOW)   # If false, turn off LED on GPIO 24,

        blink(led[1], 1)                # and blink LED on GPIO 23