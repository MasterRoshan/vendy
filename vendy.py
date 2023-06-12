from RPi import GPIO
import time

# Map rows and columns to pins on the RPi
PIN_ROW = {
    'A': 14,
    'B': 15,
    'C': 18,
    'D': 23,
    'E': 24
}
PIN_COL = {
    1: 2,
    2: 3,
    3: 4,
    4: 17,
    5: 27,
    6: 22,
    7: 10,
    8: 8,
    9: 17,
    10: 5
}
INPUT_PIN = 26

GPIO.setmode(GPIO.BCM) # Use Broadcom SOC channel numbering

GPIO.setup(INPUT_PIN, GPIO.IN)
# get a list of all the output pins to setup
pins = list(PIN_ROW.values())
pins.extend(PIN_COL.values())

# set all the pins to output
# NOTE: initial is HIGH because board is active LOW
for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

def send_full_rotation(row, col):
    """Send a complete rotation to the tray

    Args:
        row (str): The row (A,B,C,D,E)
        col (int): The column 1-10
    """
    GPIO.output(PIN_ROW.get(row), GPIO.LOW)
    GPIO.output(PIN_COL.get(col), GPIO.LOW)
    time.sleep(2)

    while GPIO.input(INPUT_PIN) == GPIO.HIGH:
        time.sleep(0.1)

    GPIO.output(PIN_ROW.get(row), GPIO.HIGH)
    GPIO.output(PIN_COL.get(col), GPIO.HIGH)
    
    