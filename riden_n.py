import time
import instrument_logger
from rd6006 import RD6006
from threading import Thread


class RidenMonitor(instrument_logger.Instrument):

    def __init__(self, port: str = None, rd60xx: RD6006 = None) -> None:
        if (rd60xx is not None):
            self._rd = rd60xx
        elif (port is not None):
            self._rd = RD6006(port)
        else:
            raise ValueError('Either a port or RD606 instance must be provided')
        
        self._voltage = ''
        self._current = ''
        self._measvoltage = ''
        self._meascurrent = ''
        self._measpower = ''
        self._meastemp_external = ''
        self._started = False
        self._isValid = False

    @property
    def name(self) -> str:
        """Required by Instrument"""
        return 'rd6018'
    
    @property
    def allmeasurements(self) -> 'dict':
        """Required by Instrument"""
        all_meas = {}
        for param in self.parameters:
            all_meas[param] = self.getmeasurement(param)
        return all_meas

    @property
    def parameters(self) -> 'list[str]':
        """Required by Instrument"""
        return [
            self.name + '.Voltage Setting.V',
            self.name + '.Current Setting.A',
            self.name + '.Voltage Output.V',
            self.name + '.Current Output.A',
            self.name + '.Power Output.W',
            self.name + '.External Temperature.C'
        ]

    def getmeasurement(self, name: str) -> str:
        """Required by Instrument"""
        if (name == self.name + '.Voltage Setting.V'):
             return str(self._voltage)
        if (name == self.name + '.Current Setting.A'):
             return str(self._current)
        if (name == self.name + '.Voltage Output.V'):
             return str(self._measvoltage)
        if (name == self.name + '.Current Output.A'):
             return str(self._meascurrent)
        if (name == self.name + '.Power Output.W'):
             return str(self._measpower)
        if (name == self.name + '.External Temperature.C'):
             return str(self._meastemp_external)
    
    @property
    def isValid(self) -> 'str':
        return self._isValid
    
    def _riden_poller(self):
        while self._started:
            self._voltage = str(self._rd.voltage)
            time.sleep(0.5)
            self._current = str(self._rd.current)
            time.sleep(0.5)
            self._measvoltage = str(self._rd.measvoltage)
            time.sleep(0.5)
            self._meascurrent = str(self._rd.meascurrent)
            time.sleep(0.5)
            self._measpower = str(self._rd.measpower)
            time.sleep(0.5)
            self._meastemp_external = str(self._rd.meastemp_external)
            self._isValid = True
            time.sleep(0.5)
            
    def start(self):
        self._started = True
        rx = Thread(target=self._riden_poller)
        rx.daemon = True
        rx.start()

    def stop(self):
        self._started = False



    

