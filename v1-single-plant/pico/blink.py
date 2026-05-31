# First boot test - blinks the Pico W's onboard LED.
# If this blinks, the board is alive and MicroPython is running.

from machine import Pin
import time

led = Pin("LED", Pin.OUT)   # Pico W onboard LED

while True:
    led.toggle()
    time.sleep(0.5)
