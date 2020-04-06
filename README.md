# ventivalve
The medical ventilator valve controller.

![](doc/scm.jpg)

## Used Software
* [VSCode](https://code.visualstudio.com/)
* [Micropython](http://docs.micropython.org/en/latest/)
* [esptool](https://github.com/espressif/esptool)
* [ampy](https://github.com/pycampers/ampy)
* [Ubuntu](https://ubuntu.com/)

## Flashing the firmware
Make sure it's enough current could flow through the cable the module is connected to.
```sh
cd fw/
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200406-v1.12-337-g312c69949.bin
```

List files on th device:
```sh
ampy -p /dev/ttyUSB0 -b115200 ls
```
Device console:
```sh
picocom /dev/ttyUSB0 -b115200
```

## Upload the software
But also uploading could be done manually with ampy tool.
```sh
cd src/
ampy -p /dev/ttyUSB0 -b115200 put filname.py
```
## [Hardware components list](hw/hardware_list.md)