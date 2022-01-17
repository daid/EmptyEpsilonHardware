# Neopixel ESP8266 Wifi enabled

Code to setup an ESP8266 to receive DMX512 messages over WiFi from EmptyEpsilon.

Talks to Neopixels (WS2811 leds) on Pin 2.

Tested with ESP-01 hardware, 1MB flash.

## Installation

1) Install https://micropython.org/ on your ESP
2) Configure the ESP to connect to your WiFi network. Should be:
```
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('essid', 'password')
```
3) Upload main.py
