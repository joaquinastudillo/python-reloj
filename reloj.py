import numpy as np
import math

class Reloj(object):
    puntoBaseSegundero = np.array([0, 1])

    def __init__(self, hora, minutos, segundos):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    #recordar pasar angulos en radianes no en grados
    def actualizarSegundero(self):
        matrizRotacion = np.array(((math.cos(0.10472), math.sin(0.10472)), (math.sin(0.10472) * -1, math.cos(0.10472))))
        if(self.segundos == 0):
            #se define el ángulo de cada segundo en 6° => 360/60
            #se define punto de partida el vertice 0.0
            self.puntoBaseSegundero = self.puntoBaseSegundero.dot(matrizRotacion)
        #agregar else

        return self.puntoBaseSegundero

    def sumarSegundos(self):
        self.segundos = self.segundos + 1
