# v1 — Single Plant

The first working version of the automated plant waterer: **one plant**, a Raspberry Pi Pico W, one soil moisture sensor, and a relay-driven pump. This is the version that's built and running today.

![Build photo](photos/IMG_4742%20Small.jpeg)

## What it does

- Reads soil moisture once an hour
- If the soil is dry (past a calibrated threshold), runs the pump for a short pulse
- Otherwise waits and checks again on the next cycle
- Runs standalone off a USB power supply — no computer needed once the code is loaded

## Hardware

- Raspberry Pi Pico W (RP2040)
- Capacitive soil moisture sensor (HW-390 / v2.0)
- SONGLE SRD-05VDC-SL-C single-channel relay module (active-low)
- 5V mini submersible pump
- Breadboard + jumper wires
- 5V / 3A USB power supply

## Wiring

| Connection | Pico pin |
|---|---|
| Sensor VCC | 3V3 |
| Sensor GND | GND |
| Sensor signal (AOUT) | GP26 (ADC) |
| Relay VCC | 3V3 |
| Relay GND | GND |
| Relay IN | GP22 |

Pump power runs through the relay's switch contacts: COM to the Pico's 5V (VBUS), NO to the pump's positive lead, and the pump's negative lead to GND.

## The code

Found in [`pico/`](pico/):

- `main.py` — the watering program (runs automatically on boot)
- `calibrate.py` — prints raw sensor readings so you can find your own dry/wet numbers
- `blink.py` — the first "is this thing alive" LED blink test

## Calibration

Measured with `calibrate.py`:

- Dry (sensor in air): ~54,500
- Wet (sensor in water): ~20,000
- Threshold: ~37,000 (the midpoint)

A capacitive sensor reads higher as the soil gets drier, so the pump triggers when the reading climbs above the threshold.

## What I learned (the hard part)

**1. The pump turned on and never stopped.** The relay is a 5V active-low board, but the Pico's GPIO only outputs 3.3V — enough to switch the relay on, but not enough to switch it back off against the 5V coil, so it latched. The fix was moving the relay's VCC from the 5V rail to the Pico's 3V3 pin so the control signal and the coil share a reference. After that it switched cleanly on command — and as a bonus, it now defaults to OFF on any reset.

**2. The pump browning out the Pico.** When the relay closed, the pump's startup current surge collapsed the shared 5V rail and reset the board before the motor could spin. The fix is a large capacitor across the 5V rail to absorb the inrush. *(In progress.)*

## Status

- ✅ Sensor reading, watering logic, and relay control all working
- 🔧 Inrush-brownout capacitor — to be added
