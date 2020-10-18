# installed libraries
from names import get_full_name, get_first_name, get_last_name
from brule import full_name, first_name, last_name
from numpy.random import normal, rand

# part of the Standard Library
from datetime import datetime, timedelta, time, date
from random import choice, randint
from uuid import uuid4


#------------------------#
#                        #
#   Abstracted Classes   #
#                        #
#------------------------#

class _Numeric():
    """
    Abstract class extended by UniformDist and NormalDist
    """
    
    def __init__(self, precision=0):
        self.precision = precision


#-------------------#
#                   #
#   Numeric Types   #
#                   #
#-------------------#

class UniformDist(_Numeric):
    """
    A field type to be used in the "fields" configuration

    This field creates a series of numbers with a uniform distribution
    """

    # TODO there's an issue where a uniform
    # distribution isn't always created, but rather
    # the first group is low and the last is high

    def __init__(self, low, high, precision=None):
        """
        Create instance of UniformDist field type

        Required params:
            low: Inclusive lower bound of the uniform distribution
            high: Inclusive upper bound of the uniform distribution
            
        Optional params:
            precision: Number of decimal places. Defaults to None, which
                       results in an integer
        """
        
        super().__init__(precision)
        self.low = low
        self.high = high

    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        return [
            round((rand() * (self.high - self.low) + self.low), self.precision)
            for _ in range(n)
        ]


class NormalDist(_Numeric):
    """
    A field type to be used in the "fields" configuration

    This field creates a series of numbers with a normal distribution
    """

    def __init__(self, mean, sd, bounds=None, precision=None):
        """
        Create instance of NormalDist field type

        Required params:
            mean: Mean of the normal distribution
            sd: Standard Deviation of the normal distribution
            
        Optional params:
            bounds: Tuple containing the lower and upper bounds of the distribution.
                    Defaults to None
            precision: Number of decimal places. Defaults to None, which
                       results in an integer
        """

        super().__init__(precision)
        self.mean = mean
        self.sd = sd
        self.bounds = bounds

    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        if self.bounds:
            low, high = self.bounds
            out_of_bound = low-1

            series = []

            for i in range(n):
                num = out_of_bound
                while num < low or num > high:
                    num = normal(self.mean, self.sd)
                series.append(round(num, self.precision))

            return series

        else:
            return [round(normal(self.mean, self.sd), self.precision) for _ in range(n)]


#----------------#
#                #
#   Text Types   #
#                #
#----------------#

class Name():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of names
    """
    
    def __init__(self, first_only=False, last_only=False, brule=False, depends_on=None):
        """
        Create instance of Name field type

        Optional params:
            first_only: Boolean indicating whether or not to return just a first name.
                        Defaults to False
            last_only: Boolean indicating whether or not to return just a last name.
                       Defaults to False
            brule: Boolean indicated whether or not to return a "Brule-ized" name.
                   Defaults to False
            depends_on: Column name of a gender field (if applicable), so that random
                        names match up with random genders
        """
        
        self.first_only = first_only
        self.last_only = last_only
        self.brule = brule
        self.depends_on = depends_on


    def _to_series(self, n, dep_series=None):
        """
        Return a list of length `n` in accordance with this field type
        """

        # choose which functions to use
        if self.brule:        
            F = {'full': full_name, 'first': first_name, 'last': last_name}
        else:
            F = {'full': get_full_name, 'first': get_first_name, 'last': get_last_name}

        if self.depends_on:
            dep_series = dep_series.apply(lambda x: 'male' if x.lower()[0] == 'm' else 'female')

            if self.first_only:
                return [F['first'](gender=dep_series[i]) for i in range(n)]
            if self.last_only:
                return [F['last']() for _ in range(n)]
            
            # else
            return [F['full'](gender=dep_series[i]) for i in range(n)]     

        else:
            if self.first_only:
                return [F['first']() for _ in range(n)]
            if self.last_only:
                return [F['last']() for _ in range(n)]
            
            # else
            return [F['full']() for _ in range(n)]  


class Group():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of different groups / classes
    """

    def __init__(self, groups):
        """
        Create instance of Name field type

        Required params:
            groups: List of groups (with the option of providing discrete probabilites)
        """

        self.groups = groups

    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """
        
        # check if custom probabilites were provided
        if isinstance(self.groups[0], (list, tuple)):
            
            if sum([x[1] for x in self.groups]) != 1:
                raise ValueError("Probabilites don't add to 1")

            series = []
            for _ in range(n):
                r = rand()
                for label, prob in self.groups:
                    r -= prob
                    if r <= 0:
                        series.append(label)
                        break
            return series

        # if no probabilities were given, use a uniform dist
        else:
            return [choice(self.groups) for _ in range(n)]


class Custom():
    """
    A field type to be used in the "fields" configuration

    This field creates a series based on a custom function
    """

    def __init__(self, base, func):
        """
        Create instance of Custom field type

        Required params:
            base: Name of column which this function is applied to
            func: Function to be applied
        """

        if not hasattr(func, '__call__'):
            raise TypeError('`func` must be a function')
        
        self.base = base
        self.func = func

    def _to_series(self, base_series):
        """
        Return a list of length `n` in accordance with this field type
        """

        return base_series.apply(self.func)


class Constant():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a constant value
    """

    def __init__(self, value):
        """
        Create instance of Constant field type

        Required params:
            value: Constant value to be returned
        """

        self.value = value

    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        return [self.value for _ in range(n)]


#--------------------#
#                    #
#   DateTime Types   #
#                    #
#--------------------#

class Date():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a dates 
    """
    
    def __init__(self, start, end):
        """
        Create instance of Date field type

        Required params:
            start: Start of date range
            end: End of date range
        """

        # clean args
        if not isinstance(start, (date, datetime)):
            try:
                start = self._parse_date(start)
            except:
                raise ValueError("Unable to parse start date, see `help(Date)` for info")

        if not isinstance(end, (date, datetime)):
            try:
                end = self._parse_date(end)
            except:
                raise ValueError("Unable to parse end date, see `help(Date)` for info")

        if start >= end:
            raise ValueError("`start` time must be before `end` time")

        self.start = start
        self.end = end


    def _parse_date(self, date_string):
        """
        Parse date string into datetime.date
        """

        parts = re_split(r'(-|/|\.|\s)', date_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        if len(parts) == 3:
            return date(*list(map(int, parts)))
        
        else:
            raise ValueError(f"Unable to parse date: {date_string}")

    
    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        diff = self.end - self.start
        return [self.start + timedelta(days=randint(0, diff.days)) for _ in range(n)]


class DateTime():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a datetimes
    """

    def __init__(self, start, end, unix=False):
        """
        Create instance of DateTime field type

        Required params:
            start: Start of datetime range
            end: End of datetime range

        Optional params:
            unix: Boolean of whether or not to return as UNIX timestamp.
                  Defaults to False
        """
        
        if not isinstance(start, datetime):
            try:
                start = self._parse_date(start)
            except:
                raise TypeError("Unable to parse start date, see `help(DateTime)` for info")

        if not isinstance(end, datetime):
            try:
                end = self._parse_date(end)
            except:
                raise TypeError("Unable to parse end date, see `help(DateTime)` for info")

        if start >= end:
            raise ValueError("`start` time must be before `end` time")

        self.start = start
        self.end = end
        self.unix = unix


    def _parse_date(self, date_string):
        """
        Parse datetime string into datetime.datetime
        """

        parts = re_split(r'(-|/|:|\.|\s)', date_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        # [year, mon, day, hour, min, sec]
        # [year, mon, day, hour, min]
        if len(parts) >= 5:
            return datetime(*list(map(int, parts)))
        
        else:
            raise TypeError(f"Unable to parse date: {date_string}")


    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        diff = self.end - self.start
        if self.unix:
            return [int((self.start + timedelta(seconds=randint(0, diff.total_seconds()))).timestamp()) for _ in range(n)]
        else:
            return [self.start + timedelta(seconds=randint(0, diff.total_seconds())) for _ in range(n)]


class Time():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a times
    """

    def __init__(self, start, end):
        """
        Create instance of Time field type

        Required params:
            start: Start of time range
            end: End of time range
        """
        
        if not isinstance(start, time):
            try:
                start = self._parse_time(start)
            except:
                raise TypeError("Unable to parse start time, see `help(Time)` for info")

        if not isinstance(end, time):
            try:
                end = self._parse_time(end)
            except:
                raise TypeError("Unable to parse end time, see `help(Time)` for info")

        if start >= end:
            raise ValueError("`start` time must be before `end` time")

        self.start = start
        self.end = end        


    def _parse_time(self, time_string):
        """
        Parse time string into datetime.time
        """

        parts = re_split(r'(-|/|:|\.|\s)', time_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        if len(parts) >= 2:
            return time(*list(map(int, parts)))
        
        else:
            raise TypeError(f"Unable to parse time: {time_string}")


    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        form = '%H:%M:%S'
        d1 = datetime.strptime(self.start.strftime(form), form)
        d2 = datetime.strptime(self.end.strftime(form), form)
        diff = d2 - d1
        return [
            (d1 + timedelta(seconds=randint(0, diff.total_seconds()))).strftime(form)
            for _ in range(n)
        ]


#--------------#
#              #
#   ID Types   #
#              #
#--------------#

class ID():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a IDs
    """

    def __init__(self, start=1):
        """
        Create instance of ID field type

        Optional params:
            start: Starting value for the ID, incremented by 1 after that point.
                   Defaults to 1
        """

        try:
            self.start = int(start)
        except:
            raise TypeError('`start` needs to be of type `int`')
        
    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        return [x for x in range(self.start, n+self.start)]


class GUID():
    """
    A field type to be used in the "fields" configuration

    This field creates a series of a GUIDs
    """

    def __init__(self, format="str"):
        """
        Create instance of GUID field type

        Optional params:
            format: Format type for the GUID. Can be "str", "int", or "hex"
                    Defaults to str
        """

        self.format = format

    def _to_series(self, n):
        """
        Return a list of length `n` in accordance with this field type
        """

        if self.format == "hex":
            return [uuid4().hex for _ in range(n)]
        elif self.format == "int":
            return [uuid4().int for _ in range(n)]
        else:
            return [uuid4() for _ in range(n)]