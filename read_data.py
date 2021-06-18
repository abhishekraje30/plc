import snap7

ip_address = '192.168.6.5'
rack = 0
slot = 1

db_number = 101
start_address = 2
size = 2

plc = snap7.client.Client()
# print(plc)
plc.connect(ip_address, rack, slot)




plc_info = plc.get_cpu_info()
print(f'The PLC INFO: {plc_info}')

state = plc.get_cpu_state()
print(f'The PLC State: {state}')

data = plc.db_read(db_number = db_number, start = start_address, size = size)
# print(data)
# fit_101 = db[0:size].decode('UTF-8').strip('\\x00')
fit_101 = data.decode('UTF-8').strip('\\x00')
print(fit_101)

plc.disconnect()


