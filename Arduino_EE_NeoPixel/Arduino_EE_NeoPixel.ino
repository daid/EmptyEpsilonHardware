#include <Adafruit_NeoPixel.h>

// Which pin on the Arduino is connected to the NeoPixels?
#define PIN        4

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS  8

// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin();
  Serial.begin(115200);
}

// Read a single byte from the serial interface. This function blocks until data is available.
uint8_t readSerial()
{
  while(true) {
    int n = Serial.read();
    if (n != -1) return n;
  }
}

void loop() {
  while(readSerial() != 0x7E) {} // Wait for EnttecPRO start byte
  if (readSerial() != 0x06) return; // Wrong followup byte
  uint16_t size = readSerial();
  size |= readSerial() << 8;
  
  pixels.clear();
  for(int i=0; i<size/3; i++) {
    uint8_t r = readSerial();
    uint8_t g = readSerial();
    uint8_t b = readSerial();
    pixels.setPixelColor(i, pixels.Color(g, r, b)); //Depending on your pixel type, you might need to reorder rgb here.
  }
  pixels.show();
}
