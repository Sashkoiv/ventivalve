class Pressure:
    '''Pressure measuring class'''

    def __init__(self,
                 scl: int = 22,
                 sda: int = 21,
                 addr: int = 0x76,
                 name: str = 'bme280'):
        self.scl = scl
        self.sda = sda
        self.addr = addr
        self.sensors = {
            'bme280': self._bme280,
            'bmp280': self._bmp280,
            'bmp180': self._bmp180,
            'mock': self._mock
        }

        if name in self.sensors:
            self.sensor = self.sensors[name]
        else:
            raise NameError(f'No such sensor supported: {name}')

    @property
    def get(self) -> int:
        '''
        Gets the value of pressure and returns it.
        '''
        return self.sensor()

    def _bme280(self):
        ...

    def _bmp280(self):
        ...

    def _bmp180(self):
        ...

    def _mock(self):
        ...
