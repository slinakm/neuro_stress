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
    def __init__(self):
        pass

    def cluster_gps_locations(self, max_clusters=10, max_distance=500):
        pass

    def get_location_variance(lat, lng):
        return np.log(np.power(np.std(lat), 2) + np.power(np.std(lng), 2))

    def calc_home_stay_time():
        pass

    def calc_circadian_rhythm_variance():
        pass

    def calc_phone_usage_frequency():
        pass

    def calc_normalized_location_entropy():
        pass

    def calc_phone_usage_duration_by_day():
        pass

    def partition_data_by_day():
        pass

class PHQRegressor():
    def __init__(self):
        pass

     
