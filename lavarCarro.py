class LavarCarro :
    def __init__(self):
        pass
    
    def lavar(self, temperatura = 'Caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._aspirar()
        self._poner_jabon()
        self._lavar()
        self._pulido()
        
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
        
    def _aspirar(self):
        print('Aspirando el interior del vehiculo')
    
    def _poner_jabon(self):
        print('Añadiendo jabon')
        
    def _lavar(self):
        print('Lavando carroceria')
    
    def _pulido(self):
        print('Puliendo carroceria')
        
if __name__ == '__main__':
    lavadora = LavarCarro()
    lavadora.lavar('Fria')