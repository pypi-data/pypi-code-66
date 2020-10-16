"""\
visaplan.zope.reldb: configure a data source name

Thst's it, for now.
"""
# Python compatibility:
from __future__ import absolute_import

# Zope:
from App.config import getConfiguration

__all__ = [
    'get_dsn',  # get configured data source name
    ]

def get_dsn(product='reldb', key='dsn'):
    """
    Get the data source name from the Zope configuration
    for the reldb "product"
    """
    global_conf = getConfiguration()
    product_conf = global_conf.product_config.get(product, {})
    return product_conf[key]
