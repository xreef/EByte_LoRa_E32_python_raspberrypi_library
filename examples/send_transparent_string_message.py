# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E32 LoRa module with RaspberryPi.
# Sending string
#
# Note: This code was written and tested using RaspberryPi on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e32 import LoRaE32, Configuration
import serial

from lora_e32_operation_constant import ResponseStatusCode

# Initialize the LoRaE32 module
loraSerial = serial.Serial('/dev/serial0') #, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
lora = LoRaE32('433T20D', loraSerial, aux_pin=18, m0_pin=23, m1_pin=24)
code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

# Set the configuration to default values and print the updated configuration to the console
# Not needed if already configured
# configuration_to_set = Configuration('433T20D')
# code, confSetted = lora.set_configuration(configuration_to_set)
# print("Set configuration: {}", ResponseStatusCode.get_description(code))

# Send a string message (transparent)
message = 'Hello, world!'
code = lora.send_transparent_message(message)
print("Send message: {}", ResponseStatusCode.get_description(code))
