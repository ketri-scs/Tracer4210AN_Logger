# ******************************************************************************
# FileName     : RtuTransaction.py
# Description  : RTU 파일 저장 처리
# Author       : 손철수
# Created Date : 2022.02.02
# Reference    :
# Modified     :
# ******************************************************************************

# ------------------------------------------------------------------------------
# Import
# ------------------------------------------------------------------------------
import datetime
import Tracer4210AN as trcCtr
import os


# ------------------------------------------------------------------------------
# RtuTransaction
# ------------------------------------------------------------------------------
class RtuTransaction:
    # --------------------------------------------------------------------------
    # 클래스 변수
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # 초기자(initializer)
    # --------------------------------------------------------------------------
    def __init__(self, trc):
        self.trc = trc

    # --------------------------------------------------------------------------
    # save_temp_trans
    # --------------------------------------------------------------------------
    def save_temp_trans(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        dir_name = current_date[:7]
        path = 'log/' + dir_name
        os.makedirs(path, exist_ok=True)

        fn = 'log/' + dir_name + '/' + str(self.trc.device_id) + '_' + current_date + '.txt'

        f = open(fn, "a")
        f.write(f'{self.trc.device_id}, ')
        f.write(f'{current_date} {current_time}, ')

        f.write(f'{trcCtr.array_voltage:6.2f}, ')
        f.write(f'{trcCtr.array_current:6.2f}, ')
        f.write(f'{trcCtr.array_power:10.2f}, ')

        f.write(f'{trcCtr.load_voltage:6.2f}, ')
        f.write(f'{trcCtr.load_current:6.2f}, ')
        f.write(f'{trcCtr.load_power:10.2f}, ')

        f.write(f'{trcCtr.battery_voltage:6.2f}, ')
        f.write(f'{trcCtr.battery_current:6.2f}, ')
        f.write(f'{trcCtr.battery_temp:6.2f}, ')
        f.write(f'{trcCtr.battery_soc:6.2f}, ')

        f.write(f'{trcCtr.battery_status:#04x}, ')
        f.write(f'{trcCtr.charging_eq_status:#04x}, ')
        f.write(f'{trcCtr.discharging_eq_status:#04x}, ')

        f.write(f'{trcCtr.gen_energy_today:6.2f}, ')
        f.write(f'{trcCtr.gen_energy_month:6.2f}, ')
        f.write(f'{trcCtr.gen_energy_year:6.2f}, ')
        f.write(f'{trcCtr.gen_energy_total:10.2f}, ')

        f.write(f'{trcCtr.con_energy_today:6.2f}, ')
        f.write(f'{trcCtr.con_energy_month:6.2f}, ')
        f.write(f'{trcCtr.con_energy_year:6.2f}, ')
        f.write(f'{trcCtr.con_energy_total:10.2f}')

        f.write('\n')
        f.close()

# ******************************************************************************
# End of File
# ******************************************************************************
