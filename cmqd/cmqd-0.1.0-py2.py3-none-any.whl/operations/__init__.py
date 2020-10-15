from clearmacro.operations.login import Login
from clearmacro.operations.get_categories_for_universe import GetCategoriesForUniverse
from clearmacro.operations.list_markets_for_signal import ListMarketsForSignal

class Operations(Login, ListMarketsForSignal, GetCategoriesForUniverse, object):
    pass
