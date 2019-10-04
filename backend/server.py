from flask import Flask, request, render_template
import data_utils
import model_nn
import sqlite3
import argparse
import database as db

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "This is a default landing page!"

@app.route("/db/", methods=["GET"])
def view_data():
    connection = sqlite3.connect("data/database.db")
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute("select * from userdata")
    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

@app.route('/api/score/', methods=['POST'])
def regression():
    req_struct = request.get_json()
    data_utils.push_to_db(req_struct)
    prediction = model_nn.predict(db.get_db())
    return str(req_struct["lat"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--initialize', action='store_true') # flag for updating schema
    args = parser.parse_args()
    if args.initialize: 
        db.init_db()
    app.run(debug=True)