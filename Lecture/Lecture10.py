from math import pi, sqrt
from functools import reduce
import string

def shortestPath(Cities, Dists):
    if len(Cities) == 1: return 0
    else:
        return min(
            map(lambda nxtCit:
                    Dists[(Cities[0], Cities[nxtCit])]
                    + shortestPath(Cities[nxtCit:], Dists),
                range(1,len(Cities))
            ))
