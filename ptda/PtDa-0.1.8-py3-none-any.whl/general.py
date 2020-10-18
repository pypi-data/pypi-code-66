import pandas as pd
import numpy as np
import itertools

"""
pmr is a function to calulcate permutation with repetition and form the possible arrangement as a result.
Where x is a set of objects and r is number of objects selected
"""
def pmr(x,r):
    output = [p for p in itertools.product(x, repeat=r)]
    pmr = pd.DataFrame({})
    for i in np.vstack(output):
        pmr = pmr.append([i])
    return pmr