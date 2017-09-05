from flask_restful import reqparse, abort, Resource

users = {}
parser = reqparse.RequestParser()
parser.add_argument('name')

class User(Resource):
    def get(self, user_id):
        return { user_id: users[user_id] }

    def post(self, user_id):
        args = parser.parse_args()
        users[user_id] = { 'name': args['name'] }

        return users[user_id], 201