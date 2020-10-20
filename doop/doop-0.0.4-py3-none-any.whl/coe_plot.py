import numpy as np
from numpy import pi, sqrt, sin, cos
#from matplotlib import pyplot as plt

def perifocal(coe, f):
    """
    Given the COE for an orbit and the angle (f) from perisapsis (in
    radians), then this returns the (p,q) cartesian locationl

    https://www.sciencedirect.com/topics/engineering/perifocal-frame
    """
    p = coe.a * (1 - coe.e ** 2)
    pos = np.array([cos(f), sin(f)]) * p / (1 + coe.e * cos(f))
    return pos

def orbit(coe):
    """
    Produces the (x,y) or (p,q) locations with in the perifocal plan (always 2D)
    of the orbit. Allows a simple 2D plot in jupyter notebook with:

        r = orbit(coe)
        plt.plot(r[:,0], r[:,1],'--r')
        plt.grid(True);

    coe: Classical Orbital Elements
    return: numpy([(x,y),(x,y), ...]) which has a shape of (360,2)

    https://www.sciencedirect.com/topics/engineering/perifocal-frame
    """
    orb = np.zeros((360,2))
    deg2rad = pi/180
    for i,f in enumerate(range(360)):
        orb[i,:] = perifocal(coe, f*deg2rad)

    return orb
