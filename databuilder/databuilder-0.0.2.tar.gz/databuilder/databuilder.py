from pandas import DataFrame


def create_df(config, n):
    """
    Create a Pandas DataFrame.

    Params:
        config: A dictionary containing fields and
                options for making the DataFrame
                (see docs for examples)
        n: Number of rows in the DataFrame

    Returns:
        Pandas DataFrame
    """
    
    fields = config.get('fields', None)
    options = config.get("options", {})

    if not 'fields':
        raise ValueError("Config missing `fields` attribute!")
    
    # create empty dataframe
    df = DataFrame()

    # append each series to the dataframe
    for column_name, field in fields.items():
        
        if field.__class__.__qualname__ == 'Custom':
            try:
                df[column_name] = field._to_series(df[field.base])
            except KeyError:
                raise ValueError(f"Custom field's `{field.base}` was not found")
        
        elif hasattr(field, 'depends_on') and field.depends_on:
            try:
                df[column_name] = field._to_series(n, df[field.depends_on])
            except:
                raise ValueError(f"Name field's `{field.depends_on}` was not found")
        
        else:
            df[column_name] = field._to_series(n)

    # handle options
    if 'correlation' in options:

        corr = options['correlation']

        fs = {k:v for k,v in fields.items() if k in corr.columns}
        df = corr._apply_correlation(df, fs, n)

    return df