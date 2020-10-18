from random import choice, random
import statistics as st
import numpy as np
import pandas as pd
import warnings


warnings.filterwarnings('ignore', category=RuntimeWarning)


def _transform_sd(xs, sd):
    """
    Transforms a vector with a stdev of 1 to
    a newly specified stdev.
    """
    
    x_bar = st.mean(xs)
    z_scores = [(x-x_bar) for x in xs]
    new_xs = [((z*sd) + x_bar) for z in z_scores]

    return new_xs


def _random_cov_matrix(n):
    """
    Generates random correlation matrix (n x n)
    """

    mat = []
    for _ in range(n):
        mat.append( [1 for _ in range(n)] )

    possible_r = [round(x, 2) for x in np.append(np.arange(-.95, -.10, .05), np.arange(.15, 1, .05))]
    vals = [choice(possible_r) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                mat[i][j] = vals[(i+j-1)]

    return mat


class ExplicitCorrelation():
    """
    One possible option value for the "correlation"
    option that can be defined in ther `databuilder.create_df`
    configuration dictionary

    This option alters columns in the dataframe so that
    they loosly fit an explicit correlation matrix
    """
    
    def __init__(self, columns, matrix):
        """
        Create an instance of the ExplicitCorrelation class

        Params:
            columns: List of columns (as strings) that the correlation
                     will be applied to. NOTE: The order of this list
                     needs to match the values provided in the `matrix` param
            matrix: The correlation matrix for the columns given in the
                    `columns` param. This matrix should be N x N, where N
                    is the len(columns)
        """
        self.columns = columns
        self.matrix = matrix

    def _apply_correlation(self, df, fields, n):
        """
        Applies correlation adjustment to the required fields
        """
            
        # these checks could happen somewhere else too maybe
        means = []
        for f in fields.values():
            if f.__class__.__qualname__ == 'NormalDist':
                means.append(f.mean)
            else:
                raise ValueError('Correlated column must be of a `NormalDist` column')

        res = np.random.multivariate_normal(means, self.matrix, n).T

        for i,(f_name,f) in enumerate(fields.items()):
            res[i] = _transform_sd(res[i], f.sd)
            df[f_name] = pd.Series(map(lambda _: round(_, f.precision), res[i]))

        return df


class RandomCorrelation():
    """
    One possible option value for the "correlation"
    option that can be defined in ther `databuilder.create_df`
    configuration dictionary

    This option alters columns in the dataframe so that the
    provided columns have a random correlation between them
    """
    
    def __init__(self, columns):
        """
        Create an instance of the RandomCorrelation class

        Params:
            columns: List of columns (as strings) that the random
                     correlation will be applied to
        """
        self.columns = columns

    def _apply_correlation(self, df, fields, n):
        """
        Applies correlation adjustment to the required fields
        """

        # these checks could happen somewhere else too maybe
        means = []
        for f in fields.values():
            if f.__class__.__qualname__ == 'NormalDist':
                means.append(f.mean)
            else:
                raise ValueError('Correlated column must be of a `NormalDist` column')

        cov = _random_cov_matrix(len(fields))

        res = np.random.multivariate_normal(means, cov, n).T

        for i,(f_name,f) in enumerate(fields.items()):
            res[i] = _transform_sd(res[i], f.sd)
            df[f_name] = pd.Series(map(lambda _: round(_, f.precision), res[i]))

        return df