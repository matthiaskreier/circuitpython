import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
N = 200_000

# Unroll the loop 8 times
def blink_preload_unrolled8(n):
    n //= 8
    on = led.value
    r = range(n)
    for i in r:
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        on = True
        on = False
        
def time_it(f, n):
    t0 = time.monotonic()
    f(n)
    t1 = time.monotonic()
    dt = (t1 - t0)
    fmt = '{:5.3f} sec,  {:6.3f} µsec/blink : {:8.2f} kblinks/sec'
    print(fmt.format(dt, dt/N*1e6, N/dt*1e-3))

time_it(blink_preload_unrolled8, N)
led.deinit()
