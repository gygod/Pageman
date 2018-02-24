from flask import Flask, jsonify
from flask_restful import Api, Resource
from uuid import uuid4
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO_URI'] = ''

data = [
    {
        'id':1,
        'title': 'something',
        'done': False
    },
    {
        'id':2,
        'title': 'something',
        'done': True
    }
]



@app.route('/')

def show_data():
    print(str(uuid4()))
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host="localhost", debug=True)