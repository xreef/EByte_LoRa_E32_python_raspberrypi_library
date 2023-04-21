# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script initializes the E32 LoRa module with RaspberryPi, retrieves the current configuration, and prints it to the console.
# The code demonstrates how to use the LoRaE32 library to interact with the module and read its configuration.
#
# Note: This code was written and tested using RaspberryPi on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e32 import LoRaE32, print_configuration, Configuration
from lora_e32_operation_constant import ResponseStatusCode
import serial

loraSerial = serial.Serial('/dev/serial0') #, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

lora = LoRaE32('433T20D', loraSerial, aux_pin=18, m0_pin=23, m1_pin=24)

code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

code, configuration = lora.get_configuration()

print("Retrieve configuration: {}", ResponseStatusCode.get_description(code))

print_configuration(configuration)

# Initialization: {} Success
# Retrieve configuration: {} Success
# ----------------------------------------
# HEAD : 0b11000000 192
#
# AddH : 0
# AddL : 0
# Chan : 23  ->  433
#
# SpeedParityBit    : 0b0  ->  8N1 (Default)
# SpeedUARTDatte : 0b11  ->  9600bps (default)
# SpeedAirDataRate  : 0b10  ->  2.4kbps (default)
# OptionTrans       : 0b0  ->  Transparent transmission (default)
# OptionPullup      : 0b1  ->  TXD, RXD, AUX are push-pulls/pull-ups (default)
# OptionWakeup      : 0b0  ->  250ms (default)
# OptionFEC         : 0b1  ->  Turn on Forward Error Correction Switch (Default)
# OptionPower       : 0b0  ->  20dBm (Default)
# ----------------------------------------

