from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)


with app.app_context():
    app.config['MONGO_DBNAME'] = 'CryptoDB'
    # app.config['MONGO_URI'] = 'mongodb://localhost:27017'
    # app.config['MONGO_PORT'] = 27017
    mongo = PyMongo(app)

@app.route('/')
def cryproShow():
    return render_template("index.html")

@app.route('/load_ajax', methods=["GET"])
def load_ajax():
    if request.method == "GET":

            m = mongo.db.coments  # Here Mail is your Table Name
            k = m.find()
            result = []
            for i in k:
                result.append(i['theme'])

    return jsonify(result)


@app.route('/load_autors', methods=["GET"])
def load_autors():
    if request.method == "GET":
        topic = request.args['val']
        m = mongo.db.coments  # Here Mail is your Table Name
        k = m.find()
        result = []
        for i in k:
            if i['theme'] == topic:
                result = i
                break
    result = [i['author'] for i in result['posts']]
    result = {i: result.count(i) for i in result}
    return jsonify(result)

@app.route('/load_percent', methods=["GET"])
def load_percent():
    if request.method == "GET":
        author = request.args['author']
        topic = request.args['topic']
        m = mongo.db.coments  # Here Mail is your Table Name
        k = m.find()
        result = []
        for i in k:
            if i['theme'] == topic:
                result = i
                break
    result = [i['author'] for i in result['posts']]
    result = {i: result.count(i) for i in result}
    arr = list(result.values())
    result = (result[author]*100)/sum((int(arr[i]) for i in range(0, int(len(arr)))))
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
