# -*- coding: utf-8 -*-
"""
Created on Mar 2, 2016

@author: Derek Wood
"""

from datetime import date, datetime
import json
import logging
from operator import attrgetter

import typing
from sqlalchemy import types
from sqlalchemy.sql import or_, and_
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.expression import desc
import sqlalchemy.sql.expression
from sqlalchemy.sql.functions import func

import pyjTable

DEFAULT_DATE_FORMATSTR = "{0:%Y-%m-%d}"


class JTable(object):
    def __init__(self, columns: typing.List[pyjTable.Column] = None, query_table=None):
        """
        Initializes the object with the attributes needed

        Parameters
        ----------
        columns : list of Column objects
        query_table: sqlalchemy table to query
        """
        self.log = logging.getLogger(__name__)

        self.query_table = query_table

        # In case we are passed an iterable and not a list
        if columns:
            if isinstance(columns, list):
                self._columns = columns
            else:
                self._columns = list(columns)
        else:
            self._columns = list()
        self.defaultPageSize = 25
        self.add_column_names()
        self.searchField = 'sSearch'
        self.outputMode = 'jTable'

    @property
    def columns(self) -> typing.List[pyjTable.Column]:
        return self._columns

    def add_column_names(self):
        col_num = 0
        for c in self.columns:
            col_num += 1
            if not c.column_name:
                c.column_name = "column_{}".format(col_num)

    def fields_definition(self, arguments=None):
        js_str = "{\n"
        delim = ""
        colNum = 0
        for c in self.columns:
            colNum += 1
            js_str += delim + c.javascript_definition(arguments)
            delim = ",\n"
        js_str += "}\n"
        return js_str

    def build_query(self, session):
        """Builds a a SQL Alchemy query on the session provided
         Parameters
        ----------
        session : a SQL Alchemy session
        """

        # Get a list of just the SQL Alchemy column objects
        # Note: label is used so we can get columns by name and not just position
        if self.query_table is not None:
            query = session.query(self.query_table)
        else:
            sa_columns = list()
            joins = list()
            for c in self.columns:
                if c.saColumn is not None:
                    saCol = c.saColumn
                    if hasattr(saCol, 'type'):
                        sa_columns.append(saCol.label(c.column_name))
                    else:
                        joins.append(saCol.class_)
            query = session.query(*sa_columns)
            for join_tbl in joins:
                try:
                    query = query.join(join_tbl)
                except sqlalchemy.exc.InvalidRequestError:
                    pass
        return query

    def results_structure(self, results, record_count=None, request=None):
        """
        Outputs the results in the structure needed by jTable or jQuery

        Parameters
        ----------
        results : list of row dicts
        record_count : number of records
        request: pyramid request
        """
        # TODO: Change outputMode to be a property with setter that validates
        # TODO: Add class OutputModes to contain valid choices
        if self.outputMode == 'jTable':
            output = dict()
            if record_count is None:
                record_count = len(results)
            output['TotalRecordCount'] = str(record_count)
            output['Result'] = u'OK'
            output['Records'] = results
        elif self.outputMode == 'jTableOptions':
            output = dict()
            output['Result'] = u'OK'
            output['Options'] = results
        elif self.outputMode == 'select2':
            output = dict()
            (_, stop) = self.get_paging_start_stop(request)
            pagination = dict()
            output['pagination'] = pagination
            if stop < record_count:
                pagination['more'] = 'true'
            else:
                pagination['more'] = 'false'
            output['results'] = results
            # TODO: Provide a way to specify a grouping field to get results to look like this Hierarchical data:
            # ===============================================================
            # results: [
            #     { text: "Western", children: [
            #         { id: "CA", text: "California" },
            #         { id: "AZ", text: "Arizona" }
            #     ] },
            #     { text: "Eastern", children: [
            #         { id: "FL", text: "Florida" }
            #     ] }
            # ]
            # ===============================================================
            # The object may also contain a disabled boolean property indicating whether this result can be selected.
        else:
            output = results
        return output

    def results_structure_json(self, results, record_count=None, request=None):
        json_str = json.dumps(self.results_structure(results, record_count, request=request))
        return json_str

    def format_result_row(self, sa_object):
        table_row_dict = dict()

        for col in self.columns:
            # self.log.debug("col = {}".format(col))
            table_column_name = col.column_name
            col_val = None
            if col.attribute_name is not None:
                for attr_parts in col.attribute_name.split('.'):
                    if col_val is None:
                        col_val = getattr(sa_object, attr_parts)
                    else:
                        col_val = getattr(col_val, attr_parts)
            elif col.saColumn is not None:
                # self.log.debug("tableColumnName = {}".format(tableColumnName))
                try:
                    col_val = getattr(sa_object, table_column_name)
                except AttributeError:
                    # Try getitem for SA Core query results or dict
                    try:
                        col_val = sa_object[table_column_name]
                    # pylint: disable=broad-except
                    except Exception as e:
                        col_val = 'could not find {}'.format(table_column_name)
                        self.log.exception(e)
            if col_val is not None:
                # self.log.debug("colVal = {}".format(col_val))
                if col.formatStr:
                    try:
                        col_val = ('{:' + col.formatStr + '}').format(col_val)
                    except ValueError as err:
                        message = err.args[0] or ''
                        message += " formatStr={}".format(col.formatStr)
                        message += " colVal={}".format(col_val)
                        err.args = (message,) + err.args[1:]
                        raise err

                # Check if we still have a date after applying explicit formatStr, if so use the default format
                if isinstance(col_val, date) or isinstance(col_val, datetime):
                    col_val = DEFAULT_DATE_FORMATSTR.format(col_val)
                    # log.debug("date {} => {}".format(beforeVal, colVal))
                col_val = str(col_val)
            else:
                col_val = ''

            table_row_dict[table_column_name] = col_val
        return table_row_dict

    def format_result_rows(self, results):
        # Translate SQL Alchemy rows into table rows
        result_rows = []
        for row in results:
            # log.debug("row = {}".format(row))
            result_rows.append(self.format_result_row(row))
        return result_rows

    def get_result_rows_tuple(self, query=None, session=None, request=None) -> tuple:
        """
        Using SA Query, launch apply_filter, apply_sort and apply_paging processes to modify the query
        and get a total row count and page results.
        """
        if not query:
            if session:
                query = self.build_query(session)
            else:
                raise ValueError("Either query or session parameter must be provided")
        # If we were provided with a request object, alter the query with it
        if request:
            # the term entered in the datatable's search box
            self.log.debug("Applying filter")
            query = self.apply_filter(query, request)

            self.log.debug("Getting filtered record count")
            try:
                # Make a version of the query with just the key columns for the count
                # that will use far less memory and time.
                if session is not None:
                    sa_key_columns = list()
                    for col in self.columns:
                        if col.key and col.saColumn:
                            sa_key_columns.append(col.saColumn)
                    count_query = session.query(*sa_key_columns)
                    record_count = count_query.count()
                else:
                    record_count = query.count()
                self.log.debug("record count={}".format(record_count))
            except AttributeError:
                record_count = None

            # field chosen to sort on
            self.log.debug("Applying sort")
            query = self.apply_sort(query, request)

            # pages have a 'start' and 'length' attributes
            self.log.debug("Applying paging")
            query = self.apply_paging(query, request)
        else:
            self.log.debug("Processing query results with no browser request processing of filters, sorting, or paging")
            self.log.debug("Getting filtered record count")
            try:
                record_count = query.count()
                self.log.debug("record count={}".format(record_count))
            except AttributeError:
                record_count = None

        # fetch the result of the queries
        self.log.debug("Running query")
        results = query.all()

        result_rows = self.format_result_rows(results)

        return result_rows, record_count

    def get_result_rows_tuple_from_list(self, results_list, request=None) -> tuple:
        """
         Using list of rows, apply the filter, sorting and paging processes and get a total row count and page results.
        """
        # If we were provided with a request object, alter the results_list with it
        if request:
            # the term entered in the datatable's search box
            self.log.debug("Applying filter")
            results_list = self.apply_filter_list(results_list, request)

            self.log.debug("Getting filtered record count")
            record_count = len(results_list)
            self.log.debug("record count={}".format(record_count))

            # field chosen to sort on
            self.log.debug("Applying sort")
            results_list = self.apply_sort_list(results_list, request)

            # pages have a 'start' and 'length' attributes
            self.log.debug("Applying paging")
            results_list = self.apply_paging_list(results_list, request)
        else:
            self.log.debug("Processing query results with no browser request processing of filters, sorting, or paging")
            self.log.debug("Getting filtered record count")
            record_count = len(results_list)

        result_rows = self.format_result_rows(results_list)

        return result_rows, record_count

    def get_result_rows(self, query=None, session=None, request=None):
        return self.get_result_rows_tuple(query, session, request)[0]

    def get_results(self, query=None, session=None, request=None):
        """
        Get results from SA query
        """
        (result_rows, record_count) = self.get_result_rows_tuple(query, session, request)
        return self.results_structure(result_rows, record_count, request=request)

    def get_results_from_list(self, results_list, request=None):
        (result_rows, record_count) = self.get_result_rows_tuple_from_list(results_list, request)
        return self.results_structure(result_rows, record_count, request=request)

    def get_results_from_sql(self, sql, session, request=None):
        column_list = [c.column_name for c in self.columns]
        query1 = session.query(*column_list).from_statement(sqlalchemy.sql.expression.text("(" + sql + ")"))
        query1.is_selectable = True

        count_qry = session.query(func.count(1)).select_from(query1)
        # print count_qry
        record_count = count_qry.scalar()

        query = session.query(*column_list).select_from(query1)
        # print query
        (result_rows, _) = self.get_result_rows_tuple(query, session, request)
        return self.results_structure(result_rows, record_count, request=request)

    def apply_filter(self, query, request):
        """Modifies the query, by adding filter on all any columns matched in the search form
        """

        # NOTE: To guard against SQL Injection we use SQL Alchemy's operators ilike, __eq__
        # DO NOT GENERATE TEXT WHERE CLAUSE ELEMENTS!
        where_clause = None
        self.log.debug('Checking for all columns search criteria in {}'.format(self.searchField))
        search_value_list = request.params.get(self.searchField)
        if search_value_list and search_value_list != '':
            self.log.debug('All columns search criteria found: {}'.format(search_value_list))
            conditions = list()
            for col in self.columns:
                try:
                    if col.searchSAColumn:
                        sa_col = col.searchSAColumn
                    else:
                        sa_col = col.saColumn
                    if sa_col is None:
                        continue
                    if col.searchable:
                        if col.searchUsingLike:
                            self.log.debug('{} ilike {}'.format(sa_col, search_value_list))
                            conditions.append(sa_col.ilike(r'%{}%'.format(search_value_list)))
                        elif isinstance(col.saColumn.type, types.String):
                            self.log.debug('{} == {} str'.format(sa_col, search_value_list))
                            conditions.append(sa_col.__eq__(search_value_list))
                        else:
                            self.log.debug(
                                'not searching non-string column {} == {}'.format(repr(col), search_value_list))
                except TypeError as e:
                    self.log.exception(e)
                    self.log.error("Could not add filter on %s = %s", col, search_value_list)
            self.log.debug("  added conditions {}".format(conditions))
            where_clause = or_(*conditions)
            self.log.debug("  added where_clause {}".format(where_clause))

        conditions = list()
        joins = list()
        for col in self.columns:
            if col.searchSAColumn:
                sa_col = col.searchSAColumn
            else:
                sa_col = col.saColumn
            if sa_col is None:
                continue
            if col.searchable:
                self.log.debug('Checking for search criteria on {}'.format(col.searchField))
                search_value_raw_list = request.params.getall(col.searchField)
                search_value_list = list()

                # Get rid of blank or null entries
                for search_entry in search_value_raw_list:
                    if search_entry and search_entry != '':
                        search_value_list.append(search_entry)

                if search_value_list:
                    if hasattr(sa_col, 'class_'):
                        joins.append(sa_col.class_)
                    if col.searchUsingLike:
                        or_list = list()
                        for search_val_entry in search_value_list:
                            self.log.debug('{} ilike {}'.format(sa_col, search_val_entry))
                            or_list.append(sa_col.ilike(r'%{}%'.format(search_val_entry)))
                        conditions.append(or_(*or_list))
                    elif isinstance(sa_col.type, types.String):
                        self.log.debug('{} in {} str'.format(sa_col, search_value_list))
                        conditions.append(sa_col.in_(search_value_list))
                    else:
                        self.log.debug("{} in {}".format(sa_col, search_value_list))
                        conditions.append(sa_col.in_(search_value_list))
                        # conditions.append("{} = '{}'".format(sa_col, search_value_list))

        if where_clause is not None:
            # We already had all fields search conditions
            where_clause = and_(where_clause, and_(*conditions))
        else:
            # Otherwise just and together the column specific filters
            where_clause = and_(*conditions)
        self.log.debug("Final where_clause {}".format(where_clause))

        if where_clause is not None:
            query = query.filter(where_clause)

        for join_tbl in joins:
            try:
                query = query.join(join_tbl)
                self.log.debug("Added join to {}".format(join_tbl))
            except sqlalchemy.exc.InvalidRequestError as e:
                self.log.debug("Skip join to {} {}".format(join_tbl, repr(e)))

        return query

    def apply_filter_list(self, results_list, request):
        """
        Modifies the results_list, by adding filter on all any columns matched in the search form
        """

        new_results_list = list()
        self.log.debug('Checking for all columns search criteria in {}'.format(self.searchField))
        search_value = request.params.get(self.searchField)
        if search_value:
            self.log.debug('All columns search criteria found: {}'.format(search_value))
            for row in results_list:
                row_matches = False
                for col in self.columns:
                    if col.searchable:
                        if col.searchUsingLike:
                            self.log.debug('{} ilike {}'.format(col, search_value))
                            if search_value in results_list[col]:
                                row_matches = True
                        elif isinstance(col.saColumn.type, types.String):
                            self.log.debug('{} == {} str'.format(col, search_value))
                            if search_value.upper() == results_list[col].upper():
                                row_matches = True
                        else:
                            self.log.debug('{} == {}'.format(col, search_value))
                            if search_value == results_list[col]:
                                row_matches = True
                if row_matches:
                    new_results_list.append(row)
            results_list = new_results_list

        new_results_list = list()
        for row in results_list:
            row_matches = True
            for col in self.columns:
                if col.searchable:
                    # self.log.debug('Checking for search criteria on {}'.format(col.searchField))
                    search_value = request.params.get(col.searchField)

                    if search_value:
                        if col.searchUsingLike:
                            self.log.debug('{} ilike {}'.format(col, search_value))
                            if search_value not in row[col]:
                                row_matches = False
                        elif isinstance(col.saColumn.type, types.String):
                            self.log.debug('{} == {} str'.format(col, search_value))
                            if search_value.upper() != row[col].upper():
                                row_matches = False
                        else:
                            self.log.debug('{} == {}'.format(col, search_value))
                            if search_value != row[col]:
                                row_matches = False

            if row_matches:
                new_results_list.append(row)

        return new_results_list

    def get_sa_column(self, column_name):
        # We could create a Columnname based dict. However at init time the columnName might not be set.
        for c in self.columns:
            if c.column_name == column_name:
                if c.searchSAColumn is not None:
                    return c.searchSAColumn
                else:
                    return c.saColumn

    def apply_sort(self, query, request):
        """Modify the query by adding order by on the columns requested
        """
        if 'jtSorting' in request.params:
            self.log.debug("Sorting={}".format(request.params['jtSorting']))
            sort_terms = request.params['jtSorting'].split(',')
            for term in sort_terms:
                if term != '':
                    term_parts = term.split()

                    col_name = term_parts[0]
                    col = self.get_sa_column(col_name)
                    if col:
                        # only order by real columns
                        if hasattr(col, 'type'):
                            if len(term_parts) == 2:
                                direction = term_parts[1].upper()
                            else:
                                direction = 'ASC'
                            self.log.debug("  Sort on {}={} {}".format(col_name, col, direction))
                            # We need to have a cross-walk to turn the  column name back into an SA column name
                            query = query.order_by(
                                asc(col).nullsfirst() if direction == 'ASC' else desc(col).nullslast())
        return query

    def apply_sort_list(self, results_list, request):
        """Modify the query by adding order by on the columns requested
        """
        if 'jtSorting' in request.params:
            self.log.debug("Sorting={}".format(request.params['jtSorting']))
            sort_terms = request.params['jtSorting'].split(',')
            # print sort_terms
            for term in reversed(sort_terms):
                if term != '':
                    term_parts = term.split()

                    col_name = term_parts[0]
                    direction = term_parts[1].upper()
                    reverse = (direction != 'ASC')
                    self.log.debug("  Sort on {} {}".format(col_name, direction))
                    # We need to have a cross-walk to turn the  column name back into an SA column name
                    results_list = sorted(results_list, key=attrgetter(col_name), reverse=reverse)
        return results_list

    def get_paging_start_stop(self, request) -> tuple:
        start = 0
        length = self.defaultPageSize

        if (
                'jtPageSize' in request.params
                and ('jtStartIndex' in request.params or 'jtPageNumber' in request.params)
        ):

            length = int(request.params['jtPageSize'])

            if 'jtStartIndex' in request.params:
                start = int(request.params['jtStartIndex'])
            else:  # 'jtPageNumber' in request.params
                start = length * int(request.params['jtPageNumber'])

            self.log.debug("page start = {}".format(start))
            self.log.debug("page length = {}".format(length))

        stop = start + length
        return start, stop

    def apply_paging(self, query, request):
        """Modify the query by slicing to the requested page of rows
        """
        (start, stop) = self.get_paging_start_stop(request)
        return query.slice(start, stop)

    def apply_paging_list(self, results_list, request):
        """Modify the results_list by slicing to the requested page of rows
        """
        (start, stop) = self.get_paging_start_stop(request)
        return results_list[start:stop]
