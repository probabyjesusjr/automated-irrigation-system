# Pico Plant Waterer 🌱

An automated plant-watering system built on a Raspberry Pi Pico W. It reads soil moisture with a capacitive sensor and, when the soil is dry, switches on a small submersible pump through a relay to water the plant — then checks again on a timer. This was my first electronics + embedded programming project.

## What it does
- Reads soil moisture once an hour
- If the soil is dry (past a calibrated threshold), runs the pump for a short pulse
- Otherwise does nothing and waits for the next check
- Runs standalone off a USB power supply — no computer needed once it's loaded

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

Pump power runs through the relay's switch contacts: **COM** to the Pico's 5V (VBUS), **NO** to the pump's positive lead, and the pump's negative lead to GND.

## The code
- `main.py` — the watering program (runs automatically on boot)
- `calibrate.py` — prints raw sensor readings so you can find your own dry/wet numbers
- `blink.py` — the very first "is this thing alive" LED blink test

### Calibration
Using `calibrate.py` I measured:
- **Dry** (sensor in air): ~54,500
- **Wet** (sensor in water): ~20,000
- **Threshold**: ~37,000 (the midpoint)

A capacitive sensor reads *higher* as the soil gets *drier*, so the pump triggers when the reading climbs above 37,000.

## What I learned (the hard part)
It worked on paper but fought me in two memorable ways:

**1. The pump would turn on and never stop.** The relay is a 5V active-low board, but the Pico's GPIO only outputs 3.3V. That was enough to switch the relay *on* but not enough to switch it back *off* against the 5V coil — so the relay latched and the pump ran forever. The fix was a logic-level match: I moved the relay's VCC from the 5V rail to the Pico's 3V3 pin so the control signal and the coil share a reference. After that the relay turned on and off exactly on command — and as a bonus, it now defaults to OFF on any reset, so a glitch can't leave the pump running.

**2. The pump browning out the Pico.** The moment the relay closed, the pump's startup current surge collapsed the shared 5V rail and reset the microcontroller before the motor could even spin. I caught it live in the serial output: the reading printed, `DRY - watering` printed, the relay clicked — then the board disconnected. The fix is a large capacitor across the 5V rail to absorb that inrush. *(In progress.)*

## Status
- ✅ Sensor reading, watering logic, and relay control all working
- 🔧 Inrush-brownout capacitor — to be added
- 🔭 Future: log readings to a Raspberry Pi over USB serial, then build a small web dashboard
