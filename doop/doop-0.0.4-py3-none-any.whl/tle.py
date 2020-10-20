from math import pi, pow
from datetime import datetime, timedelta, timezone
from doop.constants import Earth
from collections import namedtuple

from enum import IntFlag

ID = namedtuple("ID", "launch_year launch_number piece")
Object = namedtuple("Object", "name number classification")

EphemerisType = IntFlag("EphemerisType","SGP SGP4 SDP4 SGP8 SDP8")

TLE = namedtuple("TLE",
        'object '
        'id '
        'coe '
        'ballistic_coeffecient '
        'bstar '
        'line1 line2'
    )

OE = namedtuple("OE", "a e i raan w v")

def fix_classification(x):
    if x == "U":
        return "Unclassified"
    elif x == "C":
        return "Classified"
    elif x == "S":
        return "Secret"
    raise Exception(f"Invalid classification: {x}")

def fix_sci(x):
    """
    TLE have a shorthand for storing scientific numbers, just fixing it
    """
    # leading +/- can trip this up
    if x[0] == '+' or x[0] == '-':
        xx = x[1:]
    else:
        xx = x

    s = xx.split("-")
    ss = xx.split("+")
    if len(s) == 2:
        x = float(s[0] + "e-" + s[1])
    elif len(ss) == 2:
        s = ss
        x = float(s[0] + "e+" + s[1])
    else:
        x = float(xx)
    return x

def fix_dec(x):
    """
    TLE formate assumes a leading decimal point, just putting it back in
    """
    if x[0] == "-":
        ret = float("-0." + x[1:])
    else:
        ret = float("0." + x)
    return ret

def fix_year(year:int):
    # FIXME: need a better solution :)
    return 2000+year if year < 60 else 1900+year

def fix_epoch(day:float, year:int):
    """https://ubuntuforums.org/archive/index.php/t-2032246.html"""
    # print(f"day {day} year {year}")
    yr = fix_year(year)
    return datetime(year=yr, month=1, day=1, tzinfo=timezone.utc) + timedelta(days=day-1)


def parse_tle(tle:str):
    """
    Format
    https://en.wikipedia.org/wiki/Two-line_element_set
    https://celestrak.com/NORAD/documentation/tle-fmt.php
    https://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/SSOP_Help/tle_def.html

    AAAAAAAAAAAAAAAAAAAAAAAA
    1 NNNNNU NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN
    2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN

    ISS (ZARYA)
    1 25544U 98067A   20060.61908565  .00000737  00000-0  21434-4 0  9993
    2 25544  51.6436 165.6500 0005418 332.6966 228.1099 15.49204316215186

    TLE are in ECI frame
    """
    # name, onel, twol = tle.split("\n")
    tmp = tle.split("\n")
    if len(tmp) == 2:
        name = "unknown"
        onel = tmp[0]
        twol = tmp[1]
    elif len(tmp) == 3:
        name, onel, twol = tmp
    else:
        raise Exception(f"tle_parse: too many lines: {len(tmp)}")

    one = onel.split()
    two = twol.split()
    # print(f"name: {name}\n one: {one}\n two: {two}\n")

    cat = str(one[1]).strip()
    cl = fix_classification(cat[-1])
    obj = Object(name.strip(), int(cat[:-1]),cl)

    yr = fix_year(int(one[2][:2]))
    piece = str(one[2][-1])
    num = str(one[2][2:-1])
    id = ID(yr, num, piece)

    yr = int(one[3][:2])
    day = float(one[3][2:])
    # print("epoch", fix_epoch(day, yr))

    n = float(two[7][:11])  # mean motion, or period of orbit
    u = Earth.mu

    a = pow(u,1/3)/pow(2*n*pi/86400, 2/3)
    e = fix_dec(two[4])
    i = float(two[2])
    raan = float(two[3])
    w = float(two[5])
    v = float(two[6])

    # classic orbital elements: a e i raan w v
    coe = OE(a,e,i,raan,w,v)

    d = int(one[7])
    if d > 0:
        print(EphemerisType(d))
    # else:
    #     print(f"unknown ephemeris type: {d}")

    return TLE(
            obj,
            id,
            coe,
            # float(two[63:68]), # rev num at epoch - this number isn't useful/accurate
            float(one[4]), # ballistic coeff
            fix_sci(one[6]), # bstar
            # n, # mean motion
            # fix_sci(one[44:52]), # 2nd der mean motion
            onel,
            twol
        )
