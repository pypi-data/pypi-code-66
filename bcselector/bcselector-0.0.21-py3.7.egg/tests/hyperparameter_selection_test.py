import unittest
import numpy as np
import pandas as pd

from bcselector.variable_selection import DiffVariableSelector, FractionVariableSelector, NoCostVariableSelector
from bcselector.data_generation import MatrixGenerator, DataFrameGenerator


class TestFVS_r_paramter(unittest.TestCase):
    def test_criterion_values(self):
        # Given
        def fvs_find_optimal_parameter(X, y, costs, j_criterion, budget, r, **kwargs):
            scores = []
            scores_l = []
            for r_single in r:
                fvs = FractionVariableSelector()
                fvs.fit(data=X, target_variable=y, costs=costs, r=r_single, j_criterion_func=j_criterion, budget=budget, stop_budget=True, **kwargs)
                
                scores.append(sum(fvs.criterion_values))
                scores_l.append(fvs.criterion_values)
            return r, scores, scores_l
        
        mg = MatrixGenerator()
        X,y,costs = mg.generate(n_rows = 100, n_basic_cols = 5, loc = 0, basic_cost = 1, noise_sigmas = [0.1,0.5,5,10,15,50], round_level = 3)

        a,b,c = fvs_find_optimal_parameter(X=X, 
                           y=y, 
                           costs=costs,
                           j_criterion='mifs', 
                           budget=1,
                           r=[0, 0.1, 100],
                           beta=0.1)
        a