# ******************************************************************************************
# FileName     : Tracer4210.py
# Description  : Charge Controller as Tracer4210AN
# Author       : 손철수
# Created Date : 2022.02.02
# Reference    :
# Modified     :
# ******************************************************************************************

device_id = 0

# Computing for high value
HIGH_VALUE = 2 ** 16

# Array Information
ARRAY_VOLTAGE_ADR = 0x3100
ARRAY_CURRENT_ADR = 0x3101
ARRAY_POWER1_ADR = 0x3102  # LOW
ARRAY_POWER2_ADR = 0x3103  # HIGH
array_voltage = 0
array_current = 0
array_power = 0

# Load Information
LOAD_VOLTAGE_ADR = 0x310C
LOAD_CURRENT_ADR = 0x310D
LOAD_POWER1_ADR = 0x310E
LOAD_POWER2_ADR = 0x310F
load_voltage = 0
load_current = 0
load_power = 0

# Battery Information
BATTERY_VOLTAGE_ADR = 0x331A
BATTERY_CURRENT_ADR = 0x331B
BATTERY_TEMP_ADR = 0x3110
BATTERY_SOC_ADR = 0x311A
battery_voltage = 0
battery_current = 0
battery_temp = 0
battery_soc = 0

# Charging Equipment Status
BATTERY_STATUS_ADR = 0x3200
CHARGING_EQ_STATUS_ADR = 0x3201
DISCHARGING_EQ_STATUS_ADR = 0x3202
battery_status = 0
charging_eq_status = 0
discharging_eq_status = 0

# Generated Energy
GEN_ENERGY_TODAY1_ADR = 0x330C
GEN_ENERGY_TODAY2_ADR = 0x330D
GEN_ENERGY_MONTH1_ADR = 0x330E
GEN_ENERGY_MONTH2_ADR = 0x330F
GEN_ENERGY_YEAR1_ADR = 0x3310
GEN_ENERGY_YEAR2_ADR = 0x3311
GEN_ENERGY_TOTAL1_ADR = 0x3312
GEN_ENERGY_TOTAL2_ADR = 0x3313
gen_energy_today = 0
gen_energy_month = 0
gen_energy_year = 0
gen_energy_total = 0

# Consumed Energy
CON_ENERGY_TODAY1_ADR = 0x3304
CON_ENERGY_TODAY2_ADR = 0x3305
CON_ENERGY_MONTH1_ADR = 0x3306
CON_ENERGY_MONTH2_ADR = 0x3307
CON_ENERGY_YEAR1_ADR = 0x3308
CON_ENERGY_YEAR2_ADR = 0x3309
CON_ENERGY_TOTAL1_ADR = 0x330A
CON_ENERGY_TOTAL2_ADR = 0x330B
con_energy_today = 0
con_energy_month = 0
con_energy_year = 0
con_energy_total = 0

# ******************************************************************************************
# End of File
# ******************************************************************************************
