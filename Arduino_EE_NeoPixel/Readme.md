# Arduino - EmptyEpsilon - NeoPixel hardware

Simple example on how to use an Arduino and common WS2811 (NeoPixel) led strips.

Wiring is extremely simple. WS2811 strips have 3 wires:
1) 5V
2) Data
3) Gnd

Just connect these 3 straight to the Arduino. It should have 5V, GND pins labeled.
The data pin needs to be connected to D4 in this example code.

Tested with an Arduino Nano. Should also work with the Arduino Uno, Leonardo, Mega, Micro.

Example configuration assumes 8 LEDs.