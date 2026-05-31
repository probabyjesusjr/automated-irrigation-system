# Automated plant waterer - main program
# Runs automatically on boot. Reads soil moisture and waters when dry.

from machine import ADC, Pin
import time

soil = ADC(Pin(26))          # capacitive moisture sensor on GP26
relay = Pin(22, Pin.OUT)     # relay control on GP22
relay.value(1)               # relay OFF to start (this board is active-low)

while True:
    reading = soil.read_u16()        # 0-65535; higher = drier
    print(reading)
    if reading > 37000:              # 37000 = my calibrated dry threshold
        print("DRY - watering")
        relay.value(0)               # pump ON
        time.sleep(0.1)              # pump pulse length (tune to taste)
        relay.value(1)               # pump OFF
    time.sleep(3600)                 # wait an hour, then check again
