import numpy as np

def predict(data):
    return data

# normalized location entroyp, location variance, homestay, circadian mvmt, usage duration, usage freq
bias = np.array([10, 14, 2, 14, 3, 3])
weights = np.array([-10, -14, -10, -0.6, 11 / 16000, 9 / 35])
# baseline-weights -- will be trained online

# loc.shape = (timeslices, 2 [lat and lng])
def _compute_location_entropy(loc):
    # sum_i (p_i * log(p_i))
    pass

def _compute_activation(features):
    return np.sum(np.multiply(features, weights) + bias)

