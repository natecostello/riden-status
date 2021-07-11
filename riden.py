import instrument_logger
from rd6006 import RD6006

class RidenMonitor(instrument_logger.Instrument):
    # def __init__(self, port) -> None:
    #     self._rd = RD6006(port)

    def __init__(self, port: str = None, rd60xx: RD6006 = None) -> None:
        if (rd60xx is not None):
            self._rd = rd60xx
        elif (port is not None):
            self._rd = RD6006(port)
        else:
            raise ValueError('Either a port or RD606 instance must be provided')
            

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
             return str(self._rd.voltage)
        if (name == self.name + '.Current Setting.A'):
             return str(self._rd.current)
        if (name == self.name + '.Voltage Output.V'):
             return str(self._rd.measvoltage)
        if (name == self.name + '.Current Output.A'):
             return str(self._rd.meascurrent)
        if (name == self.name + '.Power Output.W'):
             return str(self._rd.measpower)
        if (name == self.name + '.External Temperature.C'):
             return str(self._rd.meastemp_external)



    

