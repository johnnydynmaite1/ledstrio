import board
import neopixel
import time

# NeoPixel setup
LED_PIN = board.D10  # GPIO pin connected to the NeoPixel strip
NUM_LEDS = 60        # Number of LEDs on your strip
BRIGHTNESS = 0.5     # Set desired brightness

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def set_color(red, green, blue):
    """Set the color of the NeoPixel strip."""
    pixels.fill((red, green, blue))
    pixels.show()

# Test the NeoPixel strip
try:
    while True:
        print("Turning on red...")
        set_color(255, 0, 0)
        time.sleep(3)

        print("Turning off...")
        set_color(0, 0, 0)
        time.sleep(3)

        print("Turning on green...")
        set_color(0, 255, 0)
        time.sleep(3)

        print("Turning off...")
        set_color(0, 0, 0)
        time.sleep(3)

        print("Turning on blue...")
        set_color(0, 0, 255)
        time.sleep(3)

        print("Turning off...")
        set_color(0, 0, 0)
        time.sleep(3)

except KeyboardInterrupt:
    print("Exiting test.")
finally:
    set_color(0, 0, 0)  # Ensure the LEDs are turned off when done
