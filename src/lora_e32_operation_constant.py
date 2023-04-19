class ModeType:
    MODE_0_NORMAL = 0
    MODE_1_WAKE_UP = 1
    MODE_2_POWER_SAVING = 2
    MODE_3_SLEEP = 3
    MODE_3_PROGRAM = 3
    MODE_INIT = 0xFF


class ProgramCommand:
    WRITE_CFG_PWR_DWN_SAVE = 0xC0
    READ_CONFIGURATION = 0xC1
    WRITE_CFG_PWR_DWN_LOSE = 0xC2
    READ_MODULE_VERSION = 0xC3
    WRITE_RESET_MODULE = 0xC4


class ResponseStatusCode:
    SUCCESS = 1
    E32_SUCCESS = 1
    ERR_E32_UNKNOWN = 2
    ERR_E32_NOT_SUPPORT = 3
    ERR_E32_NOT_IMPLEMENT = 4
    ERR_E32_NOT_INITIAL = 5
    ERR_E32_INVALID_PARAM = 6
    ERR_E32_DATA_SIZE_NOT_MATCH = 7
    ERR_E32_BUF_TOO_SMALL = 8
    ERR_E32_TIMEOUT = 9
    ERR_E32_HARDWARE = 10
    ERR_E32_HEAD_NOT_RECOGNIZED = 11
    ERR_E32_NO_RESPONSE_FROM_DEVICE = 12
    ERR_E32_WRONG_UART_CONFIG = 13
    ERR_E32_PACKET_TOO_BIG = 14
    ERR_E32_JSON_PARSE = 15
    ERR_E32_DEINIT_UART_FAILED = 16

    @staticmethod
    def get_description(status):
        if status == ResponseStatusCode.E32_SUCCESS:
            return "Success"
        elif status == ResponseStatusCode.ERR_E32_UNKNOWN:
            return "Unknown"
        elif status == ResponseStatusCode.ERR_E32_NOT_SUPPORT:
            return "Not support!"
        elif status == ResponseStatusCode.ERR_E32_NOT_IMPLEMENT:
            return "Not implement"
        elif status == ResponseStatusCode.ERR_E32_NOT_INITIAL:
            return "Not initial!"
        elif status == ResponseStatusCode.ERR_E32_INVALID_PARAM:
            return "Invalid param!"
        elif status == ResponseStatusCode.ERR_E32_DATA_SIZE_NOT_MATCH:
            return "Data size not match!"
        elif status == ResponseStatusCode.ERR_E32_BUF_TOO_SMALL:
            return "Buff too small!"
        elif status == ResponseStatusCode.ERR_E32_TIMEOUT:
            return "Timeout!!"
        elif status == ResponseStatusCode.ERR_E32_HARDWARE:
            return "Hardware error!"
        elif status == ResponseStatusCode.ERR_E32_HEAD_NOT_RECOGNIZED:
            return "Save mode returned not recognized!"
        elif status == ResponseStatusCode.ERR_E32_NO_RESPONSE_FROM_DEVICE:
            return "No response from device! (Check wiring)"
        elif status == ResponseStatusCode.ERR_E32_WRONG_UART_CONFIG:
            return "Wrong UART configuration! (BPS must be 9600 for configuration)"
        elif status == ResponseStatusCode.ERR_E32_PACKET_TOO_BIG:
            return "The device support only 58byte of data transmission!"
        elif status == ResponseStatusCode.ERR_E32_JSON_PARSE:
            return "JSON parse error!"
        else:
            return "Invalid status!"


class SerialUARTBaudRate:
    BPS_RATE_1200 = 1200
    BPS_RATE_2400 = 2400
    BPS_RATE_4800 = 4800
    BPS_RATE_9600 = 9600
    BPS_RATE_19200 = 19200
    BPS_RATE_38400 = 38400
    BPS_RATE_57600 = 57600
    BPS_RATE_115200 = 115200

