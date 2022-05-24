#!/usr/bin/python3
import struct

device_path = "/dev/input/mice"

# unsigned long, short, unsigned char, unsigned char
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

with open(device_path, "rb") as device:
  event = device.read(EVENT_SIZE)
  while event:
    print(event)
#     (js_time, js_val, js_type, js_num) = struct.unpack(EVENT_FORMAT, event)
#     print( "{0}, {1}, {2}, {3}".format( js_time, js_val, js_type, js_num ) )
#     
    event = device.read(EVENT_SIZE)