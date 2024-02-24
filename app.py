from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [{'id': '0',
               'name': 'Ricardo',
               'skills': ['Python', 'Flask']},
              {'id': '1',
               'name': 'Galleani',
               'skills': ['Python', 'Django']}]


# returns, add and delete a developer by id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer id {} does not exist.'.format(id)
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Unknown error. Contact API admin.'
            response = {'status': 'error', 'message': message}
        return jsonify(response)
    elif request.method == 'PUT':
        info = json.loads(request.data)
        developers[id] = info
        return jsonify(info)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'successful', 'message': 'Record deleted'})


# show all developers and add a new developer
@app.route('/dev/', methods=['POST', 'GET'])
def developer_list():
    if request.method == 'POST':
        info = json.loads(request.data)
        position = len(developers)
        info['id'] = position
        developers.append(info)
        return jsonify({'status': 'success', 'message': 'Entry recorded.'})
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run()
