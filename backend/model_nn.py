import numpy as np
from sklearn.cluster import KMeans
import data_utils
import math
import argparse

def predict():
    X, lbl, ctr = compute_optimal_location_clusters(return_labels=True)
    entropy = _compute_location_entropy(lbl, ctr)
    variance = _compute_location_variance()
    circadian = get_circadian_mvmt()
    use_freq = _get_phone_use_freq()
    use_duration = _get_phone_use_duration()[0]
    a = _compute_activation(np.array([entropy, variance, circadian, use_duration, use_freq]))
    return a

# normalized location entropy, location variance, homestay, circadian mvmt, usage duration, usage freq
bias = np.array([10, 13, 14, 3, 3])
weights = np.array([-12, -13 / 20, -0.7, 12 / 16000, 9 / 40])
# homestay = -10, skipped here, bias = 2
# baseline-weights -- will be trained online

def _get_phone_use_duration():
    T = data_utils.get_column("time_recorded")
    P = data_utils.get_column("phone_on")
    time_used = 0.0
    last_time = T[0]
    phone_used_last_time = P[0]
    for time, p in zip(T, P):
        if p == 1 and phone_used_last_time: 
            time_used += (time - last_time)
        last_time = time
        phone_used_last_time = p
    return time_used / ((T[-1] - T[0]) / (60 * 60 * 24))


def _get_phone_use_freq(threshold=3):
    P = data_utils.get_column("phone_on").flatten()
    freq = 0
    last_status = 0
    for i, status in enumerate(P):
        if status == 1 and all(P[max(0, i-threshold+1):i] == 1): freq += 1
        last_status = status
    return freq

circadian_perfection = 60 * 60 * 24
def get_circadian_mvmt():
    X = data_utils.get_column("loc_x")
    Y = data_utils.get_column("loc_y")

    fft_x = np.fft.rfft(X)
    fft_y = np.fft.rfft(Y)
    ps_x = np.sum(np.abs(fft_x)**2)
    ps_y = np.sum(np.abs(fft_y) ** 2)
    return math.log(ps_x + ps_y) - math.log(24)


def get_home_stay_cluster(sleep_hour_min=23, sleep_hour_max=7):
    # T = data_utils.get_column("time").apply_along_axis()
    pass


def compute_optimal_location_clusters(max_clusters = 10, return_labels=False):
    X = data_utils.get_column("loc_x, loc_y")
    best_inertia = float('inf')
    best_centers = []
    if return_labels: best_labels = []
    for i in range(1, max_clusters):
        km = KMeans(n_clusters=i, random_state=42)
        km.fit(X)
        if km.inertia_ < best_inertia: 
            best_inertia = km.inertia_
            best_centers = km.cluster_centers_
            if return_labels: best_labels = km.labels_
    if return_labels:
        return X, best_labels, best_centers
    else:
        return best_centers

    

# loc.shape = (timeslices, 2 [lat and lng])
def _compute_location_entropy(labels, clusters, normalize=True):
    # sum_i (p_i * log(p_i))
    l = []
    for i in range(len(clusters)):
        p_i = sum(labels == i) / len(labels) 
        p_i *= np.log(p_i)
        if normalize:
            p_i /= np.log(len(clusters))
        l.append(p_i)
    return -sum(l)
    
def _compute_location_variance():
    x = data_utils.get_column("loc_x")
    y = data_utils.get_column("loc_y")
    return math.log(np.std(x) ** 2 + np.std(y) ** 2)


def _compute_activation(features):
    return np.sum(np.multiply(features, weights) + bias)

import matplotlib.pyplot as plt
if __name__ == '__main__':
    psr = argparse.ArgumentParser()
    psr.add_argument('--quiet', '-q', action='store_true')
    args = psr.parse_args()

    X, lbl, ctr = compute_optimal_location_clusters(return_labels=True)
    entropy = _compute_location_entropy(lbl, ctr)
    variance = _compute_location_variance()
    circadian = get_circadian_mvmt()
    use_freq = _get_phone_use_freq()
    use_duration = _get_phone_use_duration()[0]

    if not args.quiet:     
        print("Testing function compute_optimal_location_clusters...")
        plt.scatter(X[:, 0], X[:, 1], c=lbl, s=50, cmap='viridis')
        plt.show()
        print("Success!")
        print()
        print("Testing location entropy calculation...")
        print("Entropy:",entropy)
        print("Success!")
        print()
        print("Testing location variance calculation...")
        print("Variance:",variance)
        print("Success!")
        print()
        print("Testing Discrete FFT Circadian Rhythm Extraction...")
        print(circadian)
        print()
        print("# of times phone used:")
        print(use_freq)
        print()
        print("Length of time phone used (s/d):")
        print(use_duration)

    a = _compute_activation(np.array([entropy, variance, circadian, use_duration, use_freq]))
    print("PHQ Score:", max(0, a))