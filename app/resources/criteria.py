from flask_restful import reqparse, abort, Resource
from db import criteria

class CriteriaList(Resource):
    def get(self):
        return criteria