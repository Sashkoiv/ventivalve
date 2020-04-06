class Display:
    '''The class for showing the data'''

    def __init__(self,
                 scl: int = 22,
                 sda: int = 21,
                 addr: int = 0x78,
                 name: str = 'OLED128x64'):
        self.scl = scl
        self.sda = sda
        self.addr = addr
        self.displays = {
            '1602A': self._1602A,
            'OLED128x64': self._OLED128x64,
            'mock': self._mock
        }

        if name in self.displays:
            self.display = self.displays[name]
        else:
            raise NameError(f'No such display supported: {name}')

    @push.setter    # TODO: Consider redesign this line
    def push(self, data: str) -> None:
        '''
        Pushes the data into the display.
        '''
        self.display()

    def _1602A(self):
        ...

    def _OLED128x64(self):
        ...

    def _mock(self):
        ...
