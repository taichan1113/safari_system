import evdev

device = evdev.InputDevice('/dev/input/event2')

for event in device.read_loop():
    print(event.code)