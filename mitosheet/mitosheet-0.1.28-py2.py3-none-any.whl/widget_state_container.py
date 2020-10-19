#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

from typing import Dict, Union, List
import pandas as pd
import json
from copy import deepcopy

from mitosheet.sheet_functions import FUNCTIONS
from mitosheet.topological_sort import creates_circularity, topological_sort_columns
from mitosheet.evaluate import parse_formula
from mitosheet.utils import empty_column_python_code, dfs_to_json
from mitosheet.transpile import transpile
from mitosheet.errors import (
    make_no_sheet_error,
    make_column_exists_error,
    make_no_column_error,
    make_wrong_column_metatype_error,
    make_unsupported_function_error,
    make_circular_reference_error,
    make_execution_error,
    EditError
)


class WidgetStateContainer():
    """
    Holds all private widget state used by the evaluator and transpiler. 

    Is responsible for updating this state and maintaining correctness, 
    even in the case of invalid updates.

    Each state variable is a list where there is one entry for each
    dataframe passed to the WidgetStateContainer.
    """

    def __init__(self, dfs: pd.DataFrame):
        self.curr_step_id = 0

        self.steps = {0: {
            'step_type': 'formula',
            'column_metatype': [{key: 'value' for key in df.keys()} for df in dfs],
            'column_spreadsheet_code': [{key: '' for key in df.keys()} for df in dfs],
            'column_python_code': [{key: empty_column_python_code() for key in df.keys()} for df in dfs],
            'column_evaluation_graph': [{key: set() for key in df.keys()} for df in dfs],
            'dfs': dfs
        }}

    @property
    def curr_step(self):
        """
        Returns the current step object as a property of the object,
        so reference it with self.curr_step
        """
        return self.steps[self.curr_step_id]

    @property
    def num_sheets(self):
        """
        Duh. :)
        """
        return len(self.steps[self.curr_step_id]['dfs'])

    @property
    def dfs(self):
        return self.steps[self.curr_step_id]['dfs']

    @property
    def sheet_json(self):
        """
        sheet_json contains a serialized representation of the data
        frames that is then fed into the ag-grid in the front-end. 
        """
        return dfs_to_json(self.curr_step['dfs'])

    @property
    def column_spreadsheet_code_json(self):
        """
        column_spreadsheet_code_json is a list of all the spreadsheet
        formulas that users have used, for each sheet they have. 
        """
        return json.dumps(self.curr_step['column_spreadsheet_code'])

    @property
    def code_json(self):
        """
        This code json string is sent to the front-end and is what
        ends up getting displayed in the codeblock. 
        """
        return json.dumps(transpile(self))

    def handle_edit_event(self, edit_event):
        """
        Updates the widget state with the edit_event, and errors
        if the event is invalid. 
        """
        if edit_event['type'] == 'cell_edit':
            sheet_index = edit_event['sheet_index']
            column_header = edit_event['address']
            old_formula = edit_event['old_formula']
            new_formula = edit_event['new_formula']
            self.set_column_formula(sheet_index, column_header, old_formula, new_formula)
        elif edit_event['type'] == 'add_column':
            sheet_index = edit_event['sheet_index']
            column_header = edit_event['column_header']
            self.add_column(sheet_index, column_header)   
        elif edit_event['type'] == 'merge':
            # construct new data frame with merged data 
            self.merge_sheets(
                edit_event['sheet_index_one'],
                edit_event['merge_key_one'],
                edit_event['sheet_index_two'],
                edit_event['merge_key_two']
            )
        else:
            raise Exception(f'{edit_event} is not an edit event!')

    def handle_sheet_update_event(self, sheet_update_event):
        """
        Updates the widget state with the sheet_update_event, and errors
        if the event is invalid. 
        """
        if sheet_update_event['type'] == 'column_spreadsheet_code':
            column_spreadsheet_code_array = json.loads(sheet_update_event['column_spreadsheet_code_array'])
            self.set_column_spreadsheet_code(column_spreadsheet_code_array)
        else:
            raise Exception(f'{sheet_update_event} is not a sheet update event!')


    # TODO: We need to update this. when we create the step after the merge step, for example,
    # we don't want to take the merge_code componenet of the step. This should only copy over 
    # the persisting step data. 
    def create_and_checkout_new_step(self, new_step_id, step_type):
        """
        Creates a new step with new_step_id and step_type that starts
        with the ending state of the previous step
        """
        # new_step_id should always be greater than 0
        if new_step_id < 1:
            raise Exception(f'you can\'t insert a step before mito was created!')

        # the new step is a copy of the previous step
        new_step = deepcopy(self.steps[new_step_id - 1])
        # make sure the new step has the correct type
        new_step['step_type'] = step_type

        # add the new step to list of steps
        self.steps[new_step_id] = new_step

        # checkout the new step
        self.curr_step_id = new_step_id 

    def set_column_spreadsheet_code(self, column_spreadsheet_code_array: List[Dict[str, str]]):
        """
        If an analysis has already been run, then there are existing spreadsheet
        formulas in columns that are not known at the creation of this object.

        Thus, we update them after the fact!

        NOTE: we don't re-evaluate the JSON, as we assume it is matched up with the DF.
        TODO: this might be a bug, if you change the df before rerunning the analysis...
        """

        for sheet_index, column_spreadsheet_code in enumerate(column_spreadsheet_code_array):
            for column_header, spreadsheet_code in column_spreadsheet_code.items():
                # Skip columns without a formula!
                if spreadsheet_code == '':
                    continue

                self.curr_step['column_metatype'][sheet_index][column_header] = 'formula'
                # old_formula here is set as None, as nothing is defined as the formula
                # in the widget state container at this point!
                self.set_column_formula(
                    sheet_index,
                    column_header, 
                    None, 
                    spreadsheet_code,
                    evaluate=False
                )

    def add_column(self, sheet_index: int, column_header: str):
        """
        Adds a column. Errors if the column already exists
        """
        if column_header in self.curr_step['column_metatype'][sheet_index]:
            raise make_column_exists_error(column_header)

        # Update the state variables
        self.curr_step['column_metatype'][sheet_index][column_header] = 'formula'
        self.curr_step['column_spreadsheet_code'][sheet_index][column_header] = '=0'
        self.curr_step['column_python_code'][sheet_index][column_header] = empty_column_python_code()
        self.curr_step['column_python_code'][sheet_index][column_header]['column_formula_changes'] = f'df[\'{column_header}\'] = 0'
        self.curr_step['column_evaluation_graph'][sheet_index][column_header] = set()

        # Update the dataframe; this cannot cause an error!
        self.curr_step['dfs'][sheet_index][column_header] = 0

    def set_column_formula(
            self, 
            sheet_index: int,
            column_header: str, 
            old_formula: Union[str, None], 
            new_formula: str,
            evaluate: bool = True
        ):
        """
        Sets the column with column_header to have the new_formula, and 
        updates the dataframe as a result.

        Errors if:
        - The given column_header is not a column. 
        - The new_formula introduces a circular reference.
        - The new_formula causes an execution error in any way. 

        In the case of an error, this function rolls back all variables
        variables to their state at the start of this function.
        """

        # TODO: we need to make a column does not exist error, for this edit!

        # First, we check the column_metatype, and make sure it's a formula
        if self.curr_step['column_metatype'][sheet_index][column_header] != 'formula':
            raise make_wrong_column_metatype_error(column_header)

        # If nothings changed, there's no work to do
        if (old_formula == new_formula):
            return

        # Then we try and parse the formula
        new_python_code, new_functions, new_dependencies = parse_formula(
            new_formula, 
            column_header
        )

        # We check that the formula doesn't reference any columns that don't exist
        missing_columns = new_dependencies.difference(self.curr_step['column_metatype'][sheet_index].keys())
        if any(missing_columns):
            raise make_no_column_error(missing_columns)

        # The formula can only reference known formulas
        missing_functions = new_functions.difference(set(FUNCTIONS.keys()))
        if any(missing_functions):
            raise make_unsupported_function_error(missing_functions)

        # Then, we get the list of old column dependencies and new dependencies
        # so that we can update the graph
        old_python_code, old_functions, old_dependencies = parse_formula(old_formula, column_header)

        # Before changing any variables, we make sure this edit didn't
        # introduct any circularity
        circularity = creates_circularity(
            self.curr_step['column_evaluation_graph'][sheet_index], 
            column_header,
            old_dependencies,
            new_dependencies
        )
        if circularity:
            raise make_circular_reference_error()

        # Update the variables based on this new formula
        self.curr_step['column_spreadsheet_code'][sheet_index][column_header] = new_formula
        self.curr_step['column_python_code'][sheet_index][column_header]['column_formula_changes'] = new_python_code

        # Update the column dependency graph
        for old_dependency in old_dependencies:
            self.curr_step['column_evaluation_graph'][sheet_index][old_dependency].remove(column_header)
        for new_dependency in new_dependencies:
            self.curr_step['column_evaluation_graph'][sheet_index][new_dependency].add(column_header)

        # If we don't evaluate, we just return here...
        # TODO: maybe we should break the above out into it's own function?
        if not evaluate:
            return

        # Then we update the dataframe, first by executing on a fake dataframe
        try:
            df_copy = self.curr_step['dfs'][sheet_index].copy()
            # We execute on the copy first to see if there will be errors
            self._execute(df_copy, sheet_index)
        except Exception as e:
            # If there is an error during executing, we roll back all the changes we made
            self.curr_step['column_spreadsheet_code'][sheet_index][column_header] = old_formula
            self.curr_step['column_python_code'][sheet_index][column_header]['column_formula_changes'] = old_python_code

            # Update the column dependency graph back to what it was.
            for new_dependency in new_dependencies:
                self.curr_step['column_evaluation_graph'][sheet_index][new_dependency].remove(column_header)
            for old_dependency in old_dependencies:
                self.curr_step['column_evaluation_graph'][sheet_index][old_dependency].add(column_header)
            
            # And then we bubble the error up!
            if isinstance(e, EditError):
                # If it's an edit error, we propagate that up
                raise e
            else:
                # Otherwise, we turn it into an edit error!
                raise make_execution_error()
            
        # However, if there was no error in execution on the copy, we can execute on 
        # the real dataframe!
        self._execute(self.curr_step['dfs'][sheet_index], sheet_index)

    def merge_sheets(
            self,
            sheet_index_one: int,
            merge_key_one: str,
            sheet_index_two: int,
            merge_key_two: str
        ):
        """
        Creates a new sheet by merging sheet_index_one and sheet_index_two together
        on the keys merge_key_one and merge_key_two respectively. 
        
        The merged sheet will contain all of the columns from sheet_index_one 
        and sheet_index_two

        If either merge key does not exist, it raises an exception.
        """

        # First, we create a new step for this merge
        self.create_and_checkout_new_step(self.curr_step_id + 1, 'merge')


        # if the sheets don't exist, throw an error
        if not self.does_sheet_index_exist(sheet_index_one):
            raise make_no_sheet_error(sheet_index_one)

        if not self.does_sheet_index_exist(sheet_index_two):
            raise make_no_sheet_error(sheet_index_two)


        # We check that the merge doesn't use any columns that don't exist
        # TODO: update make_no_columns_error to use sheet names also
        missing_sheet_one_key = {merge_key_one}.difference(self.curr_step['column_metatype'][sheet_index_one].keys())
        if any(missing_sheet_one_key):
            raise make_no_column_error(missing_sheet_one_key)


        missing_sheet_two_key = {merge_key_two}.difference(self.curr_step['column_metatype'][sheet_index_two].keys())
        if any(missing_sheet_two_key):
            raise make_no_column_error(missing_sheet_two_key)

        
        # Then we update the dataframe, first by executing on a fake dataframe
        try:

            # make a copy of our data frame to test operate on 
            dfs_copy = deepcopy(self.curr_step['dfs'])

            # We execute on the copy first to see if there will be errors
            self._execute_merge(
                dfs_copy, 
                sheet_index_one, 
                sheet_index_two, 
                merge_key_one, 
                merge_key_two
            )
        except EditError as e:
            # If an edit error occurs, we propagate it upwards!
            raise e
        except Exception as e:
            raise make_execution_error()

        # if there was no error in execution on the copy, execute on real dataframes
        new_df = self._execute_merge(
                    self.curr_step['dfs'], 
                    sheet_index_one, 
                    sheet_index_two, 
                    merge_key_one, 
                    merge_key_two
                )    

        # update dfs by appending new df
        self.curr_step['dfs'] = (*self.curr_step['dfs'], (new_df))

        # update df indexes to start at 1
        display_df_one_number = sheet_index_one + 1
        display_df_two_number = sheet_index_two + 1
        display_new_df = self.num_sheets

        # write code for transpiler
        self.curr_step['merge_code'] = f'temp_df = df{display_df_two_number}.drop_duplicates(subset=\'{merge_key_two}\')\n    df{display_new_df} = df{display_df_one_number}.merge(df{display_df_two_number}, left_on=[\'{merge_key_one}\'], right_on=[\'{merge_key_two}\'], how=\'left\')'
        
        # update the step to save the variables needed to reconstruct the merge
        self.curr_step['sheet_index_one'] = sheet_index_one
        self.curr_step['sheet_index_two'] = sheet_index_two
        self.curr_step['merge_key_one'] = merge_key_one
        self.curr_step['merge_key_two'] = merge_key_two

        # create empty state for new sheet
        new_sheet_index = self.num_sheets - 1
        previous_step = deepcopy(self.steps[self.curr_step_id - 1])
        column_headers = list(previous_step['column_metatype'][sheet_index_one].keys()) + list(previous_step['column_metatype'][sheet_index_two].keys())
        # fill in state of new sheet with state of merged sheets
        self.curr_step['column_metatype'].append({column_header: 'value' for column_header in column_headers})
        self.curr_step['column_spreadsheet_code'].append({column_header: '' for column_header in column_headers})
        self.curr_step['column_python_code'].append({column_header: empty_column_python_code() for column_header in column_headers})
        self.curr_step['column_evaluation_graph'].append({column_header: set() for column_header in column_headers})

        # after done merging, we create and checkout a new formula step!
        self.create_and_checkout_new_step(self.curr_step_id + 1, 'formula')


    def does_sheet_index_exist(self, index):
        return not (index < 0 or index >= self.num_sheets)
    

    def _execute(self, df, sheet_index):
        """
        Executes the given state variables for  
        """

        topological_sort = topological_sort_columns(self.curr_step['column_evaluation_graph'][sheet_index])

        for column_header in topological_sort:
            # Exec the code, where the df is the original dataframe
            # See explination here: https://www.tutorialspoint.com/exec-in-python
            exec(
                self.curr_step['column_python_code'][sheet_index][column_header]['column_formula_changes'],
                {'df': df}, 
                FUNCTIONS
            )
        
    def _execute_merge(
        self, 
        dfs, 
        sheet_index_one, 
        sheet_index_two, 
        merge_key_one, 
        merge_key_two
        ):
        """
        Executes a merge on the sheets with the given indexes.
        
        Note we drop duplicates to avoid pairwise duplication on the merge. TODO: figure out how
        to simulate VLOOKUP style work better here...
        """

        temp_df = dfs[sheet_index_two].drop_duplicates(subset=merge_key_two)
        return dfs[sheet_index_one].merge(temp_df, left_on=[merge_key_one], right_on=[merge_key_two], how='left')









