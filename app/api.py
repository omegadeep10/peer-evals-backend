from flask import Flask
from flask_restful import Resource, Api
from resources.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)