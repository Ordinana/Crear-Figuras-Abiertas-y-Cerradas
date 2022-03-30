import abc
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

"""CREACION DE FIGURAS TANTO ABIERTAS COMO CERRADAS, PARTIENDO DE 2 CLASES PADRE (PUNTO Y FIGURA).
A raíz de ello obtendremos 4 tipos de figuras abiertas (Quebrada, Hipérbola, Parábola y Sinusoidal)
y 3 tipos de figuras cerradas (Polígono, Elipse y Círculo)"""

class Punto:
    """PUNTOS EN EL PLANO"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(str(self.x), str(self.y))


class Figura(metaclass=abc.ABCMeta):
    """CARACTERÍSTICAS COMUNES DE TODAS LAS FIGURAS Y PUNTOS"""

    # NO HABRÁN OBJETOS A ESTA CLASE PERO SI OTRAS CLASES HEREDARÁN SUS ATRIBUTOS
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def representa(self):
        pass  # SE REDEFINE EN LAS SUBCLASES


class Figura_Abierta(Figura):
    """1ER TIPO DE FIGURA"""
    pass  # SON LÍNEAS QUEBRADAS, SEGMENTOS, ETC...


class Figura_Cerrada(Figura):
    """2DO TIPO DE FIGURA"""

    # TIENE 1 ATRIBUTO Y 3 MÉTODOS ABSTRACTOS

    def __init__(self, color):
        super().__init__(color)

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def centro(self):
        self.centro = (x, y)

    @abc.abstractmethod
    def perimetro(self):
        pass


#  FIGURA ABIERTA 1
class Quebrada(Figura_Abierta):

    def __init__(self, numPuntos, color):
        self.numPuntos = numPuntos
        p = Punto(0, 0)
        self.puntos = [p for i in range(self.numPuntos)]
        Figura.__init__(self, color)

    def __str__(self):
        if self.numPuntos == 2:
            return "Es un segmento"
        elif self.numPuntos > 2:
            return "Es una linea quebrada"

    def ponPuntos(self):
        for i in range(self.numPuntos):
            print("Introduce Punto {}".format(str(i + 1)))
            x = float(input("Coordenada X: "))
            y = float(input("Coordenada Y: "))
            p = Punto(x, y)
            self.puntos[i] = p

    def obtenPuntos(self):
        for i in range(self.numPuntos):
            print("Punto {}:{}".format(i + 1, self.puntos[i]))
        return self.puntos

    def representa(self):
        x = []
        y = []
        for i in range(self.numPuntos):
            x.append(self.puntos[i].x)
            y.append(self.puntos[i].y)
            print("I es: ", i, "y X[", i, "] es: ", x[i])
            print("I es: ", i, "e Y[", i, "] es: ", y[i])
        plt.plot(x, y, self.color)
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()


# FIGURA ABIERTA 2
class Hiperbola(Figura_Abierta):
    #  Ecuación: (x/a) ^2 - (y/b)^2 = 1
    #  x0, y0, son las coordenadas del centro

    def __init__(self, centro, a, b, color):
        self.centro = centro
        self.a = a
        self.b = b
        Figura.__init__(self, color)

    def __str__(self):
        return "Hipérbola"

    def representa(self):
        rango = 10
        x = np.linspace(-int(rango / 2), int(rango / 2), 200)
        n = len(x)
        y = np.zeros(n)
        for i in range(n):
            y[i] = self.b * math.sqrt((x[i] / self.a) ** 2 + 1)
        plt.plot(x, y, self.color)
        plt.title("Hipérbola")
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()


# FIGURA ABIERTA 3
class Parabola(Figura_Abierta):
    #  Parábola de ecuacion: y= a x^2 + bx + c
    #  if a > 0 (ramas hacia arriba), a < 0 (ramas hacia abajo)
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        Figura.__init__(self, color)

    def __str__(self):
        return "Parábola"

    def representa(self):
        rango = 20
        x = np.linspace(-int(rango / 2), int(rango / 2), 200)
        y = self.a * x ** 2 + self.b * x + self.c
        plt.plot(x, y, self.color)
        plt.title("Parábola")
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()


# FIGURA ABIERTA 4
class Sinusoidal(Figura_Abierta):
    #  Genera funciones SENO
    def __init__(self, amplitud, frecuencia, fase, color):
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.fase = fase
        Figura.__init__(self, color)
        self.color = color

    def __str__(self):
        return "Función seno de amplitud {}, frecuencia {}, y fase {}".format(self.amplitud, self.frecuencia, self.fase)

    def representa(self):
        duracion = 2
        x = np.linspace(-int(duracion / 2), int(duracion / 2), 200)
        n = len(x)
        y = np.zeros(n)
        for i in range(n):
            y[i] = self.amplitud * math.sin(2 * math.pi * self.frecuencia * x[i] + self.fase)
        plt.plot(x, y, self.color)
        plt.title("Seno")
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()

    def parametros(self):
        periodo = 1 / self.frecuencia
        return periodo


# FIGURA CERRADA 1
class Poligono(Figura_Cerrada):
    def centro(self):
        pass

    def __init__(self, numLados, color):
        self.numLados = numLados
        p = Punto(0, 0)
        self.puntos = [p for i in range(self.numLados)]
        Figura_Cerrada.__init__(self, color)
        Figura.__init__(self, color)
        self.color = color

    def ponPuntos(self):
        for i in range(self.numLados):
            print("Introduce vértice {}".format(str(i + 1)))
            x = float(input("Cordenada X: "))
            y = float(input("Cordenada Y: "))
            p = Punto(x, y)
            self.puntos[i] = p

    def __str__(self):
        if self.numLados == 3:
            return "Es un triangulo"
        elif self.numLados == 4:
            return "Es un cuadrilátero"
        elif self.numLados == 5:
            return "Es un pentágono"
        elif self.numLados == 6:
            return "Es un hexágono"
        elif self.numLados == 7:
            return "Es un heptágono"
        elif self.numLados == 8:
            return "Es un octágono"
        elif self.numLados == 9:
            return "Es un eneágono"
        elif self.numLados == 10:
            return "Es un decágono"
        elif self.numLados == 11:
            return "Es un endecágono"
        elif self.numLados == 12:
            return "Es un dodecágono"
        else:
            return "Es un polígono de {} lados".format(self.numLados)

    def determinante(self, p1, p2):
        return p1.x * p2.y - p2.x * p1.y

    def area(self):
        n = len(self.puntos)
        suma = 0
        puntos = self.puntos + [self.puntos[0]]
        for i in range(n):
            suma = suma + Poligono.determinante(self, puntos[i], puntos[i + 1])
        return suma / 2

    def obtenCentro(self):
        centroX = 0
        centroY = 0
        n = len(self.puntos)
        for i in range(n):
            centroX = centroX + self.puntos[i].x
            centroY = centroY + self.puntos[i].y
        return centroX, centroY

    def distancia(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        d = math.sqrt(dx ** 2 + dy ** 2)
        return d

    def perimetro(self):
        n = len(self.puntos)
        d = 0
        puntos = self.puntos + [self.puntos[0]]
        for i in range(n):
            d = d + Poligono.distancia(self, puntos[i], puntos[i + 1])
        return d

    def obtenPuntos(self):
        for i in range(self.numLados):
            print("Punto {} : {}".format(i + 1, self.puntos[i]))
        return self.puntos

    def representa(self):
        x = []
        y = []
        for i in range(self.numLados):
            x.append(self.puntos[i].x)
            y.append(self.puntos[i].y)
            print("Valor de X [", i+1, "] es: ", x[i])
            print("Valor de Y [", i+1, "] es: ", y[i])
        x.append(self.puntos[0].x)
        y.append(self.puntos[0].y)
        plt.plot(x, y, color)
        print("Éste polígono:")
        plt.title(print(self.__str__()))
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()


# FIGURA CERRADA 2
class Elipse(Figura_Cerrada):

    def __init__(self, centro, semieje1, semieje2, anchura, altura, color):
        # Figura_Cerrada.__init__(self, centro, color)
        Figura.__init__(self, color)
        self.centro = centro
        self.semieje1 = semieje1
        self.semieje2 = semieje2
        self.anchura = anchura
        self.altura = altura

    def __str__(self):
        return "Elipse"

    def centro(self):
        self.centro = (semieje1, semieje2)

    def perimetro(self):
        pass

    def area(self):
        return math.pi * self.semieje1 * self.semieje2

    def obtenCentro(self):
        return self.centro

    def longitud(self):
        return 3 * (self.semieje1 + self.semieje2) - math.sqrt((3 * self.semieje1 + self.semieje2) *
                                                               (3 * self.semieje2 + self.semieje1))

    def representa(self):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal', anchor="C")
        ax1.add_patch(
            patches.Ellipse(
                (self.semieje1, self.semieje2),  # (x,y)
                self.anchura,  # width
                self.altura,  # height
                angle=0,
                color=self.color
            )
        )
        plt.plot(semieje1, semieje2, color)
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()


# FIGURA CERRADA 3
class Circulo(Figura_Cerrada):
    def __init__(self, centro, radio, color):
        super().__init__(color)
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return "Círculo"

    def representa(self):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal', adjustable="datalim", anchor="C")
        ax1.add_patch(
            patches.Circle(
                self.centro,  # (x,y)
                self.radio,  # radio
                color=self.color,
                angle=0
            )
        )
        plt.plot(centro, color)
        plt.grid(True)
        plt.grid(color="0.3", linestyle=":", linewidth=1)
        plt.show()

    def centro(self):
        self.centro = (x, y)

    def perimetro(self):
        pass

    def area(self):
        return math.pi * self.radio ** 2

    def obtenCentro(self):
        return self.centro

    def longitud(self):
        return 2 * math.pi * self.radio


""" ----- MENÚ PARA SELECCIONAR LA FIGURA ----- """
seguir = True
while seguir:
    print("\nFIGURAS A VISUALIZAR \n"
          "--Para figuras abiertas--\n"
          "Quebrada\n"
          "Hiperbola\n"
          "Parabola\n"
          "Sinusoidal\n\n"
          "--Para figuras cerradas--\n"
          "Poligono\n"
          "Elipse\n"
          "Circulo\n")
    figura_deseada = input("¿Cuál desea?: \n")
    figura_deseada_lower = figura_deseada.lower()

    if figura_deseada_lower == "quebrada":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        numPuntos = int(input("¿Cuántos puntos?: "))
        q = Quebrada(numPuntos, color)
        q.ponPuntos()
        q.representa()

    elif figura_deseada_lower == "hiperbola":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        p = int(input("Punto central: (de 0 a 100) "))
        a = float(input("Punto a: (de 0.0 a 100) "))
        b = float(input("Punto b: (de 0.0 a 100) "))
        hip = Hiperbola(p, a, b, color)
        hip.representa()

    elif figura_deseada_lower == "parabola":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        a = float(input("Punto a: (de 0.0 a 100) "))
        b = float(input("Punto b: (de 0.0 a 100) "))
        c = float(input("Punto c: (de 0.0 a 100) "))
        par = Parabola(a, b, c, color)
        par.representa()

    elif figura_deseada_lower == "sinusoidal":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        print("Características de la señal")
        amplitud = float(input("Amplitud: "))
        frecuencia = float(input("Frecuencia: "))
        fase = float(input("Fase: (de 0.0 a 1) "))
        seno = Sinusoidal(amplitud, frecuencia, fase, color)
        seno.representa()
        periodo = seno.parametros()
        print("El periódo es {} segundos".format(periodo))

    elif figura_deseada_lower == "poligono":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        numLados = int(input("Número de Lados: "))
        obj = Poligono(numLados, color)
        obj.ponPuntos()
        print("\nValores:")
        obj.obtenPuntos()
        print("\nOtra representación:")
        obj.representa()

    elif figura_deseada_lower == "elipse":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        print("Coordenadas X, Y para determinar el centro")
        semieje1 = float(input("Valor X: "))
        semieje2 = float(input("Valor Y: "))
        centro = (semieje1, semieje2)
        anchura = float(input("Anchura: "))
        altura = float(input("Altura: "))
        elip = Elipse(centro, semieje1, semieje2, anchura, altura, color)
        elip.representa()

    elif figura_deseada_lower == "circulo":
        color = input("Rojo: r\n"
                      "Azul: b\n"
                      "Verde: g\n"
                      "Amarillo: y\n"
                      "¿Qué color?: ")
        print("Coordenadas X, Y para determinar el centro")
        x = float(input("Valor X: "))
        y = float(input("Valor Y: "))
        centro = (x, y)
        radio = float(input("Introduzca el Ratio: "))
        circulo = Circulo(centro, radio, color)
        circulo.representa()

    otra = input("¿Desea otra figura? (si/no): ")
    if otra == "no":
        seguir = False
