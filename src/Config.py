# ******************************************************************************************
# FileName     : Config.py
# Description  : Configuration
# Author       : 손철수
# Created Date : 2022.02.02
# Reference    :
# Modified     :
# ******************************************************************************************

import json

# Device ID list
device_id_list = [1, 2]

# Serial Port
serial_port = 'COM6'

# Logging Interval (Second Unit)
logging_interval = 10

# Load from json
file_path = "./Config.json"

# json 파일 읽어 오기
with open(file_path, 'r') as file:
    data = json.load(file)
    print(data)
    string_device_id_list = data['device_id_list'].split(',')
    device_id_list = [int(i) for i in string_device_id_list]
    serial_port = data['serial_port']
    logging_interval = data['logging_interval']

# ******************************************************************************************
# End of File
# ******************************************************************************************
