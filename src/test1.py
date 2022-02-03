import time
from pymodbus.client.sync import ModbusSerialClient as pyRtu

pymc = pyRtu(method='rtu', port='COM6', baudrate=115200, stopbits=1, parity='N', bytesize=8, timeout=2)

errCnt = 0
startTs = time.time()
response = pymc.read_input_registers(address=0x0331a, count=0x01, unit=1)
print(response.registers[0])
pymc.close()

stopTs = time.time()
timeDiff = stopTs - startTs
print("pymodbus:\t time to read %.3f [s]", timeDiff)




