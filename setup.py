import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="ebyte-lora-e32-rpi",
    package_dir={'': 'src'},
    py_modules=["lora_e32", "lora_e32_constants", "lora_e32_operation_constant"],
    version="0.0.3",
    description="Ebyte E32 LoRa raspberrypi library device very cheap and very long range (from 3Km to 8Km). Arduino LoRa EBYTE E32 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. sx1278/sx1276.",
    long_description="Ebyte E32 LoRa raspberrypi library device very cheap and very long range (from 3Km to 8Km). Arduino LoRa EBYTE E32 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. sx1278/sx1276.",
    keywords="LoRa, UART, EByte, e32, RaspberryPi, sx1278, sx1276",
    url="https://github.com/xreef/EByte_LoRa_E32_raspberrypi_library",
    author="Renzo Mischianti",
    author_email="renzo.mischianti@gmail.com",
    maintainer="Renzo Mischianti",
    maintainer_email="renzo.mischianti@gmail.com",
    license="MIT",
    install_requires=["RPi", "pyserial", "time", "re"],
    project_urls={
        'homepage': 'https://www.mischianti.org',
        'Documentation': 'https://www.mischianti.org/category/my-libraries/lora-e32-devices/',
        'Documentazione': 'https://www.mischianti.org/it/category/le-mie-librerie/dispositivi-lora-e32/',
        'Repository': 'https://github.com/xreef/EByte_LoRa_E32_python_raspberrypi_library',
        'Bug Tracker': 'https://github.com/xreef/EByte_LoRa_E32_python_raspberrypi_library/issues',
        'Examples': 'https://github.com/xreef/EByte_LoRa_E32_python_raspberrypi_library/tree/main/examples',
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: RaspberryPi",
        "License :: OSI Approved :: MIT License",
    ],
)