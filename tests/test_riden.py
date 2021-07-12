from riden import Riden
from context import riden_n
from threading import Thread
import timeit
import time

print('starting')
ps = Riden('/dev/ttyUSBrd6018')
print('made power supply instance')

#ps.status()

rd_inst1 = riden_n.RidenMonitor(rd60xx=ps)
print('made the two instances')
# rd_inst1.start()


print("valid")

print(timeit.timeit("ps.update()",globals=globals(), number=100))

rd_inst1.start()
while not rd_inst1.isValid:
    print('waiting for inst to become valid')
    time.sleep(0.2)

def read_inst():
    print("inst read voltage setting from main = " + rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))

def read_inst_cont():
    while True:
        print("inst read voltage setting from thread = " + rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))
        time.sleep(0.25)

# def read_ps():
#     print("ps read voltage setting from main = " + str(ps.voltage))
#     time.sleep(2)

# def read_ps_cont():
#     while True:
#         print("ps read voltage setting from thread = " + str(ps.voltage))
#         time.sleep(0.5)

# spawn thread
tr = Thread(target=read_inst_cont)
tr.daemon = True
tr.start()

# read from main thread
count = True
while True:
    # read_inst()
    if count:
        count = not count
        ps.set_voltage_set(26.1)
    else:
        count = not count
        ps.set_voltage_set(26.0)
    time.sleep(1)
    # ps.voltage = 26.1
    
# while True:
#     print('rd6018.Voltage Setting.V= '+ rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))