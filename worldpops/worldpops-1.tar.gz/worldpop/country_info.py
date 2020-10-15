import requests
import world

res = world.response()

def data(country):
    return(res[country])

def population(country):
    return(res[country]['population'])

def rank(country):
    return(res[country]['rank'])

def percent_change(country):
    return(res[country]['change']['percent'])

def net_change(country):
    try:
        return(res[country]['change']['net'])
    except KeyError:
        raise KeyError(country + ' doesn\'t have net change data')

def density(country):
    try:
        return(res[country]['density'])
    except KeyError:
        raise KeyError(country + ' doesn\'t have density data')
