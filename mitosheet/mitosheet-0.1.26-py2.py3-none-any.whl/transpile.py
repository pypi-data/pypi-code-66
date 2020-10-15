#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Exports the transpile function, which takes the backend widget
container and generates transpiled Python code.
"""

from mitosheet.mito_analytics import analytics, static_user_id
from .topological_sort import topological_sort_columns
from .sheet_functions import FUNCTIONS


def transpile(widget_state_container):
    """
    Takes the Python code in the widget_state_container and linearizes it
    so it can be consumed by the front-end. 
    
    When there are multiple sheets, the first sheets code is first, followed
    by the second sheets code, etc. 
    """
    analytics.track(static_user_id, 'transpiler_started_log_event')

    code = []
    
    for step_id in widget_state_container.steps:
        step = widget_state_container.steps[step_id]
        if step['step_type'] == 'formula':
            for sheet_index in range(len(step['column_evaluation_graph'])):

                topological_sort = topological_sort_columns(step['column_evaluation_graph'][sheet_index])

                for column in topological_sort:
                    column_code = step['column_python_code'][sheet_index][column]['column_formula_changes']
                    if column_code != '':
                        # We replace the data frame in the code with it's parameter name!
                        raw = step['column_python_code'][sheet_index][column]['column_formula_changes']
                        raw = raw.strip().replace('df', f'df{sheet_index + 1}')
                        code.append(raw)
        elif step['step_type'] == 'merge':
            code.append(step['merge_code'])

    # Make sure we write a valid python function
    if len(code) == 0:
        code = ['# Edit the sheet to create the analysis!', 'pass']

    functions = ','.join(FUNCTIONS.keys())

    analytics.track(static_user_id, 'transpiler_finished_log_event')

    return {
        'imports': f'from mitosheet import {functions}',
        'code': code
    }