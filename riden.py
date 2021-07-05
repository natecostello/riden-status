import instrument_logger
from rd6006 import RD6006

class RidenMonitor(instrument_logger.Instrument):
    def __init__(self, port) -> None:
        self._rd = RD6006(port)

    @property
    def name(self) -> str:
        """Required by Instrument"""
        return 'rd6018'
    
    @property
    def allmeasurements(self) -> 'dict':
        """Required by Instrument"""
        pass

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
        pass



    

