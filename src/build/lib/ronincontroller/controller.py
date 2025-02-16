

import serial
import logging

class Controller:
        
    def __init__(self, device ):

        logging.debug(self.__class__.__name__ + f':  device = {device}')

        # Open Serial Port 
        self.ser = serial.Serial(device, baudrate=100000, parity=serial.PARITY_EVEN, stopbits=2)

    # S-Bus Frame Format (16 channels, 25-byte frame)
    def send_speed(self, pan=1024, tilt=1024, roll=1024):
        # Convert 11-bit channel values to 25-byte S-Bus packet
        packet = bytearray(25)
        packet[0] = 0x0F  # S-Bus Start Byte

        # Insert channel data (11-bit values packed into bytes)
        packet[1] = pan & 0xFF
        packet[2] = (pan >> 8) | ((tilt & 0x07) << 3)
        packet[3] = (tilt >> 3) & 0xFF
        packet[4] = (tilt >> 11) | ((roll & 0x3F) << 2)
        packet[5] = (roll >> 6) & 0xFF

        packet[24] = 0x00  # S-Bus End Byte

        logging.debug(self.__class__.__name__ + f':  packet send = {packet}')
        self.ser.write(packet) 
