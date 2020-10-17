# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

def hazard_vf_sum(components, hazard_expr, upper_limit=1.0):
    """
    Calculate mol-weighted hazard quantity (e.g. toxic or flammable).

    This approach is consistent with the calculations outlined in CGA P-20: Standard for the Classification of Toxic Gas Mixtures.

    :param components: dict of component -> volume_fraction, e.g. { 'H2S': 0.05, 'CO2': 0.95 }
    :param hazard_expr: function that will result in hazardous volume fraction given single argument of component
    (or 0/None if not hazardous)
    :param upper_limit: limit to value. If results are volume fraction, then default upper limit of 1.0 is reasonable.
    :return: mol/volume-weighted hazard level
    """
    frac = 0.0
    for component, vf in components.items():
        hazard = hazard_expr(component)
        if hazard:
            frac += vf / hazard
    result = 1.0 / frac if frac else None
    if result and (not upper_limit or (upper_limit and result <= upper_limit)):
        return result
    return None
