# LED fast in Circuitpython

These examples are taken from Damien George's talk at PyCon AU on 24 Aug 2018:

- [Youtube video](https://youtu.be/hHec4qL00x0)
- [Website description 2018.pycon-au.org](https://2018.pycon-au.org/talks/45358-writing-fast-and-efficient-micropython/)

Some parameters have to be adjusted, so the first example code on a F411 blackpill looks like this:

``` pycon-au
import time
import board
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
```

With the output:

```
5.842 sec,  29.209 µsec/blink :    34.24 kblinks/sec
```

But with each iteration it got faster:
```
4.841 sec,  24.207 µsec/blink :    41.31 kblinks/sec    # within a function
0.659 sec,   3.296 µsec/blink :   303.41 kblinks/sec    # preload methods
0.205 sec,   1.025 µsec/blink :   975.24 kblinks/sec    # unroll 8 times
0.205 sec,   1.025 µsec/blink :   975.24 kblinks/sec    # @micropython.native
viper does not work
assembler ... was led7.py
```
