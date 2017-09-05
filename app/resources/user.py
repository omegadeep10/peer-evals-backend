from flask_restful import reqparse, abort, Resource
from db import users

class UserList(Resource):
    def get(self):
        return users

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json', help='No name provided')
        args = parser.parse_args()
        
        # get an integer between 1-100 that's not already used as a user_id
        unused_user_id = None
        used_user_ids = []
        
        for user_id in users:
            used_user_ids.append(user_id)
        
        for i in range(1, 100):
            if i in used_user_ids:
                pass
            else:
                unused_user_id = i
                break

        # add our new user
        users[unused_user_id] = {
            'user_id': unused_user_id,
            'name': args['name'] 
        }

        # return said user
        return users[unused_user_id], 201


#helper function
def abort_if_user_does_not_exist(user_id):
    if user_id not in users:
        abort(404, message="User with the id {} does not exist.".format(user_id))


class User(Resource):
    def get(self, user_id):
        abort_if_user_does_not_exist(user_id)
        return users[user_id]

    def delete(self, user_id):
        abort_if_user_does_not_exist(user_id)
        del users[user_id]
        return '', 204