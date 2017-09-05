from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, UserList
from resources.criteria import CriteriaList
from resources.evaluations import Evaluation

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<int:user_id>')

api.add_resource(CriteriaList, '/criteria')

api.add_resource(Evaluation, '/eval/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True)