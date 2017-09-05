from flask_restful import reqparse, abort, Resource
from db import eval

#helper function
def abort_if_eval_does_not_exist(eval_id):
    if eval_id not in eval:
        abort(404, message="Eval with the id {} does not exist.".format(eval_id))

class Evaluation(Resource):
    def get(self, user_id):
        matching = []
        for e in eval.items():
            if (e[1]['user_id'] == user_id):
                matching.append(e[1])
    
        return matching

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('evaluated_user_id', type=int, required=True, location='json', help='No evaluated_user_id specified')
        parser.add_argument('criteria_id', type=int, required=True, location='json', help='No criteria selected')
        parser.add_argument('score', type=int, required=True, location='json', help='No score provided')
        args = parser.parse_args()

        # get an integer between 1-100 that's not already used as a user_id
        unused_eval_id = None
        used_eval_ids = []
        
        for e in eval:
            used_eval_ids.append(e)
        
        for i in range(1, 1000):
            if i not in used_eval_ids:
                unused_eval_id = i
                break
        

        eval[unused_eval_id] = {
            'eval_id': unused_eval_id,
            'user_id': user_id,
            'evaluated_user_id': args['evaluated_user_id'],
            'criteria_id': args['criteria_id'],
            'score': args['score']
        }


        return eval[unused_eval_id]