from collections import namedtuple
from math import pi

# value?
femto = 1E-15
pico = femto*1000
nano = pico*1000
micro = nano*1000
milli = micro*1000
centi = 1E-2
kilo = 1E3
mega = kilo*1000
giga = mega*1000

# conversions
deg2rad = pi/180
rad2deg = 180/pi


# FIXME: change grav const to km^3/sec^2?? orbits use km not m
# https://en.wikipedia.org/wiki/Standard_gravitational_parameter
# mu = GM
# G = standard gravitational parameter of celectial body
# M = mass of body

# radius [km]
# mass [kg]
# standard gravitational const [m^3/sec^2]
# tilt [deg]


Body = namedtuple("Body", "radius mass mu tilt")

to_km3 = 1/1000/1000/1000
# https://en.wikipedia.org/wiki/Earth
Earth = Body(6378.388, 5.97237E24, 3.986004418E14*to_km3, 23.4392811)

# https://en.wikipedia.org/wiki/Moon
Moon = Body(1737.4, 7.342e22, 4.9048695e12*to_km3, 1.5424)
