import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db": "mydb",
    "host": os.environ.get("MONGODB_HOST", "localhost"),
    "port": 27017,
    "username": "root",
    "password": "root",
    "authentication_source": "admin"
}


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('cpf', type=str, required=True, help="CPF is required")
_user_parser.add_argument('email', type=str, required=True, help="Email is required")
_user_parser.add_argument('first_name', type=str, required=True, help="First name is required")
_user_parser.add_argument('last_name', type=str, required=True, help="Last name is required")
_user_parser.add_argument('birth_date', type=str)


api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateField()


class Users(Resource):
    def get(self):
        return {'messsage': 'user 1'}

class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        # In a real app we'd probably validate uniqueness here or handle the exception
        # from mongoengine if the CPF/Email already exists.
        UserModel(**data).save()
        return {'message': 'User created successfully'}, 201

class UserDetail(Resource):
    def get(self, cpf):
        # Implementation for getting a user by CPF would go here
        # For now, returning the stub response as requested/implied by previous code
        return {'messsage': 'CPF: ' + cpf}


api.add_resource(Users, '/users')
api.add_resource(User, '/user')
api.add_resource(UserDetail, '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
