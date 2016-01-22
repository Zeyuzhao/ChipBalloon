from gpio import GPIO
import time, sys
io = GPIO()

PIN_7 = 415
HIGH = 1
LOW = 0
DELAY = 0.2
io.setup(PIN_7)

while(True):
    try:
        io.set(PIN_7, HIGH)
        time.sleep(DELAY)
        io.set(PIN_7, LOW)
        time.sleep(DELAY)
    except KeyboardInterrupt:
        io.cleanup()
        sys.exit()



