
import numpy as np
from numpy import cos, sqrt, sin, pi
import attr

from .tle import parse_tle
from .constants import Earth, deg2rad
from rotations.rotations import R1,R2,R3,R313

degree_symbol = u"\xb0"

@attr.s()
class COE:
    a = attr.ib()
    e = attr.ib()
    i = attr.ib()
    raan = attr.ib()
    w = attr.ib()
    v = attr.ib()

    tle = attr.ib(default=None)

    def to_rv(self):
        return coe2rv(self.a, self.e, self.i, self.raan, self.w, self.v)

    @staticmethod
    def from_rv(R, V):
        """Returns the orbit in R(x,y,z)[km] and V(x,y,z)[km/sec]"""
        a, e, i, node, w, v = rv2coe(R, V)
        return COE(a, e, i, node, w, v)

    @staticmethod
    def from_tle(tle):
        a = parse_tle(tle)
        c = COE(*a.coe)
        c.tle = a
        return c

    @property
    def r(self):
        """Returns the scalar radius[km]"""
        return self.a*(1-self.e**2)/(1+self.e*cos(self.v*pi/180))

    @property
    def velocity(self):
        """Returns the scalar velocity[km/sec]"""
        mu = Earth.mu
        # non-circular orbit
        if self.e > 1e-6:
            return sqrt(mu*(2/self.r-1/self.a))
        # circular orbit
        return sqrt(mu/self.r)

    @property
    def period(self):
        mu = Earth.mu
        return 2*pi*sqrt(self.a**3/mu)

    def __str__(self):
        s = f"a: {self.a:.1f}km e: {self.e:.4f} i: {self.i:.1f}\xb0 RAAN: {self.raan:.1f}\xb0 w: {self.w:.1f}\xb0 v: {self.v:.1f}\xb0"
        return s


######################################################################

def rv2coe(R, V, mu=Earth.mu):
    """Given postion (R) and velocity (V) in an ECI frame, this returns
    the classical orbital elements: (a, e, i, node, w, v)
    """
    H = np.cross(R,V)

    v = np.linalg.norm(V)
    r = np.linalg.norm(R)
    energy = v*v/2 - mu/r
    a = -(mu/2)/(v*v/2-mu/r)

    E = np.cross(V,H)/mu - R/r
    e = np.linalg.norm(E)

    i = np.arccos(H[2]/np.linalg.norm(H))
    if i < 1e-5: # equitorial orbit
        node = 0
        if e < 1e-5:  # circular
            vv = R[0]/r if R[1] > 0 else 2*pi-R[0]/r
            w = np.NaN
        else: # elliptical
            w = np.arccos(E[0]/e) if E[1] > 0 else 2*pi - np.arccos(E[0]/e)
            vv = np.arccos(np.dot(E,R)/(e*r))
            if np.dot(R,V) < 0:
                vv = 2*pi - vv
    else:
        N = np.cross(np.array([0,0,1]), H)
        n = np.linalg.norm(N)

        node = np.arccos(N[0]/n)
        node = 2*pi-node if N[1] <0 else node

        w = np.arccos(np.dot(N,E)/(d*e))
        w = 2*pi-w if E[2]<0 else w

    return (a, e, i*180/pi, node*180/pi, w*180/pi, vv*180/pi)


def coe2rv(a, e, i, node, w, v, MU=Earth.mu, degrees=True):
    """Given the classical orbital elements (a, e, i, node, w, v), this
    returns the position (R) and the velocity (V) in an ECI frame

    - Semimajor-axis (a)[km]: orbit size
    - Eccentricity (e): orbit shape (0=circle, 1=line)
    - Inclination (i)[deg]: orbital plane inclination measure from ascending node
    - Argument of Perigee (w)[deg]: orbit orientation
    - Ascending Node (Omega)[deg]: location of ascending node
    - True Anomaly (v)[deg]: location of satellite in orbit relative to perigee
    - Mean Anomaly (M)[deg]: fictitious angle that varies linearly with time

    return: R(x,y,z)[km], V(x,y,z)[km/sec]
    """
    # MU = MU/1000/1000/1000  # FIXME?

    if degrees:
        i *= deg2rad
        node *= deg2rad
        w *= deg2rad
        v *= deg2rad

    p = a*(1-e**2)  # p = semi-latus rectum (semiparameter)
    R = np.zeros(3)
    V = np.zeros(3)
    sv = sin(v)
    cv = cos(v)
    det = 1/(1+e*cv)
    smup = np.sqrt(MU/p)

    ###  Position Coordinates in Perifocal Coordinate System
    # R[0] = p*cv / (1+e*cv) # x-coordinate (km)
    # R[1] = p*sv / (1+e*cv) # y-coordinate (km)
    # R[2] = 0                             # z-coordinate (km)
    # V[0] = -sqrt(MU/p) * sv       # velocity in x (km/s)
    # V[1] =  sqrt(MU/p) * (e+cv)   # velocity in y (km/s)
    # V[2] =  0                            # velocity in z (km/s)


    R[0] = p*cv * det     # x-coordinate (km)
    R[1] = p*sv * det     # y-coordinate (km)
    R[2] = 0              # z-coordinate (km)
    V[0] = -smup * sv     # velocity in x (km/s)
    V[1] =  smup * (e+cv) # velocity in y (km/s)
    V[2] =  0             # velocity in z (km/s)

    r313 = R313(-node, -i, -w)

    # Perifocal -> xyz
    R = r313.dot(R)
    V = r313.dot(V)

    return (R,V,)
