# Calibration helper - prints raw sensor readings once a second.
# Hold the sensor in air to read your "dry" number, then dip it in
# water (up to the line) for your "wet" number. Your threshold is
# roughly the midpoint between them.

from machine import ADC, Pin
import time

soil = ADC(Pin(26))

while True:
    print(soil.read_u16())
    time.sleep(1)
