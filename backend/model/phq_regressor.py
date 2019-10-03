import numpy as np

"""
    Features:
        normalized location entropy
        location variance
        home stay
        circadian rhythm
        phone usage duration
        phone usage frequency
"""

class DataProcessor():
    def __init__(self, data):
        self.data = data

    def cluster_gps_locations(self, data, max_clusters=10, max_distance=500):
        for i in range(max_clusters):
            break
        """
            return [points in each clusters, mean of each cluster]
        """

    def get_location_variance(self, lat, lng):
        return np.log(np.power(np.std(lat), 2) + np.power(np.std(lng), 2))

    def calc_home_stay_time(self):
        """
            Infer which cluster represents their home by 1) length of stay and 2) time visited
        """

    def calc_circadian_rhythm_variance(self):
        pass

    def calc_phone_usage_frequency(self):
        pass

    def calc_normalized_location_entropy(self):
        return -np.sum(

    def calc_phone_usage_duration_by_day(self):
        pass

    def partition_data_by_day():
        pass

class PHQRegressor():
    def __init__(self):
        pass

    def weights(self):
        return []

     
