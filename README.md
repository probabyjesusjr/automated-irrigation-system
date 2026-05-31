# Automated Irrigation System 🌱

An automated plant-watering system built on Raspberry Pi, growing from a single-plant prototype toward a multi-plant, sensor-driven, camera-equipped garden monitor. This is my first robotics and electronics project — built and documented version by version.

![Build photo](v1-single-plant/photos/IMG_4742%20Small.jpeg)

## Versions

The project is built in stages, each one adding capability:

| Version | What it adds | Status |
|---|---|---|
| **[v1 — Single Plant](v1-single-plant/)** | One plant: Pico W reads a soil moisture sensor and runs a pump through a relay | ✅ Current / working |
| **v2 — Four Plants** | Four plants using an ADS1115 ADC to read multiple sensors | 🔭 Planned |
| **v3 — Web Dashboard** | A web dashboard to view readings and control watering remotely | 🔭 Planned |
| **v4 — Camera + ML** | A camera plus machine learning to monitor plant health | 🔭 Planned |

Each version lives in its own folder so the progression stays clear. Start with **[v1-single-plant](v1-single-plant/)** for the full hardware, wiring, and code details.

## Hardware (v1)

- Raspberry Pi Pico W (RP2040)
- Capacitive soil moisture sensor (HW-390 / v2.0)
- SONGLE single-channel relay module (active-low)
- 5V mini submersible pump
- Breadboard, jumper wires, and a 5V / 3A USB power supply

A Raspberry Pi 5 will join the project in later versions as the "brain" for logging, the dashboard, and machine learning.

## Repository structure

```
automated-irrigation-system/
├── v1-single-plant/      # Current build: one plant
│   ├── pico/             # MicroPython code for the Pico W
│   ├── photos/           # Build photos
│   └── README.md         # Full v1 details
├── docs/                 # Tutorials and write-ups
└── README.md             # You are here
```

## Learning journey

I started this project in **May 2026** knowing essentially nothing about electronics — not what a relay was, not how a sensor talks to a microcontroller, nothing. Each version is a checkpoint in learning by building: getting a single plant watered reliably first, then adding plants, then data, then intelligence. The bugs I hit along the way (and how I fixed them) are written up in each version's README, because the debugging is where most of the learning happened.
