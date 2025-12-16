class Rectangle:
    
    def __init__ (self, x : int, y : int, width : int, height : int):
        if x<0:
            self.__x = 0
        self.__x = x
        
        if y<0:
            self.__y = 0
        self.__y = y
        
        if width<0:
            self.__width = 0
        self.__width = width
        
        if height<0:
            self.__height = 0
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @x.setter
    def x(self, valor):
        self.__x = valor
    
    @y.setter
    def y(self, valor):
        self.__y = valor

    @width.setter
    def width(self, valor):
        self.__width = valor
    
    @height.setter
    def height(self, valor):
        self.__height = valor

def intersecting(rectangulo1: Rectangle, rectangulo2:Rectangle) -> bool:
    rectangulo1PuntoAlto = rectangulo1.y
    rectangulo1PuntoBajo = rectangulo1.y - rectangulo1.height
    rectangulo2PuntoAlto = rectangulo2.y 
    rectangulo2PuntoBajo = rectangulo2.y - rectangulo2.height
    
    if (rectangulo1PuntoAlto < rectangulo2PuntoBajo) or (rectangulo1PuntoBajo > rectangulo2PuntoAlto):
        return True
    rectangulo1puntaIzq = rectangulo1.x
    rectangulo1puntaDecha = rectangulo1.x - rectangulo1.width
    rectangulo2puntaIzq = rectangulo2.x
    rectangulo2puntaDecha = rectangulo2.x - rectangulo2.width
    if (rectangulo1puntaDecha > rectangulo2puntaIzq) or (rectangulo1puntaIzq < rectangulo2puntaDecha):
        return False
    return True

a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)

print(intersecting(a, b))
print(intersecting(a, c))
print(intersecting(b, c))