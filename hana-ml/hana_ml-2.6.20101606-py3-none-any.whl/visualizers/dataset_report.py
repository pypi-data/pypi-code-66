"""
This module contains report builders for dataset.

The following class is available:

    * :class:`DatasetReportBuilder`
"""

# pylint: disable=line-too-long
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=unused-variable
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
import time
import warnings
from enum import Enum, unique
import multiprocessing
import threading
import pandas as pd
from IPython.core.display import HTML, display
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from htmlmin.main import minify
from tqdm.notebook import tqdm
from hana_ml.algorithms.pal import stats
from hana_ml.dataframe import quotename
from hana_ml.visualizers.model_report import TemplateUtil, PlotUtil
from hana_ml.visualizers.eda import EDAVisualizer
from hana_ml.algorithms.pal.preprocessing import Sampling


class DatasetReportBuilder(object):
    """
    The DatasetReportBuilder instance can analyze the dataset and generate a report in HTML format.

    The generated report can be embedded in the notebook, including: \n
    - Overview
        - Dataset info
        - Variable types
        - High cardinality %
        - Highly skewed variables
    - Sample
        - Top ten rows of dataset
    - Variables
        - Numeric distributions
        - Categorical distributions
        - Variable statistics
    - Data Correlations
    - Data Scatter Matrix

    Examples
    --------
    Assume the dataset DataFrame is df, report builder is datasetReportBuilder.

    Analyze dataset:

    >>> datasetReportBuilder.build(df,key="ID")

    >>> datasetReportBuilder.build(df,key="ID",scatter_matrix_sampling=Sampling(method='every_nth', interval=5))

    Display dataset report:

    >>> datasetReportBuilder.generate_notebook_iframe_report()

    Generate dataset report:

    >>> datasetReportBuilder.generate_html_report('report_name')

    """

    def __init__(self):
        self.__data_analyzer = None

    def build(self, data, key, scatter_matrix_sampling: Sampling = None):
        """
        Build a report for dataset.

        Parameters
        ----------
        data : DataFrame
            DataFrame to use for the build dataset report.
        key : str
            Name of ID column.
        scatter_matrix_sampling : :class:`~hana_ml.algorithms.pal.preprocessing.Sampling`, optional
            Scatter matrix sampling.
        """
        self.__data_analyzer = DataAnalyzer(data, key, scatter_matrix_sampling)
        self.__data_analyzer.generate_report_html()

    def generate_html_report(self, filename):
        """
        Save dataset report as a html file.

        Parameters
        ----------
        filename : str
            Html file name.
        """
        if self.__data_analyzer is None:
            raise Exception('To generate a report, you must call the build method firstly.')

        TemplateUtil.generate_html_file('{}_dataset_report.html'.format(filename), self.__data_analyzer.get_report_html())

    def generate_notebook_iframe_report(self):
        """
        Render dataset report as a notebook iframe.

        """
        if self.__data_analyzer is None:
            raise Exception('To generate a report, you must call the build method firstly.')

        print('\033[31m{}'.format('In order to review the dataset report better, '
                                  'you need to adjust the size of the left area or hide the left area temporarily!'))
        display(HTML(self.__data_analyzer.get_iframe_report_html()))


@unique
class VariableType(Enum):
    # categorical
    CAT = "CAT"
    # numeric
    NUM = "NUM"
    # date
    DATE = "DATE"


class GenerateSVGStrThread(threading.Thread):
    def __init__(self, name, run_funcs, pbar):
        threading.Thread.__init__(self)
        self.name = name
        self.run_funcs = run_funcs
        self.results = []
        self.pbar = pbar

    def run(self):
        for func in self.run_funcs:
            self.results.append(func())
        self.pbar.update()

    def get_results(self):
        return self.results


class DataAnalyzer(object):
    def __init__(self, data, key, scatter_matrix_sampling: Sampling = None):
        self.data = data
        self.scatter_matrix_data = self.data
        if scatter_matrix_sampling:
            self.scatter_matrix_data = scatter_matrix_sampling.fit_transform(data=self.data)
        self.key = key
        self.conn_context = self.data.connection_context

        self.variables = self.data.columns
        self.variables_count = len(self.variables)
        self.variables_dtypes = self.data.dtypes()
        self.variables_describe = self.data.describe()
        self.rows_count = int(self.variables_describe.head(1).collect()['count'])
        self.col_stats = self.variables_describe.collect()
        self.col_stats_names = list(self.col_stats.columns.delete(0))
        self.col_stats_dict = {}
        for i in self.col_stats.index:
            row = self.col_stats.loc[i]
            self.col_stats_dict[row.values[0]] = list(row.values[1:])

        self.warnings_missing = {}
        self.warnings_cardinality = {}

        self.numeric = [i for i in self.variables if self.data.is_numeric(i)]
        self.categorical = [i[0] for i in self.variables_dtypes if (i[1] == 'NVARCHAR') or (i[1] == 'VARCHAR')]
        self.date = [i[0] for i in self.variables_dtypes if (i[1] == 'DATE') or (i[1] == 'TIMESTAMP')]

        self.variable_2_type_dict = {}

        for variable in self.numeric:
            self.variable_2_type_dict[variable] = VariableType.NUM

        for variable in self.categorical:
            self.variable_2_type_dict[variable] = VariableType.CAT

        for variable in self.date:
            self.variable_2_type_dict[variable] = VariableType.DATE

        self.__report_html = None
        self.__iframe_report_html = None

    def get_type(self, variable):
        return self.variable_2_type_dict.get(variable)

    def get_dataset_info(self):
        stats_name = ['Number of rows', 'Number of variables']
        stats_value = [self.rows_count, self.variables_count]

        dataset_dropna_count = self.data.dropna().count()
        missing = round((self.rows_count - dataset_dropna_count) / self.rows_count * 100, 1)
        stats_name.append('Missing cells(%)')
        stats_value.append(missing)

        memory_size = pd.DataFrame.memory_usage(self.data.collect()).sum()
        record_size = memory_size / self.rows_count
        stats_name.append('Total size in memory(KB)')
        stats_value.append(round(memory_size / 1024, 1))
        stats_name.append('Average row size in memory(B)')
        stats_value.append(round(record_size, 1))

        return stats_name, stats_value

    def get_scatter_matrix(self):
        warnings.simplefilter("ignore")

        fig_size = self.variables_count * 2
        fig, ax = plt.subplots(figsize=(fig_size, fig_size))
        scatter_matrix(self.scatter_matrix_data.collect(), ax=ax, alpha=0.8)

        def close():
            plt.close()
        fig.close = close
        scatter_matrix_html = PlotUtil.plot_to_str(fig)

        return scatter_matrix_html.replace('<svg', '<svg id="scatter_matrix"')

    def get_warnings_correlation(self):
        warnings_correlation = {}
        warnings_correlation_text = []
        if len(self.numeric) > 1:
            for i, col in enumerate(self.numeric):
                for j in range(i+1, len(self.numeric)):
                    dfc = stats.pearsonr_matrix(data=self.data.dropna(),
                                                cols=[self.numeric[i], self.numeric[j]]).collect()
                    dfc = dfc.iloc[1, 1]
                    if (i != j) and (abs(dfc) > 0.3):
                        warnings_correlation[self.numeric[i], self.numeric[j]] = dfc
                    else:
                        pass

        text = "There are {} pair(s) of variables that are show significant correlation:".format(len(warnings_correlation))
        warnings_correlation_text.append(text)
        for i in warnings_correlation:
            corr = warnings_correlation.get(i)
            if abs(corr) >= 0.5:
                text = "-  {} and {} are highly correlated, p = {:.2f}".format(i[0], i[1], warnings_correlation.get(i))
                warnings_correlation_text.append(text)
            elif 0.3 <= abs(corr) < 0.5:
                text = "-  {} and {} are moderately correlated, p = {:.2f}".format(i[0], i[1], warnings_correlation.get(i))
                warnings_correlation_text.append(text)
            else:
                pass

        return warnings_correlation_text

    def get_correlation(self):
        fig_size = self.variables_count
        fig, ax = plt.subplots(figsize=(fig_size, fig_size))
        eda = EDAVisualizer(ax)
        ax, corr = eda.correlation_plot(data=self.data, corr_cols=self.numeric, label=True)

        def close():
            plt.close()
        fig.close = close
        correlation_html = PlotUtil.plot_to_str(fig)

        return correlation_html.replace('<svg', '<svg id="correlation"')

    def get_variable_types(self):
        names = ['Numeric', 'Categorical', 'Date']
        values = [len(self.numeric), len(self.categorical), len(self.date)]

        return names, values

    def get_missing_values(self):
        # Missing Values %
        missing_threshold = 10
        for i in self.variables:
            query = 'SELECT SUM(CASE WHEN {0} is NULL THEN 1 ELSE 0 END) AS "nulls" FROM ({1})'
            pct_missing = self.conn_context.sql(query.format(quotename(i), self.data.select_statement))
            pct_missing = pct_missing.collect().values[0][0]
            pct_missing = pct_missing/self.rows_count
            if pct_missing > missing_threshold/100:
                self.warnings_missing[i] = pct_missing
        names = list(self.warnings_missing.keys())
        values = list(self.warnings_missing.values())

        return names, values

    def get_high_cardinality_variables(self):
        warnings_constant = {}
        card_threshold = 100
        for i in self.data.columns:
            query = 'SELECT COUNT(DISTINCT {0}) AS "unique" FROM ({1})'
            cardinality = self.conn_context.sql(query.format(quotename(i), self.data.select_statement))
            cardinality = cardinality.collect().values[0][0]
            if cardinality > card_threshold:
                self.warnings_cardinality[i] = (cardinality/self.rows_count)*100
            elif cardinality == 1:
                warnings_constant[i] = self.data.collect()[i].unique()

        names = list(self.warnings_cardinality.keys())
        values = list(self.warnings_cardinality.values())

        return names, values

    def get_highly_skewed_variables(self):
        skew_threshold = 0.5
        numeric = self.numeric
        categorical = self.categorical
        date = self.date

        warnings_skewness = {}
        cont, cat = stats.univariate_analysis(data=self.data, cols=numeric)
        for i in numeric:
            skewness = cont.collect()['STAT_VALUE']
            stat = 'STAT_NAME'
            val = 'skewness'
            var = 'VARIABLE_NAME'
            skewness = skewness.loc[(cont.collect()[stat] == val) & (cont.collect()[var] == i)]
            skewness = skewness.values[0]
            if abs(skewness) > skew_threshold:
                warnings_skewness[i] = skewness
            else:
                pass
        if self.key:
            if self.key in numeric:
                numeric.remove(self.key)
            elif self.key in categorical:
                categorical.remove(self.key)
            elif self.key in date:
                date.remove(self.key)
        for i in self.warnings_cardinality:
            if i in categorical:
                categorical.remove(i)
            else:
                pass
        rows = 4
        m = 0
        o = 0
        while o < len(numeric):
            if m <= 4:
                m += 1
            elif m > 4:
                rows += 2
                m = 0
                m += 1
            o += 1
        rows += 2
        rows += 1
        m = 0
        o = 0
        while o < len(categorical):
            if m <= 4:
                m += 1
            elif m > 4:
                rows += 2
                m = 0
                m += 1
            o += 1
        rows += 2
        rows += 1
        rows += 4

        names = list(warnings_skewness.keys())
        values = list(warnings_skewness.values())

        return names, values

    def get_categorical_variable_distribution_data(self, column):
        pie_data = self.data.agg([('count', column, 'COUNT')], group_by=column).sort(column).collect()
        x_data = list(pie_data[column])
        y_data = list(pie_data['COUNT'])

        return x_data, y_data

    def get_numeric_variable_distribution_data(self, column, bins=20):
        data_ = self.data.dropna(subset=[column])
        query = "SELECT MAX({}) FROM ({})".format(quotename(column), data_.select_statement)
        maxi = self.conn_context.sql(query).collect().values[0][0]
        query = "SELECT MIN({}) FROM ({})".format(quotename(column), data_.select_statement)
        mini = self.conn_context.sql(query).collect().values[0][0]
        diff = maxi-mini
        bin_size = round(diff/bins)
        if bin_size < 1:
            bin_size = 1
        query = "SELECT {0}, FLOOR({0}/{1}) AS BAND,".format(quotename(column), bin_size)
        query += " '[' || FLOOR({0}/{1})*{1} || ', ".format(quotename(column), bin_size)
        query += "' || ((FLOOR({0}/{1})*{1})+{1}) || ')'".format(quotename(column), bin_size)
        query += " AS BANDING FROM ({}) ORDER BY BAND ASC".format(data_.select_statement)
        bin_data = self.conn_context.sql(query)
        bin_data = bin_data.agg([('count', column, 'COUNT'),
                                 ('avg', 'BAND', 'ORDER')], group_by='BANDING')
        bin_data = bin_data.sort('ORDER').collect()
        x_data = list(bin_data['BANDING'])
        y_data = list(bin_data['COUNT'])
        return x_data, y_data

    @staticmethod
    def convert_pandas_to_html(df):
        return df.to_html()\
            .replace('\n', '').replace('  ', '')\
            .replace(' class="dataframe"', 'class="table table-bordered table-hover"')\
            .replace('border="1"', '')\
            .replace(' style="text-align: right;"', '')\
            .replace('<th></th>', '<th style="width: 10px">#</th>')\
            .replace('</thead><tbody>', '')\
            .replace('<thead>', '<tbody>')

    def generate_report_html(self):
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        threads = []
        thread_num = multiprocessing.cpu_count()
        count = 6
        if thread_num >= 2:
            count = 7
        pbar = tqdm(total=count, desc="Generating dataset report...", disable=False)

        variable_types = self.get_variable_types()

        high_cardinality_variables = self.get_high_cardinality_variables()
        pbar.update()

        highly_skewed_variables = self.get_highly_skewed_variables()
        pbar.update()

        if thread_num == 2:
            thread = GenerateSVGStrThread(
                'Generating scatter matrix and data correlation...',
                [self.get_scatter_matrix, self.get_correlation, self.get_warnings_correlation],
                pbar)
            threads.append(thread)
        elif thread_num >= 3:
            thread1 = GenerateSVGStrThread('Generating scatter matrix...', [self.get_scatter_matrix], pbar)
            thread2 = GenerateSVGStrThread('Generating data correlation...',
                                           [self.get_correlation, self.get_warnings_correlation], pbar)
            threads.append(thread1)
            threads.append(thread2)
        for thread in threads:
            thread.start()

        dataset_report_json = {}

        ul_html_template = '''
            <ul class="nav nav-pills flex-column">{}</ul>
        '''
        li_html_template = '''
            <li class="nav-item">
              <a class="nav-link">
                {}
                <span class="float-right">{}</span>
              </a>
            </li>        
        '''
        all_li_html = ''
        dataset_info = self.get_dataset_info()
        for i in range(0, len(dataset_info[0])):
            stats_name = dataset_info[0][i]
            stats_value = dataset_info[1][i]
            all_li_html = all_li_html + li_html_template.format(stats_name, stats_value)
        dataset_info_html = ul_html_template.format(all_li_html)

        dataset_report_json['overview_page'] = {
            'charts': []
        }
        element_id_suffix = 0
        element_id_suffix = element_id_suffix + 1
        dataset_report_json['overview_page']['charts'].append({
            'element_id': 'overview_page_chart_{}'.format(element_id_suffix),
            'x_data': variable_types[0],
            'y_data': variable_types[1],
            'type': 'doughnut',
            'title': '\n'
        })

        element_id_suffix = element_id_suffix + 1
        dataset_report_json['overview_page']['charts'].append({
            'element_id': 'overview_page_chart_{}'.format(element_id_suffix),
            'x_data': variable_types[0],
            'y_data': variable_types[1],
            'type': 'bar',
            'title': '\n'
        })

        element_id_suffix = element_id_suffix + 1
        dataset_report_json['overview_page']['charts'].append({
            'element_id': 'overview_page_chart_{}'.format(element_id_suffix),
            'x_data': high_cardinality_variables[0],
            'y_data': high_cardinality_variables[1],
            'type': 'horizontalBar',
            'title': ''
        })

        element_id_suffix = element_id_suffix + 1
        dataset_report_json['overview_page']['charts'].append({
            'element_id': 'overview_page_chart_{}'.format(element_id_suffix),
            'x_data': highly_skewed_variables[0],
            'y_data': highly_skewed_variables[1],
            'type': 'horizontalBar',
            'title': ''
        })

        variables_page_card_tools_menu_html = ''
        variables_page_card_tools_menu_html_template = \
            '<a class="dropdown-item" onclick="switchVariableContent(\'{}\')">{}</a>'
        variables_page_card_body_html = ''
        variables_page_card_body_html_template = '''
            <div class="row" id="{}">
             <div class="col-lg-{}" style="margin:0 auto">
              <div class="chart-responsive">
                <canvas id="{}"></canvas>
              </div>
             </div>
            </div>        
        '''
        variables_page_card_footer_html = ''
        variables_page_card_footer_html_template = '''
            <div id="{}">
              <ul class="nav nav-pills flex-column">{}</ul>
            </div>        
        '''
        dataset_report_json['variables_page'] = {
            'variables': self.variables,
            'child_page_ids': []
        }
        element_id_suffix = 0
        variable_stats_name_dict = {
            'count': 'Number of rows',
            'unique': 'Number of distinct values',
            'nulls': 'Number of nulls',
            'mean': 'Average',
            'std': 'Standard deviation',
            'median': 'Median',
            'min': 'Minimum value',
            'max': 'Maximum value',
            '25_percent_cont': '25% percentile when treated as continuous variable',
            '25_percent_disc': '25% percentile when treated as discrete variable',
            '50_percent_cont': '50% percentile when treated as continuous variable',
            '50_percent_disc': '50% percentile when treated as discrete variable',
            '75_percent_cont': '75% percentile when treated as continuous variable',
            '75_percent_disc': '75% percentile when treated as discrete variable'
        }
        for variable in self.variables:
            element_id_suffix = element_id_suffix + 1
            variable_type = self.variable_2_type_dict.get(variable)
            variable_distribution_data = None
            chart_type = 'bar'
            width_percent = 10
            if variable_type == VariableType.NUM:
                variable_distribution_data = self.get_numeric_variable_distribution_data(variable)
                bar_count = len(variable_distribution_data[0])
                if bar_count < 5:
                    width_percent = 4
                elif 5 <= bar_count < 10:
                    width_percent = 6
                elif 10 <= bar_count < 15:
                    width_percent = 8
            elif variable_type == VariableType.CAT:
                variable_distribution_data = self.get_categorical_variable_distribution_data(variable)
                chart_type = 'doughnut'
                width_percent = 6
            else:
                variable_distribution_data = [[], []]
                chart_type = 'doughnut'
                width_percent = 2

            element_id = 'variables_page_chart_{}'.format(element_id_suffix)
            dataset_report_json['variables_page'][variable] = {
                'element_id': element_id,
                'x_data': variable_distribution_data[0],
                'y_data': variable_distribution_data[1],
                'type': chart_type,
                'title': 'Distribution of {}'.format(variable)
            }
            child_page_id = 'variables_page_{}'.format(element_id_suffix)
            dataset_report_json['variables_page']['child_page_ids'].append(child_page_id)

            variables_page_card_tools_menu_html = \
                variables_page_card_tools_menu_html + \
                variables_page_card_tools_menu_html_template.format(child_page_id, variable)

            variables_page_card_body_html = \
                variables_page_card_body_html + \
                variables_page_card_body_html_template.format(child_page_id, width_percent, element_id)

            variable_stats = self.col_stats_dict[variable]
            all_li_html = ''
            for i in range(0, len(self.col_stats_names)):
                stats_value = variable_stats[i]
                stats_name = self.col_stats_names[i]
                all_li_html = all_li_html + li_html_template.format(variable_stats_name_dict[stats_name], stats_value)
            variables_page_card_footer_html = \
                variables_page_card_footer_html+\
                variables_page_card_footer_html_template.format('{}_footer'.format(child_page_id), all_li_html)
        pbar.update()

        sample_html = ''
        if self.rows_count >= 10:
            sample_html = DataAnalyzer.convert_pandas_to_html(self.data.head(10).collect())
        else:
            sample_html = DataAnalyzer.convert_pandas_to_html(self.data.collect())
        pbar.update()

        for thread in threads:
            thread.join()

        scatter_matrix_html = None
        correlation_html = None
        warnings_correlation = None
        if thread_num == 1:
            scatter_matrix_html = self.get_scatter_matrix()
            correlation_html = self.get_correlation()
            warnings_correlation = self.get_warnings_correlation()
        elif thread_num == 2:
            scatter_matrix_html = threads[0].get_results()[0]
            correlation_html = threads[0].get_results()[1]
            warnings_correlation = threads[0].get_results()[2]
        elif thread_num >= 3:
            scatter_matrix_html = threads[0].get_results()[0]
            correlation_html = threads[1].get_results()[0]
            warnings_correlation = threads[1].get_results()[1]

        all_li_html = ''
        li_html_template = '''
            <li class="nav-item">
              <a class="nav-link">
                {}
              </a>
            </li>
        '''
        correlation_page_card_footer_html_template = '''
            <div>
              <ul class="nav nav-pills flex-column">{}</ul>
            </div>
        '''
        for text in warnings_correlation:
            all_li_html = all_li_html + li_html_template.format(text)
        correlation_page_card_footer_html = correlation_page_card_footer_html_template.format(all_li_html)

        template = TemplateUtil.get_template('dataset_report.html')
        self.__report_html = template.render(
            dataset_name=self.data.name,
            start_time=start_time,
            dataset_info=dataset_info_html,
            sample=sample_html,
            scatter_matrix=scatter_matrix_html,
            correlation_page_card_body=correlation_html,
            correlation_page_card_footer=correlation_page_card_footer_html,
            variables_page_card_tools=variables_page_card_tools_menu_html,
            variables_page_card_body=variables_page_card_body_html,
            variables_page_card_footer=variables_page_card_footer_html,
            dataset_report_json=dataset_report_json)
        self.__report_html = minify(self.__report_html, remove_all_empty_space=True, remove_comments=True)
        pbar.update()

        self.__iframe_report_html = TemplateUtil.get_notebook_iframe(self.__report_html)

    def get_report_html(self):
        return self.__report_html

    def get_iframe_report_html(self):
        return self.__iframe_report_html
