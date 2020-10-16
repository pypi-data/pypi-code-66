

def new_query_multiple_dfs(_df1_arrays, _df1_name_arrays, _query, _spark):
    for df, df_name in zip(_df1_arrays, _df1_name_arrays):
        df.createOrReplaceTempView(df_name)
    query = _query
    df3 = _spark.sql(query)
    return df3