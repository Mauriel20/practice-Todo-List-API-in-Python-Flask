from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
   return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },

]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = request.get_json()
    todos.append(decoded_object) #Inserta al final del array
    return jsonify(todos) , 200





 
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)