from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


developers = [{'id': '0',
               'name': 'Ricardo',
               'skills': ['Python', 'Flask']},
              {'id': '1',
               'name': 'Galleani',
               'skills': ['Python', 'Django']}]



class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer id {} does not exist.'.format(id)
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Unknown error. Contact API admin.'
            response = {'status': 'error', 'message': message}
        return response
    def put(self, id):
        info = json.loads(request.data)
        developers[id] = info
        return info
    def delete(self, id):
        developers.pop(id)
        return {'status': 'successful', 'message': 'Record deleted'}

class Developer_list(Resource):
    def get(self):
        return developers
    def post(self):
        info = json.loads(request.data)
        position = len(developers)
        info['id'] = position
        developers.append(info)
        return {'status': 'success', 'message': 'Entry recorded.'}

api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(Developer_list, '/dev/')


if __name__ == '__main__':
    app.run(debug=True)