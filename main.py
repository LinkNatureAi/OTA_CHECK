import machine
import time

# Set up the LED pin
led_pin = machine.Pin(2, machine.Pin.OUT)

# Set up the serial communication

#uart = machine.UART(0, baudrate=115200)

# Loop forever
#while True:
for i in range(3):
    # Turn the LED on
    led_pin.on()
    # Print a message to the serial monitor
    print('LED ON\n')
    # Wait for 1 second
    time.sleep(0.3)
    # Turn the LED off
    led_pin.off()
    # Print a message to the serial monitor
    print('LED OFF_ota_main_py\n')
    # Wait for 1 second
    time.sleep(0.2)
    
import ugit
ugit.pull_all()
