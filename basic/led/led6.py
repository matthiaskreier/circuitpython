import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
N = 200_000

# Unroll with native machine emitter
@micropython.viper
def blink_viper(n:int):
    p = ptr16(stm.GPIOB + stm.GPIO_BSRR)
    for i in range(n):
        p[0] = 1 << 4 # high
        p[1] = 1 << 4 # low 

 
def time_it(f, n):
    t0 = time.monotonic()
    f(n)
    t1 = time.monotonic()
    dt = (t1 - t0)
    fmt = '{:5.3f} sec,  {:6.3f} µsec/blink : {:8.2f} kblinks/sec'
    print(fmt.format(dt, dt/N*1e6, N/dt*1e-3))

time_it(blink_viper, N)
led.deinit()
