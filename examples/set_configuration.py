
# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E32 LoRa module with RaspberryPi.
# It initializes the module, retrieves the current configuration,
# sets a new configuration, and restores the default configuration.
# It also includes examples of sending and receiving data using the module.
#
# Note: This code was written and tested using RaspberryPi on a ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e32 import LoRaE32, print_configuration, Configuration
from lora_e32_constants import OperatingFrequency, FixedTransmission, WirelessWakeUpTime, TransmissionPower, \
    TransmissionPower20, AirDataRate, UARTParity, UARTBaudRate
from lora_e32_operation_constant import ResponseStatusCode
import serial

loraSerial = serial.Serial('/dev/serial0') #, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

lora = LoRaE32('433T20D', loraSerial, aux_pin=18, m0_pin=23, m1_pin=24)

# Initialize the LoRa module and print the initialization status code
code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

##########################################################################################
# GET CONFIGURATION
##########################################################################################

# Retrieve the current configuration of the LoRa module and print it to the console
code, configuration = lora.get_configuration()
print("Retrieve configuration: {}", ResponseStatusCode.get_description(code))
print("------------- CONFIGURATION BEFORE CHANGE -------------")
print_configuration(configuration)

##########################################################################################
# SET CONFIGURATION
# To set the configuration, you must set the configuration with the new values
##########################################################################################

# Create a new Configuration object with the desired settings
configuration_to_set = Configuration('433T20D')
configuration_to_set.ADDL = 0x02
configuration_to_set.ADDH = 0x01
configuration_to_set.CHAN = 23
configuration_to_set.OPTION.operatingFrequency = OperatingFrequency.FREQUENCY_433
configuration_to_set.OPTION.fixedTransmission = FixedTransmission.FIXED_TRANSMISSION
configuration_to_set.OPTION.wakeUpTime = WirelessWakeUpTime.WAKE_UP_250
configuration_to_set.OPTION.transmissionPower = TransmissionPower('433T20D').\
                                                    get_transmission_power().POWER_20
# or
# configuration_to_set.OPTION.transmissionPower = TransmissionPower20.POWER_20
configuration_to_set.SPED.airDataRate = AirDataRate.AIR_DATA_RATE_100_96
configuration_to_set.SPED.uartParity = UARTParity.MODE_00_8N1
configuration_to_set.SPED.uartBaudRate = UARTBaudRate.BPS_9600

# Set the new configuration on the LoRa module and print the updated configuration to the console
code, confSetted = lora.set_configuration(configuration_to_set)
print("------------- CONFIGURATION AFTER CHANGE -------------")
print(ResponseStatusCode.get_description(code))
print_configuration(confSetted)

##########################################################################################
# RESTORE DEFAULT CONFIGURATION
# To restore the default configuration, you must set the configuration with the default values
##########################################################################################

# Set the configuration to default values and print the updated configuration to the console
print("------------- RESTORE ALL DEFAULT -------------")
configuration_to_set = Configuration('433T20D')
code, confSetted = lora.set_configuration(configuration_to_set)
print(ResponseStatusCode.get_description(code))
print_configuration(confSetted)


# print_configuration(confSetted)
# Initialization: {} Success
# Retrieve configuration: {} Success
# ------------- CONFIGURATION BEFORE CHANGE -------------
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
# ------------- CONFIGURATION AFTER CHANGE -------------
# Success
# ----------------------------------------
# HEAD : 0b11000000 192
#
# AddH : 1
# AddL : 2
# Chan : 23  ->  433
#
# SpeedParityBit    : 0b0  ->  8N1 (Default)
# SpeedUARTDatte : 0b11  ->  9600bps (default)
# SpeedAirDataRate  : 0b100  ->  9.6kbps
# OptionTrans       : 0b1  ->  Fixed transmission (first three bytes can be used a
# s high/low address and channel)
# OptionPullup      : 0b1  ->  TXD, RXD, AUX are push-pulls/pull-ups (default)
# OptionWakeup      : 0b0  ->  250ms (default)
# OptionFEC         : 0b1  ->  Turn on Forward Error Correction Switch (Default)
# OptionPower       : 0b0  ->  20dBm (Default)
# ----------------------------------------
# ------------- RESTORE ALL DEFAULT -------------
# Success
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


