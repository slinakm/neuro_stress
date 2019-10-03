from flask import Flask, request
import data_utils
import model_nn
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "This is a default landing page!"

@app.route('/api/score/', methods=['POST'])
def regression():
    req_struct = data_utils.parse_request(request.data)
    prediction = model_nn.predict(req_struct)
    return prediction

if __name__ == '__main__':
    app.run(debug=True)