from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        return {'messsage': 'user 1'}


class User(Resource):
    def post(self):
        return {'messsage': 'teste'}

    def get(self, cpf):
        return {'messsage': 'CPF'}


api.add_resource(User, '/user')
api.add_resource(Users, '/users', '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)
