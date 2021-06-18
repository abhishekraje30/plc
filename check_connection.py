import snap7
import struct
import time
import re
from ctypes import c_int, c_char_p, byref, sizeof, c_uint16, c_int32, c_byte
from ctypes import c_void_p

client = snap7.client.Client()

db_number = 101

print('Press Ctrl-C to quit.')

while True:

    if client.get_connected() == False:
        try:
            client.connect('192.168.6.5', 0, 1) #('IP-address', rack, slot)
            print('not connected')
            time.sleep(0.2)
        except Exception as e:
            continue
    else:
        print('connected')