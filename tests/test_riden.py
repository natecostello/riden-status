from rd6006 import RD6006
from context import riden_n
from threading import Thread
import timeit
import time

print('starting')
ps = RD6006('/dev/ttyUSBrd6018')
print('made power supply instance')

ps.status()

rd_inst1 = riden_n.RidenMonitor(rd60xx=ps)
print('made the two instances')
rd_inst1.start()

while not rd_inst1.isValid:
    print('waiting for inst to become valid')
    time.sleep(4)

print("valid")

#print(timeit.timeit("rd_inst1.getmeasurement('rd6018.Voltage Setting.V')",globals=globals(), number=10))

def read_inst():
    print("inst read voltage setting from main = " + rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))
    time.sleep(10)

def read_inst_cont():
    while True:
        print("inst read voltage setting from thread = " + rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))
        time.sleep(10)

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
while True:
    read_inst()
    # ps.voltage = 26.1
    
# while True:
#     print('rd6018.Voltage Setting.V= '+ rd_inst1.getmeasurement('rd6018.Voltage Setting.V'))