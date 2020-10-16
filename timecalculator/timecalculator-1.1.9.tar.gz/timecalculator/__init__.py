import time


def sys_time():
    t1 = time.localtime()
    t2 = time.strftime("%a, %d %b %Y, %H:%M:%S", t1)
    return t2


def mintosec(minutes):
    t = minutes * 60
    return t


def htosec(hours):
    t = hours * 60 * 60
    return t


def daytosec(days):
    t = days * 24 * 60 * 60
    return t


def work_week():
    t = 1 * 5 * 24 * 60 * 60
    return t


def weektosec(weeks):
    t = weeks * 7 * 24 * 60 * 60
    return t


def weekend():
    return 2 * 24 * 60 * 60


def monthtosec(months):
    t = months * 30 * 24 * 60 * 60
    return t


def yeartosec(years):
    t = years * 365 * 24 * 60 * 60
    return t
