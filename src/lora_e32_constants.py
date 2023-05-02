class Logger:
    def __init__(self, enable_debug):
        self.enable_debug = enable_debug
        self.name = ''

    def debug(self, msg, *args):
        if self.enable_debug:
            print(self.name + ' DEBUG ' + msg, *args)

    def info(self, msg, *args):
        if self.enable_debug:
            print(self.name + ' INFO ' + msg, *args)

    def error(self, msg, *args):
        if self.enable_debug:
            print(self.name + ' ERROR ' + msg, *args)

    def getLogger(self, name):
        self.name = name
        return Logger(self.enable_debug)


logging = Logger(False)

logger = logging.getLogger(__name__)


class UARTParity:
    MODE_00_8N1 = 0b00
    MODE_01_8O1 = 0b01
    MODE_10_8E1 = 0b10
    MODE_11_8N1 = 0b11

    @staticmethod
    def get_description(uart_parity):
        if uart_parity == UARTParity.MODE_00_8N1:
            return "8N1 (Default)"
        elif uart_parity == UARTParity.MODE_01_8O1:
            return "8O1"
        elif uart_parity == UARTParity.MODE_10_8E1:
            return "8E1"
        elif uart_parity == UARTParity.MODE_11_8N1:
            return "8N1"
        else:
            return "Invalid UART Parity!"

    @staticmethod
    def get_uart_value(uart_parity):
        if uart_parity == UARTParity.MODE_00_8N1:
            return None
        elif uart_parity == UARTParity.MODE_01_8O1:
            return 0
        elif uart_parity == UARTParity.MODE_10_8E1:
            return 1
        elif uart_parity == UARTParity.MODE_11_8N1:
            return None
        else:
            return ValueError("Invalid UART Parity!")


class UARTBaudRate:
    BPS_1200 = 0b000
    BPS_2400 = 0b001
    BPS_4800 = 0b010
    BPS_9600 = 0b011
    BPS_19200 = 0b100
    BPS_38400 = 0b101
    BPS_57600 = 0b110
    BPS_115200 = 0b111

    @staticmethod
    def get_description(uart_baud_rate):
        if uart_baud_rate == UARTBaudRate.BPS_1200:
            return "1200bps"
        elif uart_baud_rate == UARTBaudRate.BPS_2400:
            return "2400bps"
        elif uart_baud_rate == UARTBaudRate.BPS_4800:
            return "4800bps"
        elif uart_baud_rate == UARTBaudRate.BPS_9600:
            return "9600bps (default)"
        elif uart_baud_rate == UARTBaudRate.BPS_19200:
            return "19200bps"
        elif uart_baud_rate == UARTBaudRate.BPS_38400:
            return "38400bps"
        elif uart_baud_rate == UARTBaudRate.BPS_57600:
            return "57600bps"
        elif uart_baud_rate == UARTBaudRate.BPS_115200:
            return "115200bps"
        else:
            return "Invalid UART Baud Rate!"


class AirDataRate:
    AIR_DATA_RATE_000_03 = 0b000
    AIR_DATA_RATE_001_12 = 0b001
    AIR_DATA_RATE_010_24 = 0b010
    AIR_DATA_RATE_011_48 = 0b011
    AIR_DATA_RATE_100_96 = 0b100
    AIR_DATA_RATE_101_192 = 0b101
    AIR_DATA_RATE_110_192 = 0b110
    AIR_DATA_RATE_111_192 = 0b111

    @staticmethod
    def get_description(air_data_rate):
        if air_data_rate == AirDataRate.AIR_DATA_RATE_000_03:
            return "0.3kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_001_12:
            return "1.2kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_010_24:
            return "2.4kbps (default)"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_011_48:
            return "4.8kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_100_96:
            return "9.6kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_101_192:
            return "19.2kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_110_192:
            return "19.2kbps"
        elif air_data_rate == AirDataRate.AIR_DATA_RATE_111_192:
            return "19.2kbps"
        else:
            return "Invalid Air Data Rate!"


class FixedTransmission:
    TRANSPARENT_TRANSMISSION = 0b0
    FIXED_TRANSMISSION = 0b1

    @staticmethod
    def get_description(fixed_transmission):
        if fixed_transmission == FixedTransmission.TRANSPARENT_TRANSMISSION:
            return "Transparent transmission (default)"
        elif fixed_transmission == FixedTransmission.FIXED_TRANSMISSION:
            return "Fixed transmission (first three bytes can be used as high/low address and channel)"
        else:
            return "Invalid fixed transmission param!"


class IODriveMode:
    OPEN_COLLECTOR = 0b0
    PUSH_PULLS_PULL_UPS = 0b1

    @staticmethod
    def get_description(io_drive_mode):
        if io_drive_mode == IODriveMode.OPEN_COLLECTOR:
            return "TXD, RXD, AUX are open-collectors"
        elif io_drive_mode == IODriveMode.PUSH_PULLS_PULL_UPS:
            return "TXD, RXD, AUX are push-pulls/pull-ups (default)"
        else:
            return "Invalid IO drive mode!"


class WirelessWakeUpTime:
    WAKE_UP_250 = 0b000
    WAKE_UP_500 = 0b001
    WAKE_UP_750 = 0b010
    WAKE_UP_1000 = 0b011
    WAKE_UP_1250 = 0b100
    WAKE_UP_1500 = 0b101
    WAKE_UP_1750 = 0b110
    WAKE_UP_2000 = 0b111

    @staticmethod
    def get_description(wireless_wake_up_time):
        if wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_250:
            return "250ms (default)"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_500:
            return "500ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_750:
            return "750ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_1000:
            return "1000ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_1250:
            return "1250ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_1500:
            return "1500ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_1750:
            return "1750ms"
        elif wireless_wake_up_time == WirelessWakeUpTime.WAKE_UP_2000:
            return "2000ms"
        else:
            return "Invalid wireless wake-up mode!"


class ForwardErrorCorrectionSwitch:
    FEC_0_OFF = 0b0
    FEC_1_ON = 0b1

    @staticmethod
    def get_description(fec):
        if fec == ForwardErrorCorrectionSwitch.FEC_0_OFF:
            return "Turn off Forward Error Correction Switch"
        elif fec == ForwardErrorCorrectionSwitch.FEC_1_ON:
            return "Turn on Forward Error Correction Switch (Default)"
        else:
            return "Invalid FEC param"


class TransmissionPower20:
    POWER_20 = 0b00
    POWER_17 = 0b01
    POWER_14 = 0b10
    POWER_10 = 0b11

    @staticmethod
    def get_description(transmission_power):
        if transmission_power == TransmissionPower20.POWER_20:
            return "20dBm (Default)"
        elif transmission_power == TransmissionPower20.POWER_17:
            return "17dBm"
        elif transmission_power == TransmissionPower20.POWER_14:
            return "14dBm"
        elif transmission_power == TransmissionPower20.POWER_10:
            return "10dBm"
        else:
            return "Invalid transmission power param"

    @staticmethod
    def get_default_value():
        return TransmissionPower20.POWER_20


class TransmissionPower27:
    POWER_27 = 0b00
    POWER_24 = 0b01
    POWER_21 = 0b10
    POWER_18 = 0b11

    @staticmethod
    def get_description(transmission_power):
        if transmission_power == TransmissionPower27.POWER_27:
            return "27dBm (Default)"
        elif transmission_power == TransmissionPower27.POWER_24:
            return "24dBm"
        elif transmission_power == TransmissionPower27.POWER_21:
            return "21dBm"
        elif transmission_power == TransmissionPower27.POWER_18:
            return "18dBm"
        else:
            return "Invalid transmission power param"

    @staticmethod
    def get_default_value():
        return TransmissionPower27.POWER_27


class TransmissionPower30:
    POWER_30 = 0b00
    POWER_27 = 0b01
    POWER_24 = 0b10
    POWER_21 = 0b11

    @staticmethod
    def get_description(transmission_power):
        if transmission_power == TransmissionPower30.POWER_30:
            return "30dBm (Default)"
        elif transmission_power == TransmissionPower30.POWER_27:
            return "27dBm"
        elif transmission_power == TransmissionPower30.POWER_24:
            return "24dBm"
        elif transmission_power == TransmissionPower30.POWER_21:
            return "21dBm"
        else:
            return "Invalid transmission power param"

    @staticmethod
    def get_default_value():
        return TransmissionPower30.POWER_30


class TransmissionPower33:
    POWER_33 = 0b00
    POWER_30 = 0b01
    POWER_27 = 0b10
    POWER_24 = 0b11

    @staticmethod
    def get_description(transmission_power):
        if transmission_power == TransmissionPower33.POWER_33:
            return "33dBm (Default)"
        elif transmission_power == TransmissionPower33.POWER_30:
            return "30dBm"
        elif transmission_power == TransmissionPower33.POWER_27:
            return "27dBm"
        elif transmission_power == TransmissionPower33.POWER_24:
            return "24dBm"
        else:
            return "Invalid transmission power param"

    @staticmethod
    def get_default_value():
        return TransmissionPower33.POWER_33


class TransmissionPower37:
    POWER_37_00 = 0b00
    POWER_37_01 = 0b01
    POWER_37_10 = 0b10
    POWER_37_11 = 0b11

    @staticmethod
    def get_description(transmission_power):
        logger.debug("TransmissionPower37.get_description: transmission_power = %s", transmission_power)
        logger.debug("TransmissionPower37.POWER_37_00: transmission_power = %s", TransmissionPower37.POWER_37_00)

        if transmission_power == TransmissionPower37.POWER_37_00:
            return "37dBm (Default)"
        elif transmission_power == TransmissionPower37.POWER_37_01:
            return "37dBm"
        elif transmission_power == TransmissionPower37.POWER_37_10:
            return "37dBm"
        elif transmission_power == TransmissionPower37.POWER_37_11:
            return "37dBm"
        else:
            return "Invalid transmission power param"

    @staticmethod
    def get_default_value():
        return TransmissionPower37.POWER_37_00


# here a class that contains the starting frequency of the different devices
# the device 433 start with 410 frequency and so on
class OperatingFrequency:
    FREQUENCY_433 = 410
    FREQUENCY_170 = 130
    FREQUENCY_470 = 370
    FREQUENCY_868 = 862
    FREQUENCY_900 = 862
    FREQUENCY_915 = 900

    @staticmethod
    def get_value_from_frequency(frequency):
        if not isinstance(frequency, str):
            frequency = str(frequency)

        freq_attr_name = 'FREQUENCY_' + frequency
        freq_value = getattr(OperatingFrequency, freq_attr_name)
        return freq_value

    @staticmethod
    def get_frequency_dict():
        frequency_dict = {name.split("_")[1]: value for name, value in vars(OperatingFrequency).items() if
                          name.startswith('FREQUENCY_')}
        return frequency_dict

    # the frequency is the base element plus the channel
    @staticmethod
    def get_freq_from_channel(device_frequency, channel):
        return OperatingFrequency.get_value_from_frequency(device_frequency) + channel


# model is like 433T20D or 433T27D or 433T30D or 868T20S or 868T27S or 868T30S
# the part before T is the frequency (example 433)
# the part after T is the transmission power (example 20)
# the last letter is the package type, D is for discrete S is for SMD  (example D)
class TransmissionPower:
    def __init__(self, model):
        self.model = model
        self.package_type = None
        self.frequency = None
        self.transmission_power = None

        if model is not None:
            self.package_type = model[6]
            self.frequency = int(model[0:3])
            self.transmission_power = int(model[4:6])
            logger.debug("Package type: " + self.package_type)
            logger.debug("Frequency: " + str(self.frequency))
            logger.debug("Transmission power: " + str(self.transmission_power))

    def get_transmission_power(self):
        if self.transmission_power == 20:
            return TransmissionPower20
        elif self.transmission_power == 27:
            return TransmissionPower27
        elif self.transmission_power == 30:
            return TransmissionPower30
        elif self.transmission_power == 33:
            return TransmissionPower33
        elif self.transmission_power == 37:
            return TransmissionPower37
        else:
            return "Invalid transmission power param"

    def get_transmission_power_description(self, transmission_power):
        return self.get_transmission_power().get_description(transmission_power)
