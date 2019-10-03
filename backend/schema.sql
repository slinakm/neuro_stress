DROP TABLE IF EXISTS userdata;

CREATE TABLE userdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_recorded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    loc_x FLOAT,
    loc_y FLOAT
)