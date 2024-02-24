from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [{'name':'Ricardo',
               'skills':['Python','Flask']},
              {'name':'Galleani',
               'skills':['Python','Django']}]
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def developer(id):
    if request.method == 'GET':
        developer = developers[id]
        print(developer)
        return jsonify(developer)
    elif request.method == 'PUT':
         info = json.loads(request.data)
         developers[id] = info
         return jsonify(info)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status':'successful','message':'Record deleted'})


if __name__ == '__main__':
    app.run()
