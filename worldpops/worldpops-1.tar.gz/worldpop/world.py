import requests

lis = []

def response():
        return(requests.get('https://worldpops.herokuapp.com/').json())

res = response()

def all_countries():
    return(res.keys())

countries = all_countries()

def all_populations():
    for i in all_countries():
        lis.append({
            "country": i,
            "population": res[i]['population']
        })
    return(lis)

def all_change():
    for i in all_countries():
        try:
            lis.append({
                "country": i,
                "change": {
                    'percent': res[i]['change']['percent'],
                    "net": res[i]['change']['net']
                }
            })
        except KeyError:
            lis.append({
                "country": i,
                "change": {
                    'percent': res[i]['change']['percent'],
                }
            })
    return(lis)

def all_ranks():
    for i in all_countries():
        lis.append({
            "country": i,
            "rank": res[i]['rank']
        })
    return(lis)

def top_population():
    for i in countries:
        lis.append(res[i]['population'])

    most = max(lis)

    for i in countries:
        if res[i]['population'] == most:
            return({
                "country": i,
                "population": res[i]['population']
            })

def top_change():
    for i in countries:
        lis.append(res[i]['change']['percent'])

    most = max(lis)

    for i in countries:
        try:
            if res[i]['change']['percent'] == most:
                return({
                    "country": i,
                    "change": {
                        "percent": res[i]['change']['percent'],
                        "net": res[i]['change']['net']
                    }
                })
        except:
            if res[i]['change']['percent'] == most:
                return({
                    "country": i,
                    "change": {
                        "percent": res[i]['change']['percent']
                    }
                })