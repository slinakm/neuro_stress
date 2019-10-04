import sqlite3
import numpy as np

def parse_request(request):
    return request

def get_column(column_name):
    connection = sqlite3.connect("data/database.db")
    connection.row_factory = sqlite3.Row
    column_query = "SELECT " + column_name + " FROM userdata"
    cur = connection.cursor()
    arr = cur.execute(column_query).fetchall()
    cur.close()
    connection.close()
    return np.array(arr)

def push_to_db(struct):
    try:
        connection = sqlite3.connect("data/database.db")
        connection.row_factory = sqlite3.Row
        insert_query = """INSERT INTO userdata (id, time_recorded, loc_x, loc_y, speed, feeling, phone_on)
        VALUES (NULL, ?, ?, ?, ?, ?, ?) """
        record_tuple = (struct["time"], struct["lng"], struct["lat"], struct["spd"], struct["feeling"], struct["phone_on"])
        cur = connection.cursor()
        cur.execute(insert_query, record_tuple)
        connection.commit()
        cur.close()
        connection.close()
    except Exception as e:
        print("Failed to insert into table: {}".format(e))

            