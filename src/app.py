from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
   return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": False },


]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # decoded_object = request.get_json()
    # todos.append(decoded_object) #Inserta al final del array
    # return jsonify(todos) , 200
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)
    else:
        raise Exception("sorry, no numbers below zero")
    return jsonify(todos) , 200
   

 
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)