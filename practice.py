import snap7

ip_address = '192.168.5.2'
rack = 0
slot = 1

db_number = 101
start_address = 2042
size = 2298

plc = snap7.client.Client()
print(plc)
plc.connect(ip_address, rack, slot)

print(plc.list_blocks())

plc.disconnect()