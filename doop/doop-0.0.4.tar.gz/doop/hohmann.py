import numpy as np
from .constants import Earth

def hohman(r1, r2, mu=Earth.mu)
    #
    # Description: Assuming circular orbits of radius r1 and r2 around the
    # central body described by mu, a hohmann transfer from r1 to r2 is
    # calculated. The total deltaV and time of flight are output.
    #
    # Input:  r1  = radius of orbit 1
    #         r2  = radius of orbit 2
    #         mu  = gravitational parameter of central body
    #
    # Output: dV  = total deltaV of hohmann transfer from r1 to r2
    #         TOF = total time of flight from orbit r1 to orbit r2
    #
    # Calculate the velocities at each circular orbit:
    v1 = np.sqrt(mu/r1)
    v2 = np.sqrt(mu/r2)

    # Calculated the semi-major axis of the transfer orbit:
    a = (r1+r2)/2

    # Calculate the velocities of the transfer orbit:
    v1t = np.sqrt(2*mu/r1 - mu/a)
    v2t = np.sqrt(2*mu/r2 - mu/a)

    # Calculate the deltaV at each r1 and r2:
    dv1 = abs(v1t - v1)
    dv2 = abs(v2t - v2)

    # Calculate the total deltaV and TOF:
    dV = dv1 + dv2
    TOF = np.pi*np.sqrt(a**3/mu)

    return (dV, TOF,)
