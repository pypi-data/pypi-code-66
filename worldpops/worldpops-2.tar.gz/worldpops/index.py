import world
import country_info

res = world.response()
countries = world.all_countries()
lis = []

def population(in_population):
    for i in countries:
        if res[i]['population'] == in_population:
            return(i)
    raise(KeyError('No countries have a population of ' + str(in_population)))

def rank(in_rank):
    for i in countries:
        if res[i]['rank'] == in_rank:
            return(i)
    raise(KeyError('No countries have are ranked ' + str(in_rank)))

def percent_change(in_percent_change):
    for i in countries:
        if res[i]['change']['percent'] == in_percent_change:
            return(i)
    raise(KeyError('No countries have a change of ' + str(in_percent_change) + '%'))

def net_change(in_net_change):
    for i in countries:
        if res[i]['change']['net'] == in_net_change:
            return(i)
    raise(KeyError('No countries have a net change of ' + str(in_net_change)))

def density(in_density):
    for i in countries:
        if res[i]['density'] == in_density:
            return(i)
    raise(KeyError('No countries have a density of ' + str(in_density)))
