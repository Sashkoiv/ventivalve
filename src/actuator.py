class Actuator:
    '''Valve control class'''

    def __init__(self, name: str = 'servo'):
        self.actuators = {
            'servo': self._servo,
            'stepper': self._stepper,
            'valve': self._valve,
            'mock': self._mock
        }

        if name in self.actuators:
            self.actuator = self.actuators[name]
        else:
            raise NameError(f'No such sensor supported: {name}')

    @apply.setter    # TODO: Consider redesign this line
    def apply(self) -> int:
        '''
        Sets the value of needed pressure.
        '''
        self.actuator()

    def _servo(self):
        ...

    def _stepper(self):
        ...

    def _valve(self):
        ...

    def _mock(self):
        ...