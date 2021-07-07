from context import riden

try:
    rd_inst1 = riden.RidenMonitor()
    
except ValueError as e:
    print("Exception as expection:")
    print(e)

#rd_inst = riden.RidenMonitor('/dev/ttyUSB')