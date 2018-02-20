from flask import Flask
from flask.ext.restful import Api,Resource

app = Flask(__name__)
app = Api(app)

class UserAPI(Resource):
    def get(self, id):
        pass
    def put(self, id):
        pass
    def delete(self, id):
        pass
    def post(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>',endpoint="user")


if __name__ == '__main__':
    app.run()