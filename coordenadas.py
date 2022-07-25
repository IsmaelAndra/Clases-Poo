from unicodedata import name


class Coordenadas: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distancia(self, otra_coordenada):
        x_diff  = (self.x - otra_coordenada.x)**2
        y_diff  = (self.y - otra_coordenada.y)**2
        
        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coordenada1 = Coordenadas(8, 35)
    coordenada2 = Coordenadas(15, 1)
    
    print(coordenada1.distancia(coordenada2))
    print(isinstance(3, Coordenadas))