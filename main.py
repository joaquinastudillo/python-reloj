import stddraw
from reloj import *
import time

def iniciarSegundero(x0, y0, x1, y1, reloj):
    stddraw.line(x0, y0, x1, y1)
    reloj.sumarSegundos()
    print(reloj.segundos)

reloj = Reloj(1,2,3)

stddraw.setCanvasSize(700, 700)
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
stddraw.setPenRadius(0.001)
stddraw.circle(0.0, 0.0, 1.0)

stddraw.line(0, 0, 0, 1)
stddraw.show(0)

while True:
    stddraw.clear(stddraw.LIGHT_GRAY)
    stddraw.circle(0.0, 0.0, 1.0)
    punto = reloj.actualizarSegundero()
    iniciarSegundero(0, 0, punto[0]*-1, punto[1], reloj)
    stddraw.show(0)
    time.sleep(1)
