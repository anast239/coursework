import math
from time import time

def Solution_Nastya(e, u):
    d = 1
    while e * d % u != 1:
        d += 1
    return d
