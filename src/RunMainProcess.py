# ******************************************************************************
# FileName     : Tracer4210.py
# Description  : Charge Controller as Tracer4210AN
# Author       : 손철수
# Created Date : 2022.02.02
# Reference    :
# Modified     :
# ******************************************************************************

# ------------------------------------------------------------------------------
# Import
# ------------------------------------------------------------------------------
import time
import datetime

from pymodbus.client.sync import ModbusSerialClient as pyRtu
import Tracer4210AN as trcCtr
import Config

import RtuTransaction

# ------------------------------------------------------------------------------
# global
# ------------------------------------------------------------------------------
pymc = ""


# ------------------------------------------------------------------------------
# open_rtu
# ------------------------------------------------------------------------------
def open_rtu():
    global pymc

    try:
        pymc = pyRtu(method='rtu', port=Config.serial_port,
                     baudrate=115200, stopbits=1, parity='N', bytesize=8, timeout=1)
        if pymc.connect():
            return True
        else:
            return False
    except pymc.exceptions.ConnectionException:
        print("open port error")
        return False
    finally:
        pass


# ------------------------------------------------------------------------------
# get_rtu
# ------------------------------------------------------------------------------
def get_rtu(device_id):
    global pymc

    trcCtr.device_id = device_id
    print(f'\nDevice id = {trcCtr.device_id}', end=', ')

    # ------------------------------------------------------------------------------
    # PV ARRAY
    # ------------------------------------------------------------------------------
    print('PV ARRAY', end=', ')
    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.ARRAY_VOLTAGE_ADR, count=0x04, unit=device_id)
    if response.isError():
        return False

    trcCtr.array_voltage = response.registers[0] / 100
    trcCtr.array_current = response.registers[1] / 100
    # response.registers[2] = 0x93e0
    # response.registers[3] = 0x0004
    trcCtr.array_power = (response.registers[3] * trcCtr.HIGH_VALUE + response.registers[2]) / 100

    # ------------------------------------------------------------------------------
    # LOAD
    # ------------------------------------------------------------------------------
    print('LOAD', end=', ')

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.LOAD_VOLTAGE_ADR, count=0x04, unit=device_id)
    if response.isError():
        return False

    trcCtr.load_voltage = response.registers[0] / 100
    trcCtr.load_current = response.registers[1] / 100
    trcCtr.load_power = (response.registers[3] * trcCtr.HIGH_VALUE + response.registers[2]) / 100

    # ------------------------------------------------------------------------------
    # BATTERY
    # ------------------------------------------------------------------------------
    print('BATTERY', end=', ')

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.BATTERY_VOLTAGE_ADR, count=0x02, unit=device_id)
    if response.isError():
        return False

    trcCtr.battery_voltage = response.registers[0] / 100
    trcCtr.battery_current = response.registers[1] / 100

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.BATTERY_TEMP_ADR, count=0x01, unit=device_id)
    if response.isError():
        return False

    trcCtr.battery_temp = response.registers[0] / 100

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.BATTERY_SOC_ADR, count=0x01, unit=device_id)
    if response.isError():
        return False

    trcCtr.battery_soc = response.registers[0] / 100

    # ------------------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------------------
    print('STATUS', end=', ')

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.BATTERY_STATUS_ADR, count=0x03, unit=device_id)
    if response.isError():
        return False

    trcCtr.battery_status = response.registers[0]
    trcCtr.charging_eq_status = response.registers[1]
    trcCtr.discharging_eq_status = response.registers[2]

    # ------------------------------------------------------------------------------
    # GENERATED ENERGY
    # ------------------------------------------------------------------------------
    print('GENERATED ENERGY', end=', ')

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.GEN_ENERGY_TODAY1_ADR, count=0x08, unit=device_id)
    if response.isError():
        return False

    trcCtr.gen_energy_today = (response.registers[1] * trcCtr.HIGH_VALUE + response.registers[0]) / 100
    trcCtr.gen_energy_month = (response.registers[3] * trcCtr.HIGH_VALUE + response.registers[2]) / 100
    trcCtr.gen_energy_year = (response.registers[5] * trcCtr.HIGH_VALUE + response.registers[4]) / 100
    trcCtr.gen_energy_total = (response.registers[7] * trcCtr.HIGH_VALUE + response.registers[6]) / 100

    # ------------------------------------------------------------------------------
    # CONSUMED ENERGY
    # ------------------------------------------------------------------------------
    print('CONSUMED ENERGY', end=', ')

    time.sleep(0.25)
    response = pymc.read_input_registers(address=trcCtr.CON_ENERGY_TODAY1_ADR, count=0x08, unit=device_id)
    if response.isError():
        return False

    trcCtr.con_energy_today = (response.registers[1] * trcCtr.HIGH_VALUE + response.registers[0]) / 100
    trcCtr.con_energy_month = (response.registers[3] * trcCtr.HIGH_VALUE + response.registers[2]) / 100
    trcCtr.con_energy_year = (response.registers[5] * trcCtr.HIGH_VALUE + response.registers[4]) / 100
    trcCtr.con_energy_total = (response.registers[7] * trcCtr.HIGH_VALUE + response.registers[6]) / 100

    return True

# ------------------------------------------------------------------------------
# Display RTU
# ------------------------------------------------------------------------------
def display_rtu():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_date} {current_time}")
    print('array', trcCtr.array_voltage, trcCtr.array_current, trcCtr.array_power)
    print('load', trcCtr.load_voltage, trcCtr.load_current, trcCtr.load_power)
    print('battery', trcCtr.battery_voltage, trcCtr.battery_current, trcCtr.battery_temp, trcCtr.battery_soc)
    print('status', trcCtr.battery_status, trcCtr.charging_eq_status, trcCtr.discharging_eq_status)
    print('generated', trcCtr.gen_energy_today, trcCtr.gen_energy_month, trcCtr.gen_energy_year, trcCtr.gen_energy_total)
    print('consumed', trcCtr.con_energy_today, trcCtr.con_energy_month, trcCtr.con_energy_year, trcCtr.con_energy_total)


# ------------------------------------------------------------------------------
# Close
# ------------------------------------------------------------------------------
def close_rtu():
    global pymc

    pymc.close()


# ------------------------------------------------------------------------------
# Log RTU
# ------------------------------------------------------------------------------
def log_rtu():
    import RtuTransaction
    rf = RtuTransaction.RtuTransaction(trcCtr)
    rf.save_temp_trans()


# ------------------------------------------------------------------------------
# Do
# ------------------------------------------------------------------------------
def do_process():
    # global
    error_count = 0

    # open
    if not open_rtu():
        print('Error open port ')
        time.sleep(1)
        return

    # get
    try:
        for device_id in Config.device_id_list:
            if get_rtu(device_id):
                display_rtu()
                log_rtu()
                sleep_time = Config.logging_interval - 3 - error_count
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    error_count = 0
            else:
                error_count = error_count + 1
                print(f'Error get_rtu() {error_count:3}')
    except KeyboardInterrupt:
        exit(1)
    finally:
        close_rtu()


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    while True:
        do_process()

# ******************************************************************************
# End of File
# ******************************************************************************
