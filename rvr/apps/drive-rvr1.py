import board
import busio
import time
import math
import struct
import digitalio

# board specific definitions
uart = busio.UART(board.A2, board.A3, baudrate=115200) # TX2 RX2 blackpill
#uart = busio.UART(board.C2, board.C3, baudrate=115200) # TX2 RX2 Metro M0 express

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def blink(n):
    for x in range(n):
        led.value = False
        time.sleep(0.3)
        led.value = True
        time.sleep(0.3)

def drive_to_position_si(yaw_angle, x, y, speed):
    SOP = 0x8d
    FLAGS = 0x06
    TARGET_ID = 0x0e
    SOURCE_ID = 0x0b
    DEVICE_ID = 0x16
    COMMAND_ID = 0x38
    SEQ = 0x01
    EOP = 0xD8

    yaw_angle = bytearray(struct.pack('>f', yaw_angle))
    x = bytearray(struct.pack('>f', x))
    y = bytearray(struct.pack('>f', y))
    speed = bytearray(struct.pack('>f', speed))
    flags = bytearray(struct.pack('B', 0))

    output_packet = [SOP, FLAGS, DEVICE_ID,COMMAND_ID,SEQ]
    output_packet.extend(yaw_angle)
    output_packet.extend(x)
    output_packet.extend(y)
    output_packet.extend(speed)
    output_packet.extend(flags)
    output_packet.extend([~((sum(output_packet) - SOP) % 256) & 0x00FF,EOP])

    print(bytearray(output_packet))
    return bytearray(output_packet)

blink(3)
SPEED = 0.6
TILE_WIDTH = 0.8

coordinates = [[0,0],[0,1],[1,1],[1,0],[0,0],[1,1],[0,0],[0,0.1]]
#coordinates = [[0,0],[0,2],[-1,2],[-1,3],[2,3],[2,2],[0,1],[0,0],[0,0.1]]
positions = []

for pair in coordinates:
    positions.append([0.0,pair[0]*TILE_WIDTH,pair[1]*TILE_WIDTH])

for i in range(len(positions)-1):
    current_position = positions[i]
    next_position = positions[i+1]
    dx = next_position[1] - current_position[1]
    dy = next_position[2] - current_position[2]
    raw_angle = -180.0/3.1415926*math.atan2(dx,dy)

    command = drive_to_position_si(raw_angle,next_position[1],next_position[2],SPEED)
    uart.write(command)

    travel_time = math.sqrt(dx*dx + dy*dy)/SPEED*1.1 + 2.5
    print("Driving to {0},{1}, heading {2}, travel time {3}".format(next_position[1],next_position[2], raw_angle,travel_time))
    blink(2)
    time.sleep(travel_time)

blink(3)
