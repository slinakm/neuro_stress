import sqlite3

def parse_request(request):
    return request

def push_to_db(struct):
    try:
        connection = sqlite3.connect("data/database.db")
        connection.row_factory = sqlite3.Row
        insert_query = """INSERT INTO userdata (id, time_recorded, loc_x, loc_y, speed, feeling)
        VALUES (NULL, ?, ?, ?, ?, ?) """
        record_tuple = (struct["time"], struct["lng"], struct["lat"], struct["spd"], 0)
        cur = connection.cursor()
        cur.execute(insert_query, record_tuple)
        connection.commit()
        cur.close()
        connection.close()
    except Exception as e:
        print("Failed to insert into table: {}".format(e))

            