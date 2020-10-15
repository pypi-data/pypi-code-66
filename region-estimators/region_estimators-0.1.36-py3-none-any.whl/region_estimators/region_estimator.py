from abc import ABCMeta, abstractmethod
import geopandas as gpd
import pandas as pd
import json

class RegionEstimator(object):
    """
        Abstract class, parent of region estimators (each implementing a different estimation method).
        Requires GeoPandas and Pandas
    """
    __metaclass__ = ABCMeta

    def __init__(self, sensors, regions, actuals):
        """ Initialise instance of the RegionEstimator class.

            Args:
                sensors: list of sensors as pandas.DataFrame
                    Required columns:
                        'sensor_id' (Unique INDEX)
                        'latitude' (float): latitude of sensor location
                        'longitude' (float): longitude of sensor location
                        'name' (string (Optional): Name of sensor

                regions: list of regions as pandas.DataFrame
                    Required columns:
                        'region_id' (Unique INDEX)
                        'geometry' (shapely.wkt/geom.wkt)

                actuals: list of sensor values as pandas.DataFrame
                    Required columns:
                        'timestamp' (string): timestamp of actual reading
                        'sensor_id': ID of sensor which took actual reading - must match an index value in sensors
                        [one or more value columns] (float):    value of actual measurement readings.
                                                                each column name is the name of the measurement e.g. 'NO2'

            Returns:
                Initialised instance of subclass of RegionEstimator

        """
        ### Check sensors:

        # (Not checking sensor_id as that forms the index)
        assert 'latitude' in list(sensors.columns), "There is no latitude column in sensors dataframe"
        assert pd.to_numeric(sensors['latitude'], errors='coerce').notnull().all(), \
            "latitude column contains non-numeric values."
        assert 'longitude' in list(sensors.columns), "There is no longitude column in sensors dataframe"
        assert pd.to_numeric(sensors['longitude'], errors='coerce').notnull().all(), \
            "longitude column contains non-numeric values."

        ### Check regions
        # (Not checking region_id as that forms the index)
        assert 'geometry' in list(regions.columns), "There is no geometry column in regions dataframe"

        ### Check actuals
        assert 'timestamp' in list(actuals.columns), "There is no timestamp column in actuals dataframe"
        assert 'sensor_id' in list(actuals.columns), "There is no sensor_id column in actuals dataframe"
        assert len(list(actuals.columns)) > 2, "There are no measurement value columns in the actuals dataframe."

        # Check measurement columns have either numeric or null data
        for column in list(actuals.columns):
            if column not in ['timestamp', 'sensor_id']:
                # Check measurement does not contain numeric (nulls are OK)
                df_temp = actuals.loc[actuals[column].notnull()]
                assert pd.to_numeric(df_temp[column], errors='coerce').notnull().all(), \
                    "actuals['" + column + "'] column contains non-numeric values (null values are accepted)."



        # Check that each sensor_id value is present in the sensors dataframe index.
        # ... So sensor_id values must be a subset of allowed sensors
        error_sensors = set(actuals['sensor_id'].unique()) - set(sensors.index.values)
        assert len(error_sensors) == 0, \
            "Each sensor ID must match a sensor_id in sensors. Error sensor IDs: " + str(error_sensors)


        ### Convert to geo dataframe
        try:
            gdf_sensors = gpd.GeoDataFrame(data=sensors,
                                           geometry=gpd.points_from_xy(sensors.longitude, sensors.latitude))
        except Exception as err:
            raise ValueError('Error converting sensors DataFrame to a GeoDataFrame: ' + str(err))

        gdf_sensors = gdf_sensors.drop(columns=['longitude', 'latitude'])

        try:
            gdf_regions = gpd.GeoDataFrame(data=regions, geometry='geometry')
        except Exception as err:
            raise ValueError('Error converting regions DataFrame to a GeoDataFrame: ' + str(err))



        #   Make sure value columns at the end of column list
        cols = actuals.columns.tolist()
        cols.insert(0, cols.pop(cols.index('sensor_id')))
        cols.insert(0, cols.pop(cols.index('timestamp')))

        # Make all non integer values Null in measurement fields
        # No longer required, as covered in 'check actuals' assertations above
        #actuals[cols[2:]] = actuals[cols[2:]].apply(pd.to_numeric, errors='coerce')

        self.sensors = gdf_sensors
        self.regions = gdf_regions
        self.actuals = actuals

        self.__get_all_region_neighbours()
        self.__get_all_region_sensors()


    @abstractmethod
    def get_estimate(self, measurement, timestamp, region_id):
        raise NotImplementedError("Must override get_estimate")


    def get_estimations(self, measurement, region_id=None, timestamp=None, print_progress=False):
        """  Find estimations for a region (or all regions if region_id==None) and
                timestamp (or all timestamps (or all timestamps if timestamp==None)

            :param measurement: measurement to be estimated (string - required)
            :param region_id: region identifier (string or None)
            :param timestamp:  timestamp identifier (string or None)

            :return: pandas dataframe with columns:
                'measurement'
                'region_id'
                'timestamp'
                'value' (calculated 'estimate)
                'extra_data' (json string)
        """

        # Check inputs
        assert measurement is not None, "measurement parameter cannot be None"
        assert measurement in list(self.actuals.columns), "The measurement: '" + measurement \
                                                          + "' does not exist in the actuals dataframe"

        if region_id is not None:
            df_reset = pd.DataFrame(self.regions.reset_index())
            regions_temp = df_reset.loc[df_reset['region_id'] == region_id]
            assert len(regions_temp.index) > 0, "The region_id does not exist in the regions dataframe"
        if timestamp is not None:
            df_actuals_reset = pd.DataFrame(self.actuals.reset_index())
            actuals_temp = df_actuals_reset.loc[df_actuals_reset['timestamp'] == timestamp]
            assert len(actuals_temp.index) > 0, "The timestamp does not exist in the actuals dataframe"

        df_result = pd.DataFrame(columns=['measurement','region_id','timestamp','value','extra_data'])

        # Calculate estimates
        if region_id:
            if print_progress == True:
                print('Calculating for region:', region_id)
            results = [self.get_region_estimation(measurement, region_id, timestamp, print_progress)]
        else:
            results = []
            for index, _ in self.regions.iterrows():
                if print_progress == True:
                    print('Calculating for region:', index)
                results.append(self.get_region_estimation(measurement, index, timestamp, print_progress))

        for item in results:
            for estimate in item['estimates']:
                df_result = df_result.append({  'measurement': measurement,
                                                'region_id': item['region_id'],
                                                'timestamp': estimate['timestamp'],
                                                'value': estimate['value'],
                                                 'extra_data': json.dumps(estimate['extra_data'])
                                                }
                                             , ignore_index=True)

        return df_result


    def get_region_estimation(self, measurement, region_id, timestamp=None, print_progress=False):
        """  Find estimations for a region and timestamp (or all timestamps (or all timestamps if timestamp==None)

            :param measurement: measurement to be estimated (string, required)
            :param region_id: region identifier (string, required)
            :param timestamp:  timestamp identifier (string or None)

            :return: a dict with items 'region_id' and 'estimates (list). Estimates contains
                        'timestamp', (estimated) 'value' and 'extra_data'
        """
        region_result = {'region_id': region_id, 'estimates':[]}

        if timestamp is not None:
            if print_progress == True:
                print(region_id, '    Calculating for timestamp:', timestamp)

            region_result_estimate = self.get_estimate(measurement, timestamp, region_id)

            if print_progress == True:
                print(region_id, '    Calculated for timestamp:', region_result_estimate)

            region_result['estimates'].append({'value':region_result_estimate[0],
                                               'extra_data': region_result_estimate[1],
                                               'timestamp':timestamp})
        else:
            timestamps = sorted(self.actuals['timestamp'].unique())
            for _, timestamp in enumerate(timestamps):
                if print_progress == True:
                    print(region_id, '    Calculating for timestamp:', timestamp)

                region_result_estimate = self.get_estimate(measurement, timestamp, region_id)

                if print_progress == True:
                    print(region_id, '    Calculated for ', timestamp, ':', region_result_estimate)

                region_result['estimates'].append(  {'value':region_result_estimate[0],
                                                     'extra_data': region_result_estimate[1],
                                                     'timestamp': timestamp}
                                                    )
        return region_result


    def get_adjacent_regions(self, region_ids, ignore_regions):
        """  Find all adjacent regions for list a of region ids

            :param region_ids: list of region identifier (list of strings)
            :param ignore_regions:  list of region identifier (list of strings): list to be ignored

            :return: a list of regions_ids
        """

        # Create an empty list for adjacent regions
        adjacent_regions =  []
        # Get all adjacent regions for each region
        df_reset = self.regions.reset_index()
        for region_id in region_ids:
            regions_temp = df_reset.loc[df_reset['region_id'] == region_id]
            if len(regions_temp.index) > 0:
                adjacent_regions.extend(regions_temp['neighbours'].iloc[0].split(','))

        # Return all adjacent regions as a querySet and remove any that are in the completed/ignore list.
        return [x for x in adjacent_regions if x not in ignore_regions]


    def sensors_exist(self, measurement, timestamp):
        return len(self.actuals.loc[(self.actuals['timestamp'] == timestamp) & (self.actuals[measurement].notna())]) > 0


    def __get_all_region_neighbours(self):
        '''
        Find all of the neighbours of each region and add to a 'neighbours' column in self.regions -
        as comma-delimited string of region_ids

        :return: No return value
        '''
        for index, region in self.regions.iterrows():
            neighbors = self.regions[self.regions.geometry.touches(region.geometry)].index.tolist()
            neighbors = filter(lambda item: item != index, neighbors)
            self.regions.at[index, "neighbours"] = ",".join(neighbors)


    def __get_all_region_sensors(self):
        '''
            Find all of the sensors within each region and add to a 'sensors' column in self.regions -
            as comma-delimited string of sensor ids.

            :return: No return value
        '''
        for index, region in self.regions.iterrows():
            sensors = self.sensors[self.sensors.geometry.within(region['geometry'])].index.tolist()
            self.regions.at[index, "sensors"] = ",".join(str(x) for x in sensors)
