import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
print("LED on")
led.value = False
time.sleep(1)
print("LED off")
led.value = True
time.sleep(1)
print("LED on")
led.value = False
time.sleep(1)

print("Done!")
led.deinit()
