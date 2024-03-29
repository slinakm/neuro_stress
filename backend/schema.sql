DROP TABLE IF EXISTS userdata;
DROP TABLE IF EXISTS scores;

CREATE TABLE userdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_recorded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    loc_x FLOAT,
    loc_y FLOAT,
    speed FLOAT,
    phone_on INTEGER,
    feeling INTEGER
);

CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_calculated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    score FLOAT
);