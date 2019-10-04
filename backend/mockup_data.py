import argparse
import random 
import data_utils
import database
import time
import math
import sqlite3
import numpy as np

"""
    Since it's infeasible during testing to collect large swaths of test data, this
    autopopulates the database with mock data for testing the functionality of the
    neural model.
"""

if __name__=='__main__':
    psr = argparse.ArgumentParser()
    psr.add_argument("-n", type=int, default=1000)
    psr.add_argument("--reinitialize", action='store_true')
    args = psr.parse_args()
    if args.reinitialize:
        try:
            connection = sqlite3.connect("data/database.db")
            cursor = connection.cursor()
            cursor.execute("DROP TABLE userdata")
            connection.close()
        except Exception as e:
            print(e)
        _ = database.init_db()
    rand_time_since = 0.0
    init_spd = 0.0
    dspd = 0.0
    last_spd = 0.0
    last_lat = 0.0
    last_lng = 0.0
    for _ in range(args.n):
        # generate (auto-id, time + increment, lat, lng, spd, feeling)
        rand_time_since += 500 * random.random()
        dspd = random.gauss(0, 0.1)
        newspd = last_spd + dspd
        lat_spd = newspd * random.random()
        lng_spd = math.sqrt(newspd ** 2 - lat_spd ** 2) * -1 if random.choice([True, False]) else 1
        new_lat = last_lat + lat_spd
        new_lng = last_lng + lng_spd
        record_dict = {"time": int(time.time() + rand_time_since), "lat": new_lat, "lng": new_lng,"spd": newspd, "feeling": random.randint(0, 15), "phone_on": np.random.binomial(1, 0.35)}
        last_spd = newspd
        last_lat = new_lat
        last_lng = new_lng
        data_utils.push_to_db(record_dict)