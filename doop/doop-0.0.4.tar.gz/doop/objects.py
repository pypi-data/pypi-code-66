
import requests
from .elements import COE
from colorama import Fore

# from collections import namedtuple

# SatelliteTLE = {
#     "Dragon": """DRAGON CRS-2
#     1 39115U 13010A   13062.62492353  .00008823  00000-0  14845-3 0   188
#     2 39115  51.6441 272.5899 0012056 334.2535  68.5574 15.52501943   306""",
#
#     "ISS": """ISS (ZARYA)
#     1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927
#     2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537""",
#
#     "DragonDemo": """CREW DRAGON DEMO-1
#     1 44063U 19011A   19062.34862786 -.10981604  00000-0 -22652+0 0  9998
#     2 44063  51.6335 167.4655 0006446 102.4656 353.9277 15.51500210   163""",
#
#     "ChinaSat": """CHINASAT 2D
#     1 43920U 19001A   19062.86574468 -.00000352  00000-0  00000+0 0  9995
#     2 43920   0.0402 293.1489 0001187  74.3893 235.4568  1.00273137   662"""
# }

celestrack = {
    "gps": "https://celestrak.com/NORAD/elements/gps-ops.txt",
    "stations": "https://celestrak.com/NORAD/elements/stations.txt"
}

def get_tles(w):
    if w not in celestrack:
        print(f"{Fore.RED}{w} is invalid; choose: {list(w.keys())}{Fore.RESET}")
        raise Exception

    f = celestrack[w]
    resp = requests.get(f)
    if resp.status_code != 200:
        raise Exception(f"{Fore.RED}Failed to get TLEs from: {f}{Fore.RESET}")

    # print(len(resp.text))
    # print(resp.text)

    d = resp.text.split("\r\n")
    # print(len(d))
    # print(d[:6])
    tles = []
    for i in range(0, len(d), 3):
        if d[i] is None:
            break
        s = "\n".join(d[i:i+3])
        tles.append(s)

    print(f">> Found {len(tles)} TLEs")
    return tles

def get_coes(w):
    tles = get_tles(w)

    coes = []
    for tle in tles:
        try:
            coes.append(COE.from_tle(tle))
        except Exception as e:
            print(f"{Fore.CYAN}{tle}{Fore.RESET}")
            print(f"{Fore.RED}*** {e} ***{Fore.RESET}")
    return coes
