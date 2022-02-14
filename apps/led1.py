import time
import machine
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
N = 200_000

t0 = time.monotonic()

# Simple loop
for i in range(N):
    led.value = True
    led.value = False
    
t1 = time.monotonic()
dt = (t1 - t0)
fmt = '{:5.3f} sec,  {:6.3f} µsec/blink : {:8.2f} kblinks/sec'
print(fmt.format(dt, dt/N*1e6, N/dt*1e-3))
led.deinit()
